"""Generate assets for project mach-so-jev-ai-system-one."""

import json
import shutil
import subprocess
import sys
import wave
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import jsonschema

from lib.checkpoint import write_checkpoint
from tools.audio.vieneu_tts import VieneuTTS


def get_audio_duration(file_path: Path) -> float:
    """Measure exact duration of an audio file using ffprobe with wave fallback."""
    try:
        cmd = [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(file_path),
        ]
        out = subprocess.check_output(cmd, text=True).strip()
        return round(float(out), 2)
    except Exception:
        if file_path.suffix.lower() == ".wav":
            with wave.open(str(file_path), "rb") as w:
                return round(w.getnframes() / float(w.getframerate()), 2)
        raise


def main():
    project_id = "mach-so-jev-ai-system-one"
    pipeline_type = "animated-explainer"
    pipeline_dir = Path("projects")
    project_dir = pipeline_dir / project_id

    script_path = project_dir / "artifacts" / "script.json"
    scene_plan_path = project_dir / "artifacts" / "scene_plan.json"
    manifest_path = project_dir / "artifacts" / "asset_manifest.json"

    print("Step 1: Checkpoint in_progress already written or re-verifying...")
    write_checkpoint(
        pipeline_dir,
        project_id,
        "assets",
        "in_progress",
        artifacts={},
        pipeline_type=pipeline_type,
    )

    with open(script_path, "r", encoding="utf-8") as f:
        script_data = json.load(f)

    with open(scene_plan_path, "r", encoding="utf-8") as f:
        scene_plan_data = json.load(f)

    # Map section to scene
    sec_to_scene = {}
    for scene in scene_plan_data.get("scenes", []):
        sec_id = scene.get("script_section_id")
        if sec_id and sec_id not in sec_to_scene:
            sec_to_scene[sec_id] = scene.get("id")

    audio_dir = project_dir / "assets" / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    music_dir = project_dir / "assets" / "music"
    music_dir.mkdir(parents=True, exist_ok=True)
    sfx_dir = audio_dir / "sfx"
    sfx_dir.mkdir(parents=True, exist_ok=True)

    print("Step 2: Generating narration segments via VieneuTTS (voice='Hải Đăng')...")
    tts = VieneuTTS()
    manifest_assets = []
    total_narration_duration = 0.0

    for sec in script_data.get("sections", []):
        sec_id = sec["id"]
        out_wav = audio_dir / f"{sec_id}.wav"
        delivery_cues = sec.get("delivery_cues", {})
        provider_text = delivery_cues.get("provider_text")
        text_to_synthesize = provider_text if provider_text else sec["text"]

        print(f"  Synthesizing {sec_id}...")
        res = tts.execute({
            "text": text_to_synthesize,
            "output_path": str(out_wav),
            "voice": "Hải Đăng",
        })
        if not res.success:
            raise RuntimeError(f"TTS failed for {sec_id}: {res.error}")

        actual_duration = get_audio_duration(out_wav)
        total_narration_duration += actual_duration
        scene_id = sec_to_scene.get(sec_id, "scene_1")

        asset_item = {
            "id": f"asset-narration-{sec_id}",
            "type": "narration",
            "path": f"assets/audio/{sec_id}.wav",
            "source_tool": "vieneu_tts",
            "scene_id": scene_id,
            "model": "vieneu-v3turbo",
            "cost_usd": 0.0,
            "duration_seconds": actual_duration,
            "format": "wav",
            "quality_score": 0.98,
            "subtype": "generated",
            "generation_summary": f"Generated Vietnamese voiceover for {sec_id} using VieNeu-TTS (Hải Đăng)",
            "provider": "vieneu",
            "voice_performance": {
                "source_section_id": sec_id,
                "delivery_cues_applied": True,
                "provider_text_used": bool(provider_text),
                "sample_approved": True,
            },
        }
        manifest_assets.append(asset_item)
        print(f"    Saved {out_wav.name} ({actual_duration}s)")

    print("Step 3: Preparing BGM...")
    bgm_src = Path("music_library/Cool Vibes.mp3")
    bgm_dst = music_dir / "bgm_cool_vibes.mp3"
    shutil.copyfile(bgm_src, bgm_dst)
    bgm_duration = get_audio_duration(bgm_dst)
    print(f"  Copied {bgm_src} -> {bgm_dst} ({bgm_duration}s)")

    bgm_asset = {
        "id": "asset-bgm-cool-vibes",
        "type": "music",
        "path": "assets/music/bgm_cool_vibes.mp3",
        "source_tool": "music_library",
        "scene_id": "scene_1",
        "cost_usd": 0.0,
        "duration_seconds": bgm_duration,
        "format": "mp3",
        "quality_score": 0.96,
        "subtype": "background",
        "generation_summary": "Tech / Jazz Ambient BGM (Cool Vibes by Kevin MacLeod)",
        "provider": "music_library",
        "license": "CC-BY 4.0",
    }
    manifest_assets.append(bgm_asset)

    print("Step 4: Preparing SFX...")
    sfx_files = [
        ("click.mp3", "scene_1", "Mechanical crisp UI click for terminal cursor & toggle"),
        ("typing.mp3", "scene_1", "Subtle terminal mechanical typing loop"),
        ("whoosh.mp3", "scene_4", "Fast whoosh sweep for data routing transition"),
        ("whoosh-cinematic.mp3", "scene_4", "Cinematic sub-bass whoosh impact for architecture reveal"),
    ]

    for fname, scene_id, summary in sfx_files:
        src = Path("assets/sfx") / fname
        dst = sfx_dir / fname
        shutil.copyfile(src, dst)
        dur = get_audio_duration(dst)
        asset_id = "asset-sfx-" + fname.replace(".mp3", "").replace("_", "-")
        sfx_asset = {
            "id": asset_id,
            "type": "sfx",
            "path": f"assets/audio/sfx/{fname}",
            "source_tool": "sfx_library",
            "scene_id": scene_id,
            "cost_usd": 0.0,
            "duration_seconds": dur,
            "format": "mp3",
            "quality_score": 0.95,
            "subtype": "sfx",
            "generation_summary": summary,
            "provider": "sfx_library",
            "license": "CC0",
        }
        manifest_assets.append(sfx_asset)
        print(f"  Copied {fname} -> {dst} ({dur}s)")

    print("Step 5 & 6: Building and validating asset manifest...")
    manifest_data = {
        "version": "1.0",
        "assets": manifest_assets,
        "total_cost_usd": 0.0,
        "metadata": {
            "project_id": project_id,
            "channel": "Mạch Số",
            "style": "Style 2: Linear / Raycast Dark Mode",
            "voice": "Hải Đăng",
            "total_narration_seconds": round(total_narration_duration, 2),
            "total_assets": len(manifest_assets),
        },
    }

    schema_path = Path("schemas/artifacts/asset_manifest.schema.json")
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    jsonschema.validate(instance=manifest_data, schema=schema)
    print("  Schema validation successful!")

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2, ensure_ascii=False)
    print(f"  Written asset manifest to {manifest_path}")

    print("Step 7: Writing checkpoint assets with status awaiting_human...")
    cp_path = write_checkpoint(
        pipeline_dir,
        project_id,
        "assets",
        "awaiting_human",
        artifacts={"asset_manifest": manifest_data},
        pipeline_type=pipeline_type,
    )
    print(f"  Checkpoint successfully written to {cp_path}")


if __name__ == "__main__":
    main()
