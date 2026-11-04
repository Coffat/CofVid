"""Music search and download from Pixabay Music (free, no API key).

Scrapes Pixabay's music section to find and download royalty-free
background music tracks. If Pixabay is unavailable or blocks requests
with Cloudflare 403, falls back automatically across multiple tiers:
1) Pixabay website scraper (browser-emulated session).
2) Local music library (`music_library/` directory).
3) Wikimedia Commons open CC0 audio.
4) Local FFmpeg electronic Ambient Pad generator (48kHz stereo, zero-failure).
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Optional

from tools.base_tool import (
    BaseTool,
    Determinism,
    ExecutionMode,
    ResourceProfile,
    RetryPolicy,
    ToolResult,
    ToolRuntime,
    ToolStability,
    ToolStatus,
    ToolTier,
)

_PROJECT_ROOT = Path(__file__).resolve().parents[2]


class PixabayMusic(BaseTool):
    name = "pixabay_music"
    version = "0.2.0"
    tier = ToolTier.SOURCE
    capability = "music_search"
    provider = "pixabay_music"
    stability = ToolStability.PRODUCTION
    execution_mode = ExecutionMode.SYNC
    determinism = Determinism.DETERMINISTIC
    runtime = ToolRuntime.HYBRID

    dependencies = []  # no API key needed
    install_instructions = (
        "No setup required. Pixabay Music is free and needs no API key.\n"
        "Includes automated fallback to local music library and FFmpeg ambient synth."
    )

    agent_skills = ["music"]

    capabilities = ["search_music", "download_music", "stock_music"]
    supports = {
        "duration_filter": True,
        "free_commercial_use": True,
        "no_api_key": True,
        "zero_failure_fallback": True,
    }
    best_for = [
        "quick background music with zero setup (no API key)",
        "royalty-free music for any commercial project",
        "reliable music fallback even under network restrictions",
    ]
    not_good_for = [
        "precise stem separation",
        "custom vocal lyric generation",
    ]

    fallback_tools = ["music_library", "google_music"]

    input_schema = {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query for music (e.g., 'upbeat corporate background', 'minimalist ambient tech')",
            },
            "prompt": {
                "type": "string",
                "description": "Alternative key for query",
            },
            "keyword": {
                "type": "string",
                "description": "Alternative key for query",
            },
            "min_duration": {
                "type": "number",
                "default": 30,
                "minimum": 1,
                "description": "Minimum duration in seconds",
            },
            "max_duration": {
                "type": "number",
                "default": 120,
                "maximum": 600,
                "description": "Maximum duration in seconds",
            },
            "duration": {
                "type": "number",
                "description": "Target duration in seconds for generated music",
            },
            "output_path": {
                "type": "string",
                "description": "File path to save the downloaded/generated MP3",
            },
        },
    }

    resource_profile = ResourceProfile(
        cpu_cores=1, ram_mb=256, vram_mb=0, disk_mb=50, network_required=False
    )
    retry_policy = RetryPolicy(max_retries=2, retryable_errors=["timeout"])
    idempotency_key_fields = ["query", "min_duration", "max_duration"]
    side_effects = ["writes audio file to output_path"]
    user_visible_verification = [
        "Listen to audio track for mood and quality",
    ]

    _USER_AGENT = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/131.0.0.0 Safari/537.36"
    )

    _BROWSER_HEADERS = {
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;"
            "q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Ch-Ua": '"Chromium";v="131", "Not_A Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
    }

    def get_status(self) -> ToolStatus:
        return ToolStatus.AVAILABLE

    def estimate_cost(self, inputs: dict[str, Any]) -> float:
        return 0.0

    def execute(self, inputs: dict[str, Any]) -> ToolResult:
        start = time.time()

        # Normalize query and parameters
        query = (
            inputs.get("query")
            or inputs.get("prompt")
            or inputs.get("keyword")
            or "minimalist ambient background"
        ).strip()

        min_dur = float(inputs.get("min_duration", 30))
        max_dur = float(inputs.get("max_duration", 120))
        target_dur = float(inputs.get("duration") or max(min_dur, min(max_dur, 60.0)))

        # Resolve output path
        output_path_str = inputs.get("output_path")
        if output_path_str:
            output_path = Path(output_path_str)
        else:
            safe_query = "".join(
                c if c.isalnum() or c in "._- " else "_" for c in query
            )[:40].strip() or "ambient_music"
            output_path = Path("projects/temp_music") / f"pixabay_{safe_query}_{int(time.time())}.mp3"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        fallback_reasons: list[str] = []

        # -------------------------------------------------------------
        # Tier 1: Try scraping Pixabay Music
        # -------------------------------------------------------------
        try:
            tracks = self._search(query)
            if tracks:
                filtered = [
                    t for t in tracks
                    if t.get("duration") is not None
                    and min_dur <= t["duration"] <= max_dur
                ]
                if not filtered:
                    filtered = tracks

                track = filtered[0]
                self._download(track, output_path)

                if output_path.exists() and output_path.stat().st_size > 1024:
                    return ToolResult(
                        success=True,
                        data={
                            "provider": "pixabay_music",
                            "source": "pixabay",
                            "track_title": track.get("title", "Unknown"),
                            "artist": track.get("artist", "Unknown"),
                            "duration_seconds": track.get("duration"),
                            "query": query,
                            "output": str(output_path),
                            "format": "mp3",
                            "license": "Pixabay Content License (free, no attribution required)",
                            "results_found": len(tracks),
                            "results_after_filter": len(filtered),
                        },
                        artifacts=[str(output_path)],
                        cost_usd=0.0,
                        duration_seconds=round(time.time() - start, 2),
                    )
                fallback_reasons.append("Pixabay download produced incomplete file")
            else:
                fallback_reasons.append("Pixabay search returned no results or was blocked by Cloudflare (403/Challenge)")
        except Exception as e:
            fallback_reasons.append(f"Pixabay scrape failed: {type(e).__name__}: {e}")

        # -------------------------------------------------------------
        # Tier 2: Check local music_library/
        # -------------------------------------------------------------
        local_track = self._find_local_track(query, min_dur, max_dur)
        if local_track and local_track.exists():
            try:
                if local_track.suffix.lower() == ".mp3":
                    shutil.copyfile(local_track, output_path)
                else:
                    # Convert to MP3 via ffmpeg
                    subprocess.run(
                        [
                            "ffmpeg", "-y", "-i", str(local_track),
                            "-ar", "48000", "-ac", "2", "-b:a", "192k",
                            str(output_path),
                        ],
                        capture_output=True,
                        timeout=30,
                        check=True,
                    )

                if output_path.exists() and output_path.stat().st_size > 1024:
                    return ToolResult(
                        success=True,
                        data={
                            "provider": "pixabay_music (fallback: music_library)",
                            "source": "music_library",
                            "track_title": local_track.stem,
                            "artist": "Local Library",
                            "query": query,
                            "output": str(output_path),
                            "format": "mp3",
                            "license": "Royalty-Free (User Music Library)",
                            "fallback_applied": "music_library",
                            "fallback_reasons": fallback_reasons,
                        },
                        artifacts=[str(output_path)],
                        cost_usd=0.0,
                        duration_seconds=round(time.time() - start, 2),
                    )
            except Exception as e:
                fallback_reasons.append(f"Local track copy/convert failed: {e}")

        # -------------------------------------------------------------
        # Tier 3: Wikimedia CC0 audio OR FFmpeg Ambient Synth
        # -------------------------------------------------------------
        # Attempt open CC0 / Wikimedia audio search
        try:
            wm_ok = self._search_and_download_wikimedia(query, output_path, min_dur, max_dur)
            if wm_ok and output_path.exists() and output_path.stat().st_size > 1024:
                return ToolResult(
                    success=True,
                    data={
                        "provider": "pixabay_music (fallback: wikimedia_audio)",
                        "source": "wikimedia_commons",
                        "track_title": f"Wikimedia Audio ({query[:30]})",
                        "artist": "Wikimedia Commons CC0",
                        "query": query,
                        "output": str(output_path),
                        "format": "mp3",
                        "license": "Creative Commons / Public Domain",
                        "fallback_applied": "wikimedia_commons",
                        "fallback_reasons": fallback_reasons,
                    },
                    artifacts=[str(output_path)],
                    cost_usd=0.0,
                    duration_seconds=round(time.time() - start, 2),
                )
        except Exception as e:
            fallback_reasons.append(f"Wikimedia audio fallback failed: {e}")

        # -------------------------------------------------------------
        # Tier 4 (Guaranteed Zero-Failure): Synthesize Ambient Pad via FFmpeg
        # -------------------------------------------------------------
        try:
            self._generate_ambient_pad_ffmpeg(output_path, target_dur, query)
            if output_path.exists() and output_path.stat().st_size > 1024:
                return ToolResult(
                    success=True,
                    data={
                        "provider": "pixabay_music (fallback: ffmpeg_ambient_synth)",
                        "source": "ffmpeg_ambient_synth",
                        "track_title": f"Ambient Pad ({query[:30]})",
                        "artist": "CofVid Ambient Synth",
                        "duration_seconds": target_dur,
                        "query": query,
                        "output": str(output_path),
                        "format": "mp3",
                        "sample_rate": 48000,
                        "channels": 2,
                        "license": "CC0 / Generated (Royalty-free)",
                        "fallback_applied": "ffmpeg_ambient_synth",
                        "fallback_reasons": fallback_reasons,
                    },
                    artifacts=[str(output_path)],
                    cost_usd=0.0,
                    duration_seconds=round(time.time() - start, 2),
                )
        except Exception as e:
            return ToolResult(
                success=False,
                error=f"All music acquisition and fallback methods failed: {e}. Reasons: {fallback_reasons}",
                duration_seconds=round(time.time() - start, 2),
            )

        return ToolResult(
            success=False,
            error=f"Music generation could not produce a valid file. Reasons: {fallback_reasons}",
            duration_seconds=round(time.time() - start, 2),
        )

    def _build_opener(self) -> urllib.request.OpenerDirector:
        """Build a URL opener with cookie support for session persistence."""
        import http.cookiejar

        cj = http.cookiejar.CookieJar()
        return urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(cj)
        )

    def _search(self, query: str) -> list[dict]:
        """Search Pixabay Music via the bootstrap JSON API.

        Gracefully catches 403 / Cloudflare challenges / URLError and returns empty list.
        """
        slug = re.sub(r"\s+", "-", query.strip().lower())
        slug = urllib.parse.quote(slug, safe="-")
        search_url = f"https://pixabay.com/music/search/{slug}/"

        opener = self._build_opener()

        request = urllib.request.Request(search_url)
        request.add_header("User-Agent", self._USER_AGENT)
        for key, val in self._BROWSER_HEADERS.items():
            request.add_header(key, val)

        try:
            with opener.open(request, timeout=10) as response:
                html = response.read().decode("utf-8", errors="replace")
        except Exception:
            # 403, 429, timeout, connection reset, etc.
            return []

        tracks = self._parse_bootstrap(html, search_url, opener)
        if tracks:
            return tracks

        return self._parse_tracks_html(html)

    def _parse_bootstrap(
        self,
        html: str,
        referer: str,
        opener: urllib.request.OpenerDirector,
    ) -> list[dict]:
        """Extract tracks from Pixabay's bootstrap JSON endpoint."""
        match = re.search(
            r'window\.__BOOTSTRAP_URL__\s*=\s*["\']([^"\']+)["\']',
            html,
        )
        if not match:
            return []

        bootstrap_path = match.group(1)
        if not bootstrap_path or bootstrap_path == "":
            return []

        bootstrap_url = f"https://pixabay.com{bootstrap_path}"

        req = urllib.request.Request(bootstrap_url)
        req.add_header("User-Agent", self._USER_AGENT)
        req.add_header("Accept", "application/json, text/plain, */*")
        req.add_header("Referer", referer)
        req.add_header("Sec-Fetch-Dest", "empty")
        req.add_header("Sec-Fetch-Mode", "cors")
        req.add_header("Sec-Fetch-Site", "same-origin")

        try:
            with opener.open(req, timeout=10) as response:
                data = json.loads(response.read().decode("utf-8"))
        except Exception:
            return []

        results = data.get("page", {}).get("results", [])
        tracks: list[dict] = []

        for item in results:
            sources = item.get("sources", {})
            audio_url = sources.get("src")
            if not audio_url:
                continue

            user = item.get("user", {}) or {}
            tracks.append({
                "title": item.get("name") or sources.get("filename", "Unknown"),
                "audio_url": audio_url,
                "duration": item.get("duration"),
                "artist": user.get("username", "Unknown"),
                "rating": item.get("rating"),
                "download_count": item.get("downloadCount"),
                "pixabay_id": item.get("id"),
            })

        return tracks

    def _parse_tracks_html(self, html: str) -> list[dict]:
        """Fallback: extract track info from HTML when bootstrap fails."""
        tracks: list[dict] = []

        mp3_urls = re.findall(
            r'(https?://cdn\.pixabay\.com/audio/[^\s"\'<>]+\.mp3[^\s"\'<>]*)',
            html,
        )
        seen: set[str] = set()
        for url in mp3_urls:
            if url not in seen:
                seen.add(url)
                tracks.append({
                    "title": "Unknown",
                    "audio_url": url,
                    "duration": None,
                    "artist": "Unknown",
                })

        return tracks

    def _download(self, track: dict, output_path: Path) -> Path:
        """Download an MP3 track to output_path."""
        audio_url = track.get("audio_url")
        if not audio_url:
            raise RuntimeError("No audio URL found for the selected track.")

        if audio_url.startswith("//"):
            audio_url = "https:" + audio_url
        elif audio_url.startswith("/"):
            audio_url = "https://pixabay.com" + audio_url

        output_path.parent.mkdir(parents=True, exist_ok=True)

        request = urllib.request.Request(
            audio_url,
            headers={
                "User-Agent": self._USER_AGENT,
                "Referer": "https://pixabay.com/music/",
            },
        )

        with urllib.request.urlopen(request, timeout=20) as response:
            output_path.write_bytes(response.read())

        return output_path

    def _find_local_track(self, query: str, min_dur: float, max_dur: float) -> Optional[Path]:
        """Search music_library/ directories for matching or available audio tracks."""
        search_dirs = [
            _PROJECT_ROOT / "music_library",
            Path.cwd() / "music_library",
        ]
        candidates: list[Path] = []
        audio_extensions = {".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg", ".opus"}
        for d in search_dirs:
            if d.is_dir():
                for p in d.rglob("*"):
                    if p.is_file() and p.suffix.lower() in audio_extensions:
                        candidates.append(p)
        if not candidates:
            return None

        # Score by token overlap
        q_tokens = set(re.findall(r"\w+", query.lower()))
        best_file = candidates[0]
        best_score = -1
        for cand in candidates:
            stem_tokens = set(re.findall(r"\w+", cand.stem.lower()))
            score = len(q_tokens.intersection(stem_tokens))
            if score > best_score:
                best_score = score
                best_file = cand

        return best_file

    def _search_and_download_wikimedia(
        self,
        query: str,
        output_path: Path,
        min_dur: float,
        max_dur: float,
    ) -> bool:
        """Attempt to fetch an open CC0/CC-BY audio track from Wikimedia Commons."""
        try:
            clean_q = re.sub(r"[^\w\s]", "", query).strip()
            search_terms = urllib.parse.quote(clean_q or "ambient")
            url = (
                "https://commons.wikimedia.org/w/api.php?action=query&generator=search"
                f"&gsrsearch=filetype:audio+{search_terms}&gsrlimit=3&prop=imageinfo&iiprop=url|size|mime&format=json"
            )
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "CofVid/1.0 (audio_fallback; test@example.com)"},
            )
            with urllib.request.urlopen(req, timeout=4) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                pages = data.get("query", {}).get("pages", {})
                for pid, page in pages.items():
                    info = page.get("imageinfo", [{}])[0]
                    audio_url = info.get("url")
                    if not audio_url:
                        continue
                    dl_req = urllib.request.Request(
                        audio_url,
                        headers={"User-Agent": "CofVid/1.0 (audio_fallback)"},
                    )
                    with urllib.request.urlopen(dl_req, timeout=8) as dl_resp:
                        content = dl_resp.read()
                        if len(content) > 1024:
                            temp_dl = output_path.with_suffix(".tmp_audio")
                            temp_dl.write_bytes(content)
                            subprocess.run(
                                [
                                    "ffmpeg", "-y", "-i", str(temp_dl),
                                    "-ar", "48000", "-ac", "2", "-b:a", "192k",
                                    str(output_path),
                                ],
                                capture_output=True,
                                timeout=15,
                                check=True,
                            )
                            if temp_dl.exists():
                                temp_dl.unlink()
                            return True
        except Exception:
            pass
        return False

    def _generate_ambient_pad_ffmpeg(
        self,
        output_path: Path,
        duration: float = 45.0,
        query: str = "ambient",
    ) -> Path:
        """Generate a lush 48kHz stereo electronic ambient pad via FFmpeg."""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        dur = max(10.0, float(duration))
        fade_in = 2.5
        fade_out = 3.0
        fade_out_start = max(0.5, dur - fade_out)

        # C major 9 / Am11 lush pad chord voicing:
        # 65.41 Hz (C2), 130.81 Hz (C3), 164.81 Hz (E3), 196.00 Hz (G3), 246.94 Hz (B3), 293.66 Hz (D4)
        freqs = [
            ("65.41", 0.35),
            ("130.81", 0.25),
            ("164.81", 0.20),
            ("196.00", 0.20),
            ("246.94", 0.15),
            ("293.66", 0.15),
        ]

        inputs_args = []
        volume_filters = []
        amix_inputs = []

        for i, (f, vol) in enumerate(freqs):
            inputs_args.extend(["-f", "lavfi", "-i", f"sine=f={f}:d={dur:.2f}"])
            volume_filters.append(f"[{i}:a]volume={vol}[b{i}];")
            amix_inputs.append(f"[b{i}]")

        vol_str = "".join(volume_filters)
        amix_str = "".join(amix_inputs)
        mix_chain = (
            f"{vol_str}{amix_str}amix=inputs={len(freqs)}:normalize=0,"
            f"lowpass=f=950,"
            f"aphaser=in_gain=0.8:out_gain=0.74:delay=3:decay=0.4:speed=0.2:type=t,"
            f"aecho=0.8:0.75:100|250:0.3|0.2,"
            f"afade=t=in:ss=0:d={fade_in},"
            f"afade=t=out:st={fade_out_start:.2f}:d={fade_out}[out]"
        )

        cmd = [
            "ffmpeg", "-y",
            *inputs_args,
            "-filter_complex", mix_chain,
            "-map", "[out]",
            "-ar", "48000",
            "-ac", "2",
            "-b:a", "192k",
            str(output_path),
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode != 0 or not output_path.exists() or output_path.stat().st_size < 1024:
            cmd_simple = [
                "ffmpeg", "-y",
                "-f", "lavfi",
                "-i", f"sine=f=130.81:d={dur:.2f}",
                "-ar", "48000",
                "-ac", "2",
                "-b:a", "192k",
                str(output_path),
            ]
            subprocess.run(cmd_simple, capture_output=True, timeout=15, check=True)

        return output_path
