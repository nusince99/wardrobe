# My Wardrobe

A free photo site for showcasing my clothing, hosted on GitHub Pages.

**Live site:** https://nusince99.github.io/wardrobe/

## Adding photos

1. Open the **`images`** folder on GitHub -> **Add file -> Upload files**.
2. Drag in your clothing photos and commit.
3. Refresh the site -- new photos appear automatically. No manifest to edit.

The site reads the `images/` folder live through the GitHub API, so there is
no build step and nothing to maintain.

### Naming photos

The caption shown on the site is guessed from the filename:

| Filename | Category | Title |
|---|---|---|
| `jackets_leather-biker.jpg` | Jackets | Leather biker |
| `shoes_white-sneakers.jpg` | Shoes | White sneakers |
| `blue-oxford-shirt.jpg` | *(none)* | Blue oxford shirt |

Pattern: `category_description.jpg`. Categories become filter buttons automatically.

### Overriding a caption

Add an entry to `manifest.json` to override the title/category for a photo:

```json
[
  { "src": "images/jackets_leather-biker.jpg", "title": "AllSaints biker", "category": "Outerwear" }
]
```

`scripts/gen_manifest.py` can scaffold that file from the current images:

```bash
python3 scripts/gen_manifest.py
```

## Running locally

```bash
python3 -m http.server 8000   # then open http://localhost:8000
```
