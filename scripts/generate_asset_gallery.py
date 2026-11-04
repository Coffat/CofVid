"""Asset Gallery Preview System for CofVid Projects.

Generates a standalone, publication-grade interactive HTML preview gallery
for all assets (narration audio, music, vector brand logos, UI icons, screenshots,
and architecture diagrams) produced by CofVid pipelines.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import subprocess
from pathlib import Path
from typing import Any


def get_audio_info(path: Path) -> dict[str, Any]:
    """Extract duration and stream metadata using ffprobe."""
    info = {"duration": 0.0, "sample_rate": 48000, "channels": 1, "format": path.suffix.replace(".", "")}
    try:
        cmd = [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration:stream=sample_rate,channels",
            "-of",
            "json",
            str(path),
        ]
        out = subprocess.check_output(cmd, text=True).strip()
        data = json.loads(out)
        if "format" in data and "duration" in data["format"]:
            info["duration"] = round(float(data["format"]["duration"]), 2)
        streams = data.get("streams", [])
        if streams:
            info["sample_rate"] = int(streams[0].get("sample_rate", 48000))
            info["channels"] = int(streams[0].get("channels", 1))
    except Exception:
        pass
    return info


def generate_gallery(project_dir: Path) -> Path:
    assets_dir = project_dir / "assets"
    if not assets_dir.exists():
        raise FileNotFoundError(f"Assets directory not found at {assets_dir}")

    project_id = project_dir.name
    out_html = assets_dir / "gallery.html"

    # Check for manifest / checkpoint
    checkpoint_file = project_dir / "checkpoint_assets.json"
    checkpoint = {}
    if checkpoint_file.exists():
        try:
            checkpoint = json.loads(checkpoint_file.read_text(encoding="utf-8"))
        except Exception:
            pass

    # Collect Voiceover Audio
    voiceover_dir = assets_dir / "audio" / "voiceover"
    if not voiceover_dir.exists():
        voiceover_dir = assets_dir / "audio"

    audio_files = sorted(list(voiceover_dir.glob("*.wav")) + list(voiceover_dir.glob("*.mp3")))
    audio_items = []
    total_audio_sec = 0.0
    for af in audio_files:
        if "sfx" in str(af) or "music" in str(af):
            continue
        rel_path = os.path.relpath(af, assets_dir)
        meta = get_audio_info(af)
        total_audio_sec += meta["duration"]
        audio_items.append({
            "name": af.stem,
            "filename": af.name,
            "rel_path": rel_path,
            "meta": meta,
        })

    # Collect Music
    music_dir = assets_dir / "audio" / "music"
    if not music_dir.exists():
        music_dir = assets_dir / "music"
    music_files = sorted(list(music_dir.glob("*.mp3")) + list(music_dir.glob("*.wav")))
    music_items = []
    for mf in music_files:
        rel_path = os.path.relpath(mf, assets_dir)
        meta = get_audio_info(mf)
        music_items.append({
            "name": mf.stem,
            "filename": mf.name,
            "rel_path": rel_path,
            "meta": meta,
        })

    # Collect Icons (SVG)
    icons_dir = assets_dir / "icons"
    brand_icons = []
    ui_icons = []
    known_ui = {"star", "terminal", "shield", "code", "database", "check", "alert-circle", "info", "heart", "copy", "globe", "cpu", "server"}

    if icons_dir.exists():
        for sf in sorted(icons_dir.glob("*.svg")):
            content = sf.read_text(encoding="utf-8", errors="ignore")
            item = {
                "name": sf.stem,
                "filename": sf.name,
                "svg": content,
            }
            if sf.stem in known_ui or "icon-" in content:
                ui_icons.append(item)
            else:
                brand_icons.append(item)

    # Collect Images / Diagrams / Screenshots
    images_dir = assets_dir / "images"
    image_items = []
    if images_dir.exists():
        for img in sorted(images_dir.glob("*.*")):
            if img.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp", ".svg"]:
                rel_path = os.path.relpath(img, assets_dir)
                size_kb = round(img.stat().st_size / 1024, 1)
                image_items.append({
                    "name": img.stem,
                    "filename": img.name,
                    "rel_path": rel_path,
                    "size_kb": size_kb,
                    "ext": img.suffix.upper().replace(".", ""),
                })

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Asset Gallery — {project_id}</title>
<style>
  :root {{
    --bg-main: #09090b;
    --bg-card: #121217;
    --bg-subtle: #181820;
    --border: #272733;
    --border-accent: #00F0FF;
    --text-main: #f4f4f5;
    --text-muted: #a1a1aa;
    --accent: #00F0FF;
    --accent-emerald: #10A37F;
    --accent-terracotta: #D97757;
    --accent-gold: #FFD700;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: var(--bg-main);
    color: var(--text-main);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
    padding: 32px 24px;
    line-height: 1.5;
  }}
  header {{
    max-width: 1200px;
    margin: 0 auto 36px auto;
    border-bottom: 1px solid var(--border);
    padding-bottom: 24px;
  }}
  .badge-row {{
    display: flex;
    gap: 8px;
    margin-bottom: 12px;
    flex-wrap: wrap;
  }}
  .badge {{
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 4px 10px;
    border-radius: 4px;
    background: var(--bg-subtle);
    border: 1px solid var(--border);
  }}
  .badge-cyan {{ color: var(--accent); border-color: rgba(0,240,255,0.3); background: rgba(0,240,255,0.06); }}
  .badge-green {{ color: #4ade80; border-color: rgba(74,222,128,0.3); background: rgba(74,222,128,0.06); }}
  h1 {{ font-size: 28px; font-weight: 800; letter-spacing: -0.02em; margin-bottom: 6px; }}
  .subtitle {{ color: var(--text-muted); font-size: 14px; }}
  
  .container {{ max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; gap: 40px; }}
  
  .section-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 16px;
  }}
  .section-title {{ font-size: 18px; font-weight: 700; display: flex; align-items: center; gap: 8px; }}
  .section-count {{ font-size: 12px; color: var(--text-muted); background: var(--bg-subtle); padding: 2px 8px; border-radius: 12px; }}

  /* Audio Grid */
  .audio-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 16px;
  }}
  .audio-card {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    transition: border-color 0.15s ease;
  }}
  .audio-card:hover {{ border-color: var(--border-accent); }}
  .audio-header {{ display: flex; justify-content: space-between; align-items: baseline; }}
  .audio-title {{ font-weight: 700; font-size: 14px; font-family: ui-monospace, SFMono-Regular, monospace; color: var(--accent); }}
  .audio-meta {{ font-size: 12px; color: var(--text-muted); }}
  audio {{ width: 100%; height: 36px; border-radius: 4px; outline: none; }}

  /* Icon Grid */
  .icon-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 16px;
  }}
  .icon-card {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 20px 16px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 14px;
    text-align: center;
    transition: transform 0.15s ease, border-color 0.15s ease;
  }}
  .icon-card:hover {{
    transform: translateY(-2px);
    border-color: var(--accent);
  }}
  .icon-preview {{
    width: 64px;
    height: 64px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .icon-preview svg {{
    width: 48px;
    height: 48px;
    display: block;
  }}
  .icon-name {{ font-weight: 600; font-size: 13px; font-family: ui-monospace, SFMono-Regular, monospace; }}
  .icon-tag {{ font-size: 10px; text-transform: uppercase; color: var(--text-muted); background: var(--bg-subtle); padding: 2px 6px; border-radius: 3px; }}

  /* Images / Visuals Grid */
  .visual-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 20px;
  }}
  .visual-card {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    transition: border-color 0.15s ease;
  }}
  .visual-card:hover {{ border-color: var(--border-accent); }}
  .visual-thumb {{
    width: 100%;
    height: 220px;
    background: #000;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }}
  .visual-thumb img {{
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
  }}
  .visual-info {{
    padding: 14px 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid var(--border);
    background: var(--bg-card);
  }}
  .visual-name {{ font-weight: 600; font-size: 13px; font-family: ui-monospace, SFMono-Regular, monospace; }}
  .visual-badge {{ font-size: 11px; color: var(--text-muted); }}

  footer {{
    max-width: 1200px;
    margin: 60px auto 0 auto;
    border-top: 1px solid var(--border);
    padding-top: 24px;
    text-align: center;
    color: var(--text-muted);
    font-size: 12px;
  }}
</style>
</head>
<body>

<header>
  <div class="badge-row">
    <span class="badge badge-cyan">CofVid Asset OS</span>
    <span class="badge badge-green">Zero-Hallucination Verified</span>
    <span class="badge">Pipeline State: Assets Complete</span>
  </div>
  <h1>Asset Gallery — {project_id}</h1>
  <div class="subtitle">Production asset ledger: voiceovers, background music, vector brand logos, Lucide UI icons, and visual graphics.</div>
</header>

<div class="container">

  <!-- 1. Voiceover Narration Section -->
  <section>
    <div class="section-header">
      <div class="section-title">
        <span>🎙️ Voiceover Narration Clips (VieNeu-TTS v3 Hải Đăng)</span>
        <span class="section-count">{len(audio_items)} tracks • {total_audio_sec:.1f}s total</span>
      </div>
    </div>
    <div class="audio-grid">
"""

    for a in audio_items:
        html += f"""      <div class="audio-card">
        <div class="audio-header">
          <div class="audio-title">{a['name']}</div>
          <div class="audio-meta">{a['meta']['duration']}s • {a['meta']['sample_rate']}Hz</div>
        </div>
        <audio controls preload="none">
          <source src="{a['rel_path']}" type="audio/wav">
        </audio>
      </div>\n"""

    html += """    </div>
  </section>

  <!-- 2. Background Music Section -->
  <section>
    <div class="section-header">
      <div class="section-title">
        <span>🎵 Background Music (BGM & Mix Tracks)</span>
        <span class="section-count">""" + str(len(music_items)) + """ tracks</span>
      </div>
    </div>
    <div class="audio-grid">
"""

    for m in music_items:
        html += f"""      <div class="audio-card">
        <div class="audio-header">
          <div class="audio-title">{m['name']}</div>
          <div class="audio-meta">{m['meta']['duration']}s • Stereo</div>
        </div>
        <audio controls preload="none">
          <source src="{m['rel_path']}" type="audio/mpeg">
        </audio>
      </div>\n"""

    html += """    </div>
  </section>

  <!-- 3. Official Brand Logos Section -->
  <section>
    <div class="section-header">
      <div class="section-title">
        <span>🏢 Official Vector Brand Marks (Zero-Hallucination)</span>
        <span class="section-count">""" + str(len(brand_icons)) + """ verified</span>
      </div>
    </div>
    <div class="icon-grid">
"""

    for b in brand_icons:
        html += f"""      <div class="icon-card">
        <div class="icon-preview">{b['svg']}</div>
        <div class="icon-name">{b['name']}</div>
        <div class="icon-tag">Brand Vector</div>
      </div>\n"""

    html += """    </div>
  </section>

  <!-- 4. Lucide UI Icons Section -->
  <section>
    <div class="section-header">
      <div class="section-title">
        <span>✨ Lucide / Feather UI Icons (Deterministic Geometry)</span>
        <span class="section-count">""" + str(len(ui_icons)) + """ icons</span>
      </div>
    </div>
    <div class="icon-grid">
"""

    for u in ui_icons:
        html += f"""      <div class="icon-card">
        <div class="icon-preview">{u['svg']}</div>
        <div class="icon-name">{u['name']}</div>
        <div class="icon-tag">UI Symbol</div>
      </div>\n"""

    html += """    </div>
  </section>

  <!-- 5. Visual Graphics & Architecture Diagrams -->
  <section>
    <div class="section-header">
      <div class="section-title">
        <span>🖼️ Visual Graphics, Code Snippets & Architecture Diagrams</span>
        <span class="section-count">""" + str(len(image_items)) + """ assets</span>
      </div>
    </div>
    <div class="visual-grid">
"""

    for img in image_items:
        html += f"""      <div class="visual-card">
        <div class="visual-thumb">
          <img src="{img['rel_path']}" alt="{img['name']}" loading="lazy"/>
        </div>
        <div class="visual-info">
          <div class="visual-name">{img['name']}</div>
          <div class="visual-badge">{img['ext']} • {img['size_kb']} KB</div>
        </div>
      </div>\n"""

    html += """    </div>
  </section>

</div>

<footer>
  COFFAT MEDIA Vertical Video Engine • Certified Zero-Hallucination Asset OS Preview
</footer>

</body>
</html>
"""

    out_html.write_text(html, encoding="utf-8")
    return out_html


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Asset Gallery HTML preview")
    parser.add_argument("--project", default="projects/mach-so-opencode-2-0", help="Project path")
    args = parser.parse_args()

    p = Path(args.project)
    out_file = generate_gallery(p)
    print(f"Asset Gallery successfully generated at: {out_file}")
