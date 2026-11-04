# Stock Sourcing Usage for CofVid

> How to use the stock image and video tools effectively — query construction,
> provider selection, license awareness, and integration with the asset pipeline.

## Available Stock Tools

| Tool | Provider | Content | Cost | Auth / Key | Best For |
|------|----------|---------|------|-----------|----------|
| `coverr_video` | Coverr | Video clips | Free | None (Zero key) | Modern lifestyle, cinematic, nature, urban B-roll (HD/4K) |
| `mixkit_video` | Mixkit (Envato) | Video clips | Free | None (Zero key) | High-quality curated footage, clean tech & business scenes |
| `pixabay_video` | Pixabay | Video clips | Free | Optional key | Category-filtered video, animation clips |
| `pixabay_image` | Pixabay | Photos, illustrations | Free | Optional key | Large library (5M+), category filtering |
| `pexels_video` | Pexels | Video clips | Free | *Deprecated* | Keys halted; replaced by Coverr & Mixkit |
| `pexels_image` | Pexels | Photos | Free | *Deprecated* | Keys halted; replaced by Pixabay |

## Provider Selection Guide

### When to Use Coverr (`coverr_video`)
- Need **cinematic B-roll** (urban, nature, technology, lifestyle)
- Want **HD and 4K quality** with zero API keys required
- Fast, reliable stock footage with commercial license

### When to Use Mixkit (`mixkit_video`)
- Need **curated Envato stock footage** with consistent production value
- Business, tech, nature, and office B-roll
- Completely free without API key (via local scraping)

### When to Use Pixabay (`pixabay_video` / `pixabay_image`)
- Need **category-based filtering** (nature, science, computer, etc.)
- Want **illustrations, vectors**, or animation clips
- Optional free developer key in `.env`

### Decision Flow
```
Need stock image?
└── General photo / illustration / vector? → pixabay_image

Need stock video?
├── Need cinematic lifestyle / urban / nature B-roll? → coverr_video (zero key)
├── Need clean curated business / tech B-roll? → mixkit_video (zero key)
├── Need animation clips or category filter? → pixabay_video
└── Auto-selection? → video_selector (picks best available)
```

## Input Parameters Guide

### pexels_image / pexels_video
```python
{
    "query": "city skyline sunset",      # Required: search term
    "orientation": "landscape",           # Optional: landscape/portrait/square
    "size": "large",                      # Optional: large/medium/small
    "color": "FF6B35",                    # Optional: hex without # or color name
    "per_page": 5,                        # Results per page (1-80)
    "download_size": "large2x",           # Image: original/large2x/large/medium
    "preferred_quality": "hd",            # Video: hd/sd
    "output_path": "assets/images/s3.jpg" # Where to save
}
```

### pixabay_image / pixabay_video
```python
{
    "query": "server room",              # Required: search term (max 100 chars)
    "image_type": "photo",               # Image: all/photo/illustration/vector
    "video_type": "film",                # Video: all/film/animation
    "orientation": "horizontal",          # all/horizontal/vertical
    "category": "computer",              # One of 20 categories
    "colors": "blue,gray",              # Comma-separated color names
    "editors_choice": true,              # Curated high-quality only
    "safesearch": true,                  # Always true for production
    "output_path": "assets/video/s5.mp4" # Where to save
}
```

## Gotchas and Best Practices

### 1. Pixabay URLs Expire
Pixabay download URLs contain embedded tokens that expire. **Always download immediately** after searching. The tools handle this automatically, but never cache Pixabay URLs for later use.

### 2. Pixabay Resolution Limit
Standard Pixabay API users get max 1280px wide images (`largeImageURL`). Full resolution requires approved API access. For most video production overlays, 1280px is sufficient.

### 3. Pexels Auth Header
Pexels uses a bare API key in the `Authorization` header (NOT `Bearer`). The tool handles this, but be aware if debugging.

### 4. Search Results Vary by Locale
Pexels supports 28 locales. If searching for culturally specific content, set the locale parameter.

### 5. Stock Images Are Deterministic
Unlike AI generation, searching "ocean waves" twice returns the same results. If the first result isn't good enough, try different keywords — don't retry the same query.

### 6. Duration Filtering for Video
Both stock video tools support `min_duration` and `max_duration` parameters. Use these to avoid downloading 30-second clips when you only need 4 seconds — it saves bandwidth and time.

## Integration with Asset Pipeline

Stock tools integrate exactly like generation tools. In the asset manifest:

```json
{
    "id": "broll-s3",
    "type": "image",
    "subtype": "broll",
    "path": "assets/images/broll-s3.jpg",
    "source_tool": "pexels_image",
    "scene_id": "scene-3",
    "cost_usd": 0.00,
    "metadata": {
        "photographer": "Joey Farina",
        "source_url": "https://www.pexels.com/photo/2014422/",
        "license": "Pexels License (free, no attribution required)"
    }
}
```

The Edit Director and Compose Director treat stock assets identically to generated ones — they just reference the file path from the manifest.

## Licensing Summary

| Provider | Commercial Use | Attribution | Restrictions |
|----------|---------------|-------------|-------------|
| Pexels | Yes, free | Not required (appreciated) | Cannot sell unaltered; cannot imply endorsement |
| Pixabay | Yes, free | Not required | Cannot sell unaltered; cannot create competing stock service |

Both are safe for all CofVid use cases. No licensing fees, no per-use royalties, no attribution obligations.
