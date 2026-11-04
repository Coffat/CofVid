"""Open Design graphic and editorial component generation tool.

Integrates Open Design (open-design design-systems, design-tokens, and templates)
into CofVid for documentary, explainer, and editorial motion graphics.
Supports rendering DOM snippets for HyperFrames, transparent WebM (alpha channel)
via headless Chrome and FFmpeg, and high-resolution still PNG cards.
"""

from __future__ import annotations

import json
import logging
import os
import re
import shutil
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any, Optional

from tools.base_tool import (
    BaseTool,
    Determinism,
    ExecutionMode,
    ResourceProfile,
    ToolResult,
    ToolRuntime,
    ToolStability,
    ToolStatus,
    ToolTier,
)

logger = logging.getLogger(__name__)

# Fallback presets when external/open-design is not present or theme not found
BUILTIN_THEME_TOKENS: dict[str, dict[str, str]] = {
    "editorial": {
        "--bg": "#fbf7f0",
        "--surface": "#fffdf8",
        "--surface-warm": "#f1e6d6",
        "--fg": "#1f1a16",
        "--fg-2": "#4b4038",
        "--muted": "#7d7168",
        "--meta": "#9a5a2f",
        "--border": "#ded3c5",
        "--border-soft": "#eee5da",
        "--accent": "#9a5a2f",
        "--accent-on": "#ffffff",
        "--font-display": "Georgia, 'Times New Roman', serif",
        "--font-body": "'Source Serif Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', serif",
        "--font-mono": "'IBM Plex Mono', 'SF Mono', ui-monospace, Menlo, monospace",
        "--radius-sm": "3px",
        "--radius-md": "6px",
        "--radius-lg": "10px",
    },
    "dark-data": {
        "--bg": "#0b0f19",
        "--surface": "#111827",
        "--surface-warm": "#1f2937",
        "--fg": "#f9fafb",
        "--fg-2": "#e5e7eb",
        "--muted": "#9ca3af",
        "--meta": "#38bdf8",
        "--border": "#1e293b",
        "--border-soft": "#334155",
        "--accent": "#0284c7",
        "--accent-on": "#ffffff",
        "--font-display": "-apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', sans-serif",
        "--font-body": "-apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', sans-serif",
        "--font-mono": "'JetBrains Mono', 'Fira Code', 'SF Mono', monospace",
        "--radius-sm": "4px",
        "--radius-md": "8px",
        "--radius-lg": "12px",
    },
    "minimalist-news": {
        "--bg": "#ffffff",
        "--surface": "#f8f9fa",
        "--surface-warm": "#f1f3f5",
        "--fg": "#111827",
        "--fg-2": "#374151",
        "--muted": "#6b7280",
        "--meta": "#e11d48",
        "--border": "#e5e7eb",
        "--border-soft": "#f3f4f6",
        "--accent": "#e11d48",
        "--accent-on": "#ffffff",
        "--font-display": "Helvetica Neue, Arial, sans-serif",
        "--font-body": "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
        "--font-mono": "'SF Mono', ui-monospace, monospace",
        "--radius-sm": "2px",
        "--radius-md": "4px",
        "--radius-lg": "8px",
    },
    "atelier-zero": {
        "--bg": "#f5f4ef",
        "--surface": "#ffffff",
        "--surface-warm": "#eae8df",
        "--fg": "#1a1a1a",
        "--fg-2": "#3f3f3f",
        "--muted": "#767676",
        "--meta": "#2b4c7e",
        "--border": "#dcdad1",
        "--border-soft": "#ebe9e2",
        "--accent": "#2b4c7e",
        "--accent-on": "#ffffff",
        "--font-display": "Charter, Georgia, serif",
        "--font-body": "-apple-system, BlinkMacSystemFont, sans-serif",
        "--font-mono": "'Courier New', monospace",
        "--radius-sm": "4px",
        "--radius-md": "8px",
        "--radius-lg": "12px",
    },
    "bold": {
        "--bg": "#09090b",
        "--surface": "#18181b",
        "--surface-warm": "#27272a",
        "--fg": "#fafafa",
        "--fg-2": "#d4d4d8",
        "--muted": "#a1a1aa",
        "--meta": "#f43f5e",
        "--border": "#27272a",
        "--border-soft": "#3f3f46",
        "--accent": "#f43f5e",
        "--accent-on": "#ffffff",
        "--font-display": "Impact, -apple-system, sans-serif",
        "--font-body": "-apple-system, BlinkMacSystemFont, 'Inter', sans-serif",
        "--font-mono": "'SF Mono', monospace",
        "--radius-sm": "0px",
        "--radius-md": "2px",
        "--radius-lg": "4px",
    },
}

THEME_ALIASES: dict[str, str] = {
    "swiss-editorial": "editorial",
    "swiss": "editorial",
    "monocle": "editorial",
    "dark-data": "dark-data",
    "trading-terminal": "dark-data",
    "minimalist-news": "minimalist-news",
    "theverge": "minimalist-news",
    "wired": "minimalist-news",
    "modern-minimal": "minimal",
    "linear": "linear-app",
}


def _find_chrome_executable() -> Optional[str]:
    """Find installed Chrome / Chromium executable."""
    env_bin = os.environ.get("CHROME_BIN") or os.environ.get("GOOGLE_CHROME_BIN")
    if env_bin and os.path.isfile(env_bin):
        return env_bin

    candidates = [
        shutil.which("google-chrome"),
        shutil.which("chrome"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium-browser",
    ]
    for c in candidates:
        if c and os.path.isfile(c) and os.access(c, os.X_OK):
            return c
    return None


class OpenDesign(BaseTool):
    """Open Design graphic and editorial component generation tool."""

    name = "open_design_tool"
    version = "0.1.0"
    tier = ToolTier.CORE
    capability = "graphics"
    provider = "open_design"
    stability = ToolStability.BETA
    execution_mode = ExecutionMode.SYNC
    determinism = Determinism.DETERMINISTIC
    runtime = ToolRuntime.LOCAL

    dependencies = []
    install_instructions = (
        "Open Design operates locally via vendor repository under external/open-design.\n"
        "To enable headless rendering of PNG/WebM:\n"
        "  - Ensure Google Chrome / Chromium is installed\n"
        "  - Ensure FFmpeg is installed and accessible in PATH"
    )
    agent_skills = ["open-design", "hyperframes", "hyperframes-creative"]

    capabilities = [
        "open_design_template",
        "open_design_custom",
        "render_dom_snippet",
        "render_transparent_webm",
        "render_png_still",
        "editorial_cards",
        "data_callout",
    ]

    input_schema = {
        "type": "object",
        "properties": {
            "mode": {
                "type": "string",
                "enum": ["template", "custom"],
                "default": "template",
                "description": "Generation mode: 'template' for preset layouts or 'custom' for arbitrary HTML/CSS/GSAP.",
            },
            "theme_id": {
                "type": "string",
                "default": "editorial",
                "description": "Design system theme ID (e.g., 'editorial', 'swiss-editorial', 'dark-data', 'minimalist-news', 'atelier-zero', 'bold', 'modern', 'brutalism').",
            },
            "component_type": {
                "type": "string",
                "enum": [
                    "fullscreen_card",
                    "lower_third",
                    "stat_callout",
                    "split_screen",
                    "timeline_step",
                    "quote_card",
                ],
                "default": "fullscreen_card",
                "description": "Type of editorial component to generate.",
            },
            "props": {
                "type": "object",
                "default": {},
                "description": (
                    "Data properties for component (title, kicker, subtitle, body, stat, badge, meta, author, role, "
                    "brand_icon, brand_slug, brand_name, brand_variant, icon_size, left, right, etc.)."
                ),
            },
            "output_format": {
                "type": "string",
                "enum": ["dom_snippet", "webm_alpha", "png_still"],
                "default": "dom_snippet",
                "description": "Output deliverable: HTML DOM snippet for HyperFrames, transparent WebM video, or PNG still.",
            },
            "custom_code": {
                "type": "string",
                "default": "",
                "description": "Custom HTML/CSS snippet when mode='custom'.",
            },
            "output_path": {
                "type": "string",
                "description": "Optional destination path to save output file (HTML, PNG, or WebM).",
            },
            "width": {
                "type": "integer",
                "default": 1920,
                "description": "Canvas width in pixels (default 1920).",
            },
            "height": {
                "type": "integer",
                "default": 1080,
                "description": "Canvas height in pixels (default 1080).",
            },
            "duration_seconds": {
                "type": "number",
                "default": 5.0,
                "description": "Duration for video exports in seconds (default 5.0).",
            },
        },
    }

    resource_profile = ResourceProfile(cpu_cores=1, ram_mb=512, vram_mb=0, disk_mb=100)
    idempotency_key_fields = ["mode", "theme_id", "component_type", "props", "output_format"]
    side_effects = ["writes rendered assets to output_path if requested"]
    user_visible_verification = [
        "Verify editorial typography, contrast, and layout hierarchy",
        "Verify DOM snippet compatibility with HyperFrames",
    ]

    def __init__(self) -> None:
        super().__init__()
        self._repo_root = Path(__file__).resolve().parent.parent.parent
        self._vendor_dir = self._repo_root / "external" / "open-design"

    def get_status(self) -> ToolStatus:
        """Check if Open Design tool is available."""
        # Available if vendor repo exists or fallback templates are loaded
        return ToolStatus.AVAILABLE

    def _resolve_theme_tokens(self, theme_id: str) -> tuple[str, dict[str, str], str]:
        """Resolve theme tokens from external/open-design or fallback built-ins.
        
        Returns:
            Tuple of (canonical_theme_id, token_dict, raw_css_variables_block)
        """
        raw_id = theme_id.strip().lower()
        mapped_id = THEME_ALIASES.get(raw_id, raw_id)

        # 1. Check external/open-design/design-systems/<mapped_id>/tokens.css
        theme_path = self._vendor_dir / "design-systems" / mapped_id / "tokens.css"
        if not theme_path.is_file() and raw_id in THEME_ALIASES:
            theme_path = self._vendor_dir / "design-systems" / raw_id / "tokens.css"

        if theme_path.is_file():
            try:
                css_text = theme_path.read_text(encoding="utf-8")
                token_dict: dict[str, str] = {}
                for line in css_text.splitlines():
                    line = line.strip()
                    if line.startswith("--") and ":" in line:
                        k, _, v = line.partition(":")
                        k = k.strip()
                        v = v.rstrip(";").strip()
                        token_dict[k] = v
                return mapped_id, token_dict, css_text
            except Exception as e:
                logger.warning(f"Failed to read external tokens.css for theme {mapped_id}: {e}")

        # 2. Check built-in fallback tokens
        if mapped_id in BUILTIN_THEME_TOKENS:
            tokens = BUILTIN_THEME_TOKENS[mapped_id]
        elif raw_id in BUILTIN_THEME_TOKENS:
            tokens = BUILTIN_THEME_TOKENS[raw_id]
        else:
            tokens = BUILTIN_THEME_TOKENS["editorial"]

        css_lines = [":root {"]
        for k, v in tokens.items():
            css_lines.append(f"  {k}: {v};")
        css_lines.append("}")
        return mapped_id, tokens, "\n".join(css_lines)

    def _resolve_brand_svg(self, props: dict[str, Any], default_size: int = 40) -> str:
        """Resolve official vector SVG icon from props if brand_icon or brand_slug is provided."""
        icon_val = (
            props.get("brand_icon")
            or props.get("brand_slug")
            or props.get("brand_name")
            or props.get("icon")
        )
        if not icon_val:
            return ""
        if isinstance(icon_val, str) and icon_val.strip().startswith("<svg"):
            return icon_val.strip()

        try:
            from tools.graphics.brand_icon_tool import BrandIconTool

            tool = BrandIconTool()
            icon_type = props.get("icon_type", "brand")
            variant = props.get("brand_variant", "default")
            size = int(props.get("icon_size", default_size))
            site_url = props.get("site_url")
            res = tool.execute(
                {
                    "brand_name": str(icon_val),
                    "icon_type": icon_type,
                    "variant": variant,
                    "site_url": site_url,
                    "width": size,
                    "height": size,
                }
            )
            if res.success and res.data.get("svg"):
                return res.data["svg"]
        except Exception as exc:
            logger.debug(f"Failed to resolve brand icon {icon_val}: {exc}")
        return ""

    def _build_component_html(
        self,
        component_type: str,
        props: dict[str, Any],
        theme_id: str,
        tokens_css: str,
        width: int,
        height: int,
    ) -> str:
        """Render documentary/editorial HTML with GSAP motion attributes."""
        # Sanitize / extract props with graceful defaults
        kicker = props.get("kicker") or props.get("category") or props.get("badge") or ""
        title = props.get("title") or props.get("headline") or props.get("name") or "Editorial Focus"
        subtitle = props.get("subtitle") or props.get("role") or props.get("deck") or ""
        body = props.get("body") or props.get("description") or props.get("text") or ""
        stat = props.get("stat") or props.get("metric") or props.get("value") or ""
        meta = props.get("meta") or props.get("source") or props.get("date") or ""
        icon_svg = self._resolve_brand_svg(props)

        # Common base CSS styles using tokens
        base_css = f"""
<style>
{tokens_css}

* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}

body, html {{
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: transparent;
  font-family: var(--font-body, system-ui, sans-serif);
  color: var(--fg, #1f1a16);
  -webkit-font-smoothing: antialiased;
}}

.od-canvas {{
  position: relative;
  width: {width}px;
  height: {height}px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}}

.od-kicker {{
  font-family: var(--font-mono, monospace);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--meta, var(--accent, #9a5a2f));
  margin-bottom: 12px;
  display: inline-block;
}}

.od-title {{
  font-family: var(--font-display, serif);
  font-size: 48px;
  line-height: 1.15;
  font-weight: 700;
  color: var(--fg, #1f1a16);
  letter-spacing: -0.02em;
  margin-bottom: 16px;
}}

.od-subtitle {{
  font-family: var(--font-body, serif);
  font-size: 22px;
  line-height: 1.5;
  color: var(--fg-2, #4b4038);
  margin-bottom: 20px;
}}

.od-body {{
  font-family: var(--font-body, serif);
  font-size: 17px;
  line-height: 1.6;
  color: var(--muted, #7d7168);
}}

.od-meta {{
  font-family: var(--font-mono, monospace);
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted, #7d7168);
  margin-top: 24px;
  padding-top: 14px;
  border-top: 1px solid var(--border-soft, #eee5da);
}}
</style>
"""

        # Build markup per component_type
        if component_type == "fullscreen_card":
            kicker_or_brand_html = (
                f"""<div style="display: flex; align-items: center; gap: 16px; margin-bottom: 16px;">
  <div class="od-brand-icon" style="width: 48px; height: 48px; display: inline-flex; align-items: center; justify-content: center; flex-shrink: 0;">{icon_svg}</div>
  {f'<div class="od-kicker" style="margin-bottom: 0;">{kicker}</div>' if kicker else ''}
</div>"""
                if icon_svg
                else (f'<div class="od-kicker">{kicker}</div>' if kicker else "")
            )
            body_html = f"""
<div class="od-card-fullscreen" style="
  background: var(--surface, #ffffff);
  border: 1px solid var(--border, #ded3c5);
  border-radius: var(--radius-lg, 12px);
  padding: 64px 80px;
  max-width: 1120px;
  width: 85%;
  box-shadow: 0 24px 64px rgba(0, 0, 0, 0.08);
  position: relative;
">
  {kicker_or_brand_html}
  <h1 class="od-title" style="font-size: 56px;">{title}</h1>
  {f'<div class="od-subtitle">{subtitle}</div>' if subtitle else ''}
  {f'<p class="od-body" style="font-size: 19px; max-width: 880px;">{body}</p>' if body else ''}
  {f'<div class="od-meta">{meta}</div>' if meta else ''}
</div>
"""

        elif component_type == "lower_third":
            body_html = f"""
<div style="
  position: absolute;
  left: 80px;
  bottom: 80px;
  display: flex;
  align-items: flex-end;
">
  <div style="
    background: var(--surface, #ffffff);
    border-left: 6px solid var(--accent, #9a5a2f);
    border: 1px solid var(--border, #ded3c5);
    border-left-width: 6px;
    border-radius: var(--radius-md, 8px);
    padding: 24px 36px;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.12);
    min-width: 440px;
    max-width: 800px;
    display: flex;
    align-items: center;
    gap: 20px;
  ">
    {f'<div class="od-brand-icon" style="width: 44px; height: 44px; flex-shrink: 0; display: inline-flex; align-items: center; justify-content: center;">{icon_svg}</div>' if icon_svg else ''}
    <div style="flex: 1;">
      {f'<div class="od-kicker" style="font-size: 11px; margin-bottom: 6px;">{kicker}</div>' if kicker else ''}
      <div class="od-title" style="font-size: 32px; margin-bottom: 4px;">{title}</div>
      {f'<div class="od-subtitle" style="font-size: 17px; margin-bottom: 0;">{subtitle}</div>' if subtitle else ''}
      {f'<div class="od-meta" style="margin-top: 10px; padding-top: 6px;">{meta}</div>' if meta else ''}
    </div>
  </div>
</div>
"""

        elif component_type == "stat_callout":
            brand_stat_html = (
                f'<div class="od-brand-icon" style="display: flex; justify-content: center; margin-bottom: 12px;"><div style="width: 56px; height: 56px; display: inline-flex; align-items: center; justify-content: center;">{icon_svg}</div></div>'
                if icon_svg
                else ""
            )
            body_html = f"""
<div style="
  background: var(--surface, #ffffff);
  border: 1px solid var(--border, #ded3c5);
  border-radius: var(--radius-lg, 12px);
  padding: 56px 72px;
  max-width: 960px;
  width: 75%;
  text-align: center;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.08);
">
  {brand_stat_html}
  {f'<div class="od-kicker">{kicker}</div>' if kicker else ''}
  <div style="
    font-family: var(--font-mono, monospace);
    font-size: 104px;
    font-weight: 800;
    line-height: 1.0;
    letter-spacing: -0.03em;
    color: var(--accent, #9a5a2f);
    margin: 12px 0 20px 0;
  ">{stat or '100%'}</div>
  <div class="od-title" style="font-size: 36px; margin-bottom: 12px;">{title}</div>
  {f'<p class="od-body" style="font-size: 18px; max-width: 680px; margin: 0 auto;">{body}</p>' if body else ''}
  {f'<div class="od-meta" style="margin-top: 24px;">{meta}</div>' if meta else ''}
</div>
"""

        elif component_type == "split_screen":
            left_data = props.get("left") or {}
            right_data = props.get("right") or {}
            body_html = f"""
<div style="
  background: var(--surface, #ffffff);
  border: 1px solid var(--border, #ded3c5);
  border-radius: var(--radius-lg, 12px);
  padding: 56px 64px;
  max-width: 1360px;
  width: 90%;
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.08);
">
  <div style="text-align: center; margin-bottom: 40px;">
    {f'<div class="od-kicker">{kicker}</div>' if kicker else ''}
    <h2 class="od-title" style="font-size: 40px; margin-bottom: 8px;">{title}</h2>
    {f'<div class="od-subtitle" style="font-size: 18px; margin-bottom: 0;">{subtitle}</div>' if subtitle else ''}
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1px 1fr; gap: 48px; align-items: start;">
    <div>
      <div class="od-kicker" style="color: var(--muted, #7d7168);">{left_data.get('kicker', 'LEFT')}</div>
      <h3 class="od-title" style="font-size: 28px; margin-bottom: 12px;">{left_data.get('title', 'Thesis')}</h3>
      {f"<div style='font-family: var(--font-mono); font-size: 44px; font-weight: bold; color: var(--fg); margin-bottom: 12px;'>{left_data.get('stat')}</div>" if left_data.get('stat') else ""}
      <p class="od-body">{left_data.get('body', left_data.get('text', ''))}</p>
    </div>
    <div style="width: 1px; height: 100%; background: var(--border, #ded3c5);"></div>
    <div>
      <div class="od-kicker" style="color: var(--accent, #9a5a2f);">{right_data.get('kicker', 'RIGHT')}</div>
      <h3 class="od-title" style="font-size: 28px; margin-bottom: 12px;">{right_data.get('title', 'Antithesis')}</h3>
      {f"<div style='font-family: var(--font-mono); font-size: 44px; font-weight: bold; color: var(--accent); margin-bottom: 12px;'>{right_data.get('stat')}</div>" if right_data.get('stat') else ""}
      <p class="od-body">{right_data.get('body', right_data.get('text', ''))}</p>
    </div>
  </div>
  {f'<div class="od-meta">{meta}</div>' if meta else ''}
</div>
"""

        elif component_type == "timeline_step":
            step_badge = props.get("step_number") or props.get("badge") or "01"
            body_html = f"""
<div style="
  background: var(--surface, #ffffff);
  border: 1px solid var(--border, #ded3c5);
  border-radius: var(--radius-lg, 12px);
  padding: 56px 72px;
  max-width: 1080px;
  width: 80%;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.08);
  position: relative;
">
  <div style="display: flex; align-items: center; gap: 24px; margin-bottom: 24px;">
    <div style="
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: var(--accent, #9a5a2f);
      color: var(--accent-on, #ffffff);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-mono, monospace);
      font-size: 20px;
      font-weight: 700;
    ">{step_badge}</div>
    <div>
      {f'<div class="od-kicker" style="margin-bottom: 4px;">{kicker}</div>' if kicker else ''}
      <h2 class="od-title" style="font-size: 38px; margin-bottom: 0;">{title}</h2>
    </div>
  </div>
  {f'<div class="od-subtitle" style="font-size: 20px;">{subtitle}</div>' if subtitle else ''}
  {f'<p class="od-body" style="font-size: 18px; line-height: 1.7;">{body}</p>' if body else ''}
  {f'<div class="od-meta">{meta}</div>' if meta else ''}
</div>
"""

        elif component_type == "quote_card":
            author = props.get("author") or "Author"
            role = props.get("role") or subtitle or ""
            quote = props.get("quote") or body or title
            body_html = f"""
<div style="
  background: var(--surface, #ffffff);
  border: 1px solid var(--border, #ded3c5);
  border-radius: var(--radius-lg, 12px);
  padding: 64px 80px;
  max-width: 1040px;
  width: 80%;
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.08);
  position: relative;
">
  <div style="
    font-family: var(--font-display, serif);
    font-size: 96px;
    line-height: 0.8;
    color: var(--accent, #9a5a2f);
    opacity: 0.35;
    margin-bottom: -16px;
  ">“</div>
  <blockquote style="
    font-family: var(--font-display, serif);
    font-size: 36px;
    line-height: 1.35;
    font-style: italic;
    color: var(--fg, #1f1a16);
    margin-bottom: 32px;
  ">{quote}</blockquote>
  <div style="display: flex; align-items: center; justify-content: space-between;">
    <div>
      <div style="font-family: var(--font-body); font-size: 20px; font-weight: 700; color: var(--fg);">{author}</div>
      {f"<div style='font-family: var(--font-mono); font-size: 13px; color: var(--muted); margin-top: 4px;'>{role}</div>" if role else ""}
    </div>
    {f"<div class='od-meta' style='border: none; margin: 0; padding: 0;'>{meta}</div>" if meta else ""}
  </div>
</div>
"""

        else:
            body_html = f"""
<div style="background: var(--surface, #ffffff); padding: 48px; border-radius: var(--radius-md, 8px);">
  <h1 class="od-title">{title}</h1>
  <p class="od-body">{body}</p>
</div>
"""

        # Complete HTML with canvas wrapper
        full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Open Design — {component_type}</title>
  {base_css}
</head>
<body>
  <div class="od-canvas">
    {body_html}
  </div>
</body>
</html>"""
        return full_html

    def execute(self, inputs: dict[str, Any]) -> ToolResult:
        """Execute Open Design component generation."""
        start_time = time.time()
        mode = inputs.get("mode", "template")
        theme_id = inputs.get("theme_id", "editorial")
        component_type = inputs.get("component_type", "fullscreen_card")
        props = inputs.get("props") or {}
        output_format = inputs.get("output_format", "dom_snippet")
        custom_code = inputs.get("custom_code", "")
        output_path = inputs.get("output_path")
        width = int(inputs.get("width", 1920))
        height = int(inputs.get("height", 1080))
        duration_seconds = float(inputs.get("duration_seconds", 5.0))

        # 1. Resolve theme tokens
        canonical_theme, tokens_dict, tokens_css = self._resolve_theme_tokens(theme_id)

        # 2. Build HTML
        if mode == "custom":
            html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Open Design — Custom</title>
  <style>
{tokens_css}
body, html {{
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  background: transparent;
  font-family: var(--font-body, sans-serif);
  color: var(--fg, #1f1a16);
}}
.od-canvas {{
  width: {width}px;
  height: {height}px;
  position: relative;
  overflow: hidden;
}}
  </style>
</head>
<body>
  <div class="od-canvas">
    {custom_code}
  </div>
</body>
</html>"""
        else:
            html_content = self._build_component_html(
                component_type=component_type,
                props=props,
                theme_id=canonical_theme,
                tokens_css=tokens_css,
                width=width,
                height=height,
            )

        # 3. Handle output format
        if output_format == "dom_snippet":
            if output_path:
                out_p = Path(output_path)
                out_p.parent.mkdir(parents=True, exist_ok=True)
                out_p.write_text(html_content, encoding="utf-8")

            artifacts = [output_path] if output_path else []
            return ToolResult(
                success=True,
                data={
                    "mode": mode,
                    "theme_id": canonical_theme,
                    "component_type": component_type,
                    "output_format": output_format,
                    "dom_snippet": html_content,
                    "output_path": output_path,
                    "width": width,
                    "height": height,
                    "metadata": {
                        "theme": canonical_theme,
                        "token_count": len(tokens_dict),
                        "generator": "open_design_tool",
                    },
                },
                artifacts=artifacts,
                duration_seconds=round(time.time() - start_time, 3),
            )

        elif output_format in ("png_still", "webm_alpha"):
            chrome_bin = _find_chrome_executable()
            if not chrome_bin:
                return ToolResult(
                    success=False,
                    error=(
                        f"Headless Chrome/Chromium not found for {output_format} rendering. "
                        "Install Google Chrome or set CHROME_BIN environment variable."
                    ),
                )

            # Create temporary HTML file
            with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
                f.write(html_content)
                temp_html_path = f.name

            try:
                # Target PNG file
                if output_format == "png_still" and output_path:
                    final_png = output_path
                else:
                    final_png = tempfile.mktemp(suffix=".png")

                Path(final_png).parent.mkdir(parents=True, exist_ok=True)

                # Capture transparent screenshot via Chrome headless
                chrome_cmd = [
                    chrome_bin,
                    "--headless=new",
                    f"--screenshot={final_png}",
                    f"--window-size={width},{height}",
                    "--default-background-color=00000000",
                    "--hide-scrollbars",
                    temp_html_path,
                ]
                proc = subprocess.run(chrome_cmd, capture_output=True, text=True, timeout=30)
                if proc.returncode != 0 or not os.path.exists(final_png) or os.path.getsize(final_png) == 0:
                    return ToolResult(
                        success=False,
                        error=f"Chrome headless failed to capture PNG: {proc.stderr or proc.stdout}",
                    )

                if output_format == "png_still":
                    return ToolResult(
                        success=True,
                        data={
                            "mode": mode,
                            "theme_id": canonical_theme,
                            "component_type": component_type,
                            "output_format": output_format,
                            "output_path": final_png,
                            "width": width,
                            "height": height,
                            "file_size_bytes": os.path.getsize(final_png),
                            "metadata": {"theme": canonical_theme, "generator": "open_design_tool"},
                        },
                        artifacts=[final_png],
                        duration_seconds=round(time.time() - start_time, 3),
                    )

                # webm_alpha export using FFmpeg with VP9 yuva420p
                ffmpeg_bin = shutil.which("ffmpeg")
                if not ffmpeg_bin:
                    return ToolResult(
                        success=False,
                        error="FFmpeg binary not found in PATH for webm_alpha rendering.",
                    )

                final_webm = output_path or tempfile.mktemp(suffix=".webm")
                Path(final_webm).parent.mkdir(parents=True, exist_ok=True)

                ffmpeg_cmd = [
                    ffmpeg_bin,
                    "-y",
                    "-loop",
                    "1",
                    "-t",
                    str(duration_seconds),
                    "-i",
                    final_png,
                    "-c:v",
                    "libvpx-vp9",
                    "-pix_fmt",
                    "yuva420p",
                    "-b:v",
                    "2M",
                    "-auto-alt-ref",
                    "0",
                    final_webm,
                ]
                ff_proc = subprocess.run(ffmpeg_cmd, capture_output=True, text=True, timeout=60)
                if ff_proc.returncode != 0 or not os.path.exists(final_webm) or os.path.getsize(final_webm) == 0:
                    return ToolResult(
                        success=False,
                        error=f"FFmpeg transparent WebM creation failed: {ff_proc.stderr}",
                    )

                return ToolResult(
                    success=True,
                    data={
                        "mode": mode,
                        "theme_id": canonical_theme,
                        "component_type": component_type,
                        "output_format": output_format,
                        "output_path": final_webm,
                        "width": width,
                        "height": height,
                        "duration_seconds": duration_seconds,
                        "file_size_bytes": os.path.getsize(final_webm),
                        "metadata": {"theme": canonical_theme, "codec": "vp9_yuva420p"},
                    },
                    artifacts=[final_webm],
                    duration_seconds=round(time.time() - start_time, 3),
                )

            finally:
                if os.path.exists(temp_html_path):
                    os.unlink(temp_html_path)
                if output_format == "webm_alpha" and os.path.exists(final_png) and final_png != output_path:
                    os.unlink(final_png)

        return ToolResult(success=False, error=f"Unsupported output_format: {output_format}")


# Provide class alias for PascalCase convention
OpenDesignTool = OpenDesign
