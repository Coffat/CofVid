"""Official UI Icon Resolver Tool for CofVid.

Dedicated solely to UI icons based on the Lucide/Feather spec:
viewBox="0 0 24 24", stroke-width=2, round linecap/join.

Guarantees genuine vector geometry without generative diffusion hallucinations.
"""

from __future__ import annotations

import logging
import os
import re
import shutil
import subprocess
import tempfile
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
    ToolTier,
)

logger = logging.getLogger(__name__)

# Standard Lucide / Feather UI Icons (viewBox 0 0 24 24)
BUILTIN_UI_ICONS: dict[str, dict[str, Any]] = {
    "star": {
        "viewBox": "0 0 24 24",
        "title": "Star",
        "body": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    },
    "terminal": {
        "viewBox": "0 0 24 24",
        "title": "Terminal",
        "body": '<polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/>',
    },
    "code": {
        "viewBox": "0 0 24 24",
        "title": "Code",
        "body": '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    },
    "shield": {
        "viewBox": "0 0 24 24",
        "title": "Shield",
        "body": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    },
    "database": {
        "viewBox": "0 0 24 24",
        "title": "Database",
        "body": (
            '<ellipse cx="12" cy="5" rx="9" ry="3"/>'
            '<path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/>'
            '<path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/>'
        ),
    },
    "check": {
        "viewBox": "0 0 24 24",
        "title": "Check",
        "body": '<polyline points="20 6 9 17 4 12"/>',
    },
    "alert-circle": {
        "viewBox": "0 0 24 24",
        "title": "Alert Circle",
        "body": (
            '<circle cx="12" cy="12" r="10"/>'
            '<line x1="12" y1="8" x2="12" y2="12"/>'
            '<line x1="12" y1="16" x2="12.01" y2="16"/>'
        ),
    },
    "info": {
        "viewBox": "0 0 24 24",
        "title": "Info",
        "body": (
            '<circle cx="12" cy="12" r="10"/>'
            '<line x1="12" y1="16" x2="12" y2="12"/>'
            '<line x1="12" y1="8" x2="12.01" y2="8"/>'
        ),
    },
    "heart": {
        "viewBox": "0 0 24 24",
        "title": "Heart",
        "body": '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>',
    },
    "copy": {
        "viewBox": "0 0 24 24",
        "title": "Copy",
        "body": (
            '<rect x="9" y="9" width="13" height="13" rx="2" ry="2"/>'
            '<path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>'
        ),
    },
    "globe": {
        "viewBox": "0 0 24 24",
        "title": "Globe",
        "body": (
            '<circle cx="12" cy="12" r="10"/>'
            '<line x1="2" y1="12" x2="22" y2="12"/>'
            '<path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>'
        ),
    },
    "cpu": {
        "viewBox": "0 0 24 24",
        "title": "CPU",
        "body": (
            '<rect x="4" y="4" width="16" height="16" rx="2"/>'
            '<rect x="9" y="9" width="6" height="6"/>'
            '<line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/>'
            '<line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/>'
            '<line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/>'
            '<line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/>'
        ),
    },
    "server": {
        "viewBox": "0 0 24 24",
        "title": "Server",
        "body": (
            '<rect x="2" y="2" width="20" height="8" rx="2" ry="2"/>'
            '<rect x="2" y="14" width="20" height="8" rx="2" ry="2"/>'
            '<line x1="6" y1="6" x2="6.01" y2="6"/>'
            '<line x1="6" y1="18" x2="6.01" y2="18"/>'
        ),
    },
    "external-link": {
        "viewBox": "0 0 24 24",
        "title": "External Link",
        "body": (
            '<path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>'
            '<polyline points="15 3 21 3 21 9"/>'
            '<line x1="10" y1="14" x2="21" y2="3"/>'
        ),
    },
    "zap": {
        "viewBox": "0 0 24 24",
        "title": "Zap",
        "body": '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
    },
    "layers": {
        "viewBox": "0 0 24 24",
        "title": "Layers",
        "body": (
            '<polygon points="12 2 2 7 12 12 22 7 12 2"/>'
            '<polyline points="2 17 12 22 22 17"/>'
            '<polyline points="2 12 12 17 22 12"/>'
        ),
    },
    "git-branch": {
        "viewBox": "0 0 24 24",
        "title": "Git Branch",
        "body": (
            '<line x1="6" y1="3" x2="6" y2="15"/>'
            '<circle cx="18" cy="6" r="3"/>'
            '<circle cx="6" cy="18" r="3"/>'
            '<path d="M18 9a9 9 0 0 1-9 9"/>'
        ),
    },
    "arrow-right": {
        "viewBox": "0 0 24 24",
        "title": "Arrow Right",
        "body": '<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>',
    },
    "arrow-left": {
        "viewBox": "0 0 24 24",
        "title": "Arrow Left",
        "body": '<line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/>',
    },
    "search": {
        "viewBox": "0 0 24 24",
        "title": "Search",
        "body": '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>',
    },
    "settings": {
        "viewBox": "0 0 24 24",
        "title": "Settings",
        "body": (
            '<circle cx="12" cy="12" r="3"/>'
            '<path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/>'
        ),
    },
    "play": {
        "viewBox": "0 0 24 24",
        "title": "Play",
        "body": '<polygon points="5 3 19 12 5 21 5 3"/>',
    },
    "pause": {
        "viewBox": "0 0 24 24",
        "title": "Pause",
        "body": '<rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/>',
    },
    "clock": {
        "viewBox": "0 0 24 24",
        "title": "Clock",
        "body": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    },
    "calendar": {
        "viewBox": "0 0 24 24",
        "title": "Calendar",
        "body": (
            '<rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>'
            '<line x1="16" y1="2" x2="16" y2="6"/>'
            '<line x1="8" y1="2" x2="8" y2="6"/>'
            '<line x1="3" y1="10" x2="21" y2="10"/>'
        ),
    },
    "lock": {
        "viewBox": "0 0 24 24",
        "title": "Lock",
        "body": (
            '<rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>'
            '<path d="M7 11V7a5 5 0 0 1 10 0v4"/>'
        ),
    },
    "unlock": {
        "viewBox": "0 0 24 24",
        "title": "Unlock",
        "body": (
            '<rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>'
            '<path d="M7 11V7a5 5 0 0 1 9.9-1"/>'
        ),
    },
    "eye": {
        "viewBox": "0 0 24 24",
        "title": "Eye",
        "body": '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>',
    },
    "eye-off": {
        "viewBox": "0 0 24 24",
        "title": "Eye Off",
        "body": (
            '<path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/>'
            '<line x1="1" y1="1" x2="23" y2="23"/>'
        ),
    },
    "download": {
        "viewBox": "0 0 24 24",
        "title": "Download",
        "body": (
            '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>'
            '<polyline points="7 10 12 15 17 10"/>'
            '<line x1="12" y1="15" x2="12" y2="3"/>'
        ),
    },
    "upload": {
        "viewBox": "0 0 24 24",
        "title": "Upload",
        "body": (
            '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>'
            '<polyline points="17 8 12 3 7 8"/>'
            '<line x1="12" y1="3" x2="12" y2="15"/>'
        ),
    },
}


def normalize_icon_name(name: str) -> str:
    """Normalize UI icon name to a clean lookup slug."""
    s = name.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    aliases = {
        "alert": "alert-circle",
        "warning": "alert-circle",
        "information": "info",
        "link": "external-link",
        "branch": "git-branch",
        "right": "arrow-right",
        "left": "arrow-left",
        "time": "clock",
        "gear": "settings",
        "cog": "settings",
    }
    return aliases.get(s, s)


class UIIconTool(BaseTool):
    """Dedicated Lucide/Feather UI Icon Resolver for CofVid.

    Resolves pixel-perfect standard UI icons (viewBox 0 0 24 24, stroke-width 2, round linecap/join).
    Supports outline and filled variants, custom stroke widths, colors, and direct file/PNG export.
    """

    name = "ui_icon_tool"
    version = "0.1.0"
    tier = ToolTier.CORE
    stability = ToolStability.PRODUCTION
    execution_mode = ExecutionMode.SYNC
    determinism = Determinism.DETERMINISTIC
    runtime = ToolRuntime.LOCAL

    capability = "graphics"
    provider = "ui_icon_resolver"
    capabilities = [
        "ui_icon",
        "svg_icon",
        "lucide_icon",
    ]
    agent_skills = ["brand-icon", "open-design"]

    resource_profile = ResourceProfile(cpu_cores=1, ram_mb=256, disk_mb=50)

    input_schema = {
        "type": "object",
        "properties": {
            "icon_name": {
                "type": "string",
                "description": "Name of UI icon (e.g. 'star', 'terminal', 'code', 'shield', 'database', 'check', etc.)",
            },
            "variant": {
                "type": "string",
                "enum": ["outline", "filled"],
                "default": "outline",
                "description": "Rendering style: 'outline' (fill=none, stroke=color) or 'filled' (fill=color, stroke=color)",
            },
            "color": {
                "type": "string",
                "default": "currentColor",
                "description": "Stroke / fill color in CSS format (e.g. 'currentColor', '#00F0FF', '#ffffff', '#FFD700')",
            },
            "stroke_width": {
                "type": "number",
                "default": 2,
                "description": "Stroke width (standard is 2 for Lucide spec)",
            },
            "width": {
                "type": "integer",
                "default": 24,
                "description": "Width attribute for rendered SVG / PNG in pixels",
            },
            "height": {
                "type": "integer",
                "default": 24,
                "description": "Height attribute for rendered SVG / PNG in pixels",
            },
            "output_format": {
                "type": "string",
                "enum": ["svg_snippet", "svg_file", "png_file"],
                "default": "svg_snippet",
                "description": "Output format: 'svg_snippet', 'svg_file', or 'png_file'",
            },
            "output_path": {
                "type": "string",
                "description": "Optional destination path when saving to svg_file or png_file",
            },
        },
        "required": ["icon_name"],
    }

    output_schema = {
        "type": "object",
        "properties": {
            "icon_name": {"type": "string"},
            "slug": {"type": "string"},
            "variant": {"type": "string"},
            "color": {"type": "string"},
            "stroke_width": {"type": "number"},
            "svg": {"type": "string"},
            "output_path": {"type": "string"},
            "format": {"type": "string"},
            "width": {"type": "integer"},
            "height": {"type": "integer"},
        },
        "required": ["icon_name", "slug", "svg"],
    }

    def _render_svg_to_png(self, svg_content: str, out_png_path: str, width: int, height: int) -> bool:
        """Render SVG string to PNG file using rsvg-convert or headless Chrome."""
        out_p = Path(out_png_path)
        out_p.parent.mkdir(parents=True, exist_ok=True)

        with tempfile.NamedTemporaryFile("w", suffix=".svg", delete=False) as f:
            f.write(svg_content)
            temp_svg = f.name

        try:
            # 1. Try rsvg-convert
            if shutil.which("rsvg-convert"):
                cmd = ["rsvg-convert", "-w", str(width), "-h", str(height), temp_svg, "-o", out_png_path]
                proc = subprocess.run(cmd, capture_output=True, timeout=10)
                if proc.returncode == 0 and os.path.exists(out_png_path) and os.path.getsize(out_png_path) > 0:
                    return True

            # 2. Try headless Chrome
            chrome_candidates = [
                os.environ.get("CHROME_BIN"),
                shutil.which("google-chrome"),
                shutil.which("chrome"),
                shutil.which("chromium"),
                "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                "/usr/bin/google-chrome",
            ]
            chrome_bin = next((c for c in chrome_candidates if c and os.path.isfile(c) and os.access(c, os.X_OK)), None)
            if chrome_bin:
                with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as hf:
                    html_wrap = f"""<!DOCTYPE html><html><body style="margin:0;padding:0;background:transparent;display:flex;align-items:center;justify-content:center;width:{width}px;height:{height}px;">{svg_content}</body></html>"""
                    hf.write(html_wrap)
                    temp_html = hf.name

                try:
                    c_cmd = [
                        chrome_bin,
                        "--headless=new",
                        f"--screenshot={out_png_path}",
                        f"--window-size={width},{height}",
                        "--default-background-color=00000000",
                        "--hide-scrollbars",
                        temp_html,
                    ]
                    c_proc = subprocess.run(c_cmd, capture_output=True, timeout=15)
                    if c_proc.returncode == 0 and os.path.exists(out_png_path) and os.path.getsize(out_png_path) > 0:
                        return True
                finally:
                    if os.path.exists(temp_html):
                        os.unlink(temp_html)
        finally:
            if os.path.exists(temp_svg):
                os.unlink(temp_svg)

        return False

    def execute(self, inputs: dict[str, Any]) -> ToolResult:
        icon_raw = inputs.get("icon_name", "")
        if not icon_raw:
            return ToolResult(success=False, error="icon_name is required")

        slug = normalize_icon_name(icon_raw)
        variant = inputs.get("variant", "outline")
        color = inputs.get("color", "currentColor")
        stroke_width = inputs.get("stroke_width", 2)
        width = int(inputs.get("width", 24))
        height = int(inputs.get("height", 24))
        output_format = inputs.get("output_format", "svg_snippet")
        output_path = inputs.get("output_path")

        if slug not in BUILTIN_UI_ICONS:
            return ToolResult(
                success=False,
                error=f"UI icon '{icon_raw}' (slug: '{slug}') not found in built-in UI icon library. Available icons: {', '.join(sorted(BUILTIN_UI_ICONS.keys()))}",
            )

        meta = BUILTIN_UI_ICONS[slug]
        view_box = meta.get("viewBox", "0 0 24 24")
        body = meta["body"]

        fill_attr = "none" if variant == "outline" else color
        stroke_attr = color

        raw_svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_box}" width="{width}" height="{height}" '
            f'fill="{fill_attr}" stroke="{stroke_attr}" stroke-width="{stroke_width}" '
            f'stroke-linecap="round" stroke-linejoin="round" class="cofvid-ui-icon icon-{slug}">'
            f"{body}"
            f"</svg>"
        )

        artifacts: list[str] = []
        final_path: Optional[str] = None

        if output_format == "svg_file":
            if not output_path:
                with tempfile.NamedTemporaryFile("w", suffix=f"-{slug}.svg", delete=False) as tmp_f:
                    tmp_f.write(raw_svg)
                    final_path = tmp_f.name
            else:
                out_p = Path(output_path)
                out_p.parent.mkdir(parents=True, exist_ok=True)
                out_p.write_text(raw_svg, encoding="utf-8")
                final_path = str(out_p)
            artifacts.append(final_path)

        elif output_format == "png_file":
            target_png = output_path or tempfile.mktemp(suffix=f"-{slug}.png")
            rendered = self._render_svg_to_png(raw_svg, target_png, width=width, height=height)
            if not rendered:
                return ToolResult(
                    success=False,
                    error=f"Failed to rasterize SVG icon for {icon_raw} to PNG. Ensure rsvg-convert or Chrome is available.",
                )
            final_path = target_png
            artifacts.append(final_path)

        return ToolResult(
            success=True,
            data={
                "icon_name": icon_raw,
                "slug": slug,
                "variant": variant,
                "color": color,
                "stroke_width": stroke_width,
                "width": width,
                "height": height,
                "svg": raw_svg,
                "output_path": final_path,
                "format": output_format,
            },
            artifacts=artifacts,
        )


UIIcon = UIIconTool
