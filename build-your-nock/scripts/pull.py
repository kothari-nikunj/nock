#!/usr/bin/env python3
"""Pull all Granola notes (with transcripts) for ONE account/workspace via the official API.

Usage:
    GRANOLA_API_KEY=grn_... python3 pull.py
    # or put the key in ~/.granola_api_key (chmod 600)

Writes to ./lens-data/: notes/<id>.json (one per note), folders.json, index.json.
Resumable (skips already-saved notes) and backs off on 429s.
"""
import json, os, time, urllib.request, urllib.error, urllib.parse

def load_key():
    k = os.environ.get("GRANOLA_API_KEY")
    if k:
        return k.strip()
    path = os.path.expanduser("~/.granola_api_key")
    if os.path.exists(path):
        return open(path).read().strip()
    raise SystemExit("Set GRANOLA_API_KEY env var or create ~/.granola_api_key")

KEY = load_key()
BASE = "https://public-api.granola.ai/v1"
OUT = os.path.join(os.getcwd(), "lens-data")
NOTES_DIR = os.path.join(OUT, "notes")
os.makedirs(NOTES_DIR, exist_ok=True)

def call(path, params=None, tries=6):
    url = BASE + path + (("?" + urllib.parse.urlencode(params)) if params else "")
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"Authorization": "Bearer " + KEY})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = min(60, 2 ** attempt)
                print(f"  429 — backing off {wait}s", flush=True); time.sleep(wait); continue
            if e.code >= 500:
                time.sleep(2 ** attempt); continue
            raise
    raise RuntimeError(f"failed after {tries}: {path}")

def paginate(path):
    cursor, out = None, []
    while True:
        p = {"page_size": 30}
        if cursor: p["cursor"] = cursor
        d = call(path, p)
        out += d.get("notes", d.get("folders", []))
        if not d.get("hasMore"): break
        cursor = d.get("cursor")
    return out

folders = paginate("/folders")
json.dump(folders, open(os.path.join(OUT, "folders.json"), "w"), indent=2)
print(f"folders: {len(folders)}", flush=True)

summaries = paginate("/notes")
print(f"notes to fetch: {len(summaries)}", flush=True)

index, done = [], 0
for s in summaries:
    nid = s["id"]
    path = os.path.join(NOTES_DIR, nid + ".json")
    if os.path.exists(path):
        full = json.load(open(path))
    else:
        full = call(f"/notes/{nid}", {"include": "transcript"})
        json.dump(full, open(path, "w"), indent=2)
        time.sleep(0.4)  # gentle throttle
    index.append({
        "id": nid, "title": full.get("title"), "created_at": full.get("created_at"),
        "attendees": [a.get("email") or a.get("name") for a in (full.get("attendees") or [])],
        "folders": [m.get("name") for m in (full.get("folder_membership") or [])],
        "transcript_len": len(full.get("transcript") or []),
    })
    done += 1
    if done % 20 == 0: print(f"  {done}/{len(summaries)}", flush=True)

json.dump(index, open(os.path.join(OUT, "index.json"), "w"), indent=2)
print(f"DONE — {done} notes in {NOTES_DIR}", flush=True)
