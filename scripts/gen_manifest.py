#!/usr/bin/env python3
"""Regenerate manifest.json from whatever image files live in images/.

Titles/categories you set by hand in manifest.json are preserved (matched on
"src"). New images get a title/category guessed from the filename:

    jackets_leather-biker.jpg   -> category "Jackets", title "Leather biker"
    blue-oxford-shirt.jpg       -> category "",        title "Blue oxford shirt"

So the fast way to file something is to name it "<category>_<description>.jpg".
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(ROOT, "images")
MANIFEST = os.path.join(ROOT, "manifest.json")
EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"}


def prettify(text):
    text = text.replace("-", " ").replace("_", " ").strip()
    text = re.sub(r"\s+", " ", text)
    return text[:1].upper() + text[1:] if text else text


def guess(filename):
    stem = os.path.splitext(filename)[0]
    if "_" in stem:
        cat, rest = stem.split("_", 1)
        return prettify(cat), prettify(rest)
    return "", prettify(stem)


def main():
    existing = {}
    if os.path.exists(MANIFEST):
        try:
            with open(MANIFEST) as fh:
                data = json.load(fh)
            for entry in (data if isinstance(data, list) else data.get("photos", [])):
                if isinstance(entry, dict) and entry.get("src"):
                    existing[entry["src"]] = entry
        except (ValueError, OSError):
            pass

    files = []
    if os.path.isdir(IMAGES_DIR):
        files = [
            f for f in os.listdir(IMAGES_DIR)
            if os.path.splitext(f)[1].lower() in EXTS and not f.startswith(".")
        ]
    files.sort()

    out = []
    for name in files:
        src = "images/" + name
        if src in existing:
            out.append(existing[src])
            continue
        cat, title = guess(name)
        out.append({"src": src, "title": title, "category": cat})

    with open(MANIFEST, "w") as fh:
        json.dump(out, fh, indent=2)
        fh.write("\n")

    print("Wrote %d entries to manifest.json" % len(out))


if __name__ == "__main__":
    main()
