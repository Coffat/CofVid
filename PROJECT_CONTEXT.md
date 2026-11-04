# CofVid - Shared Project Context

This is the single source of truth for project architecture and conventions. All platform-specific agent files (CLAUDE.md, CODEX.md, CURSOR.md, COPILOT.md) should point here instead of duplicating this content.

## Identity

CofVid is an open-source, AI-orchestrated video production platform.

## Architecture: Instruction-Driven (Agent-First)

The AI agent IS the intelligence. Python exists only for tools and persistence. Everything else — orchestration, creative decisions, review, stage transitions — lives in instructions (YAML manifests + markdown skills) the agent follows.

```
Agent reads pipeline manifest (YAML) → reads stage director skill (MD)
→ uses tools (Python BaseTool) → self-reviews (meta skill)
→ checkpoints (Python utility) → presents to human for approval
```

**No Python orchestrator, no Python reviewer, no Python handlers.** The agent drives the pipeline.

## Source of Truth

- **Agent guide & contract:** `AGENT_GUIDE.md` (tool inventory, pipeline selection, stage agents, protocols)
- **Skill index:** `skills/INDEX.md`
- **Tool registry:** `tools/tool_registry.py`
- **Pipeline manifests:** `pipeline_defs/`
- **Artifact schemas:** `schemas/artifacts/`
- **Style playbooks:** `styles/*.yaml` (schema: `schemas/styles/playbook.schema.json`)
- **Stage director skills:** `skills/pipelines/<pipeline>/<stage>-director.md`
- **Meta skills:** `skills/meta/*.md` (reviewer, checkpoint-protocol, skill-creator)
- **Architecture deep-dive:** `docs/ARCHITECTURE.md`

## Knowledge Architecture (3 Layers)

```
Layer 1: tools/tool_registry.py     → "What tools exist" (runtime capabilities, status, cost)
Layer 2: skills/                    → "How CofVid uses them" (project conventions)
Layer 3: .agents/skills/            → "How the technology works" (generic API rules, skills.sh)
```

Each tool's `agent_skills[]` field bridges Layer 1 → Layer 3. See `skills/INDEX.md` for the full mapping.

## Current Lean Production Architecture

CofVid is configured with a cost-free, high-efficiency, privacy-first zero-key production stack:
- **TTS (Voiceover):** **VieNeu-TTS v3-Turbo** (`tools/audio/vieneu_tts.py`) — 100% local, offline ONNX inference on Apple Silicon/CPU, studio 48kHz audio, zero API cost, voices `'Hải Đăng'` (male) & `'Mai Anh'` (female). Fallback: `piper_tts`.
- **Reasoning & Multimodal Intelligence:** **Gemini Desktop Bridge** (`tools/gemini_desktop_bridge.py` via `agy` CLI & `/Applications/Gemini.app`), operating directly with zero Google API key required.
- **Visuals & B-Roll / Graphics & Motion:** **Coverr & Mixkit** (`coverr_video`, `mixkit_video`) for zero-key curated HD/4K stock video footage, plus **Pixabay Free Stock** (`pixabay_image`, `pixabay_video`, `pixabay_music`), code-driven motion graphics in **Remotion** and **HyperFrames**, and **Open Design** (`open_design_tool`) — a 100% local, zero-key editorial graphics engine providing 150+ design systems to generate publication-grade Title cards, Stat callouts, Split screens, and Lower-thirds as WebM Alpha or DOM HyperFrames, decisively eliminating "AI Slop". Pexels is deprecated/removed.
- *Legacy Cloud Models:* Paid cloud providers (ElevenLabs, FAL.ai, Kling, Seedance, Suno, MiniMax, Replicate, etc.) are deprecated/disabled in the standard workflow.

## Key Patterns

- **Pipeline state machine:** `idea -> script -> scene_plan -> assets -> edit -> compose -> publish`
- **Instruction-driven stages:** Each stage has a director skill (MD) that teaches the agent HOW
- **Pipeline manifests:** Declarative YAML defining stages, skills, tools, review focus, approval gates
- **Capability-first tool design:** Each major family exposes a selector tool plus explicit provider tools
  - Example: `tts_selector` routes to `vieneu_tts` (default) / `piper_tts`
  - Example: `image_selector` routes to `pixabay_image`
  - Example: `video_selector` routes to `coverr_video` / `mixkit_video` / `pixabay_video` / Remotion / HyperFrames
- **Style playbooks:** YAML defining visual language, typography, motion, audio, asset generation constraints
- **Artifacts are canonical:** `brief`, `script`, `scene_plan`, `asset_manifest`, `edit_decisions`, `render_report`, `publish_log`
- **Every tool inherits from `tools/base_tool.py`** (ToolContract)
- **Checkpoint policy** lives in pipeline manifest (`human_approval_default` per stage) + `skills/meta/checkpoint-protocol.md`
- **Reviewer** is a meta skill (`skills/meta/reviewer.md`), advisory, max 2 rounds
- **Cost tracker** (`tools/cost_tracker.py`) manages budget: estimate -> reserve -> reconcile
- **Canonical artifacts** validated against JSON schemas in `schemas/artifacts/`
- **Composition Runtime Defaults:** HyperFrames (`render_runtime="hyperframes"`) is the primary default composition engine across animated explainers, kinetic typography, motion graphics, and promo reels. Remotion (`render_runtime="remotion"`) is the secondary/specialized runtime for React components and TalkingHead avatars.
- **Audio Asset Libraries:** Pre-indexed, zero-API, offline-ready libraries:
  - `music_library/`: 14 CC-BY Kevin MacLeod BGM tracks across 4 moods, indexed via `music_library/manifest.json` and discovered via `tools/audio/music_library.py`.
  - `assets/sfx/`: 23 creator sound effects (UI, transitions, impacts, glitches, ambient), indexed via `assets/sfx/manifest.json`.
  - Sound design standards and ducking rules codified in `docs/AUDIO_SOUND_DESIGN_GUIDE.md`.

## Key Files

| File | Purpose |
|------|---------|
| `config.yaml` | Global configuration |
| `lib/config_model.py` | Runtime config loader (Pydantic) |
| `lib/checkpoint.py` | Checkpoint writer/reader |
| `lib/pipeline_loader.py` | Pipeline manifest loader + helpers |
| `lib/media_profiles.py` | Platform-specific render profiles |
| `styles/playbook_loader.py` | Style playbook loader + validator + design intelligence (color/type/a11y) |
| `tools/base_tool.py` | ToolContract base class |
| `tools/tool_registry.py` | Tool discovery and reporting |
| `tools/cost_tracker.py` | Budget governance |
| `tools/audio/vieneu_tts.py` | Primary local Vietnamese TTS (VieNeu-TTS v3-Turbo, ONNX Apple Silicon/CPU, zero-cost, 'Hải Đăng' & 'Mai Anh') |
| `tools/gemini_desktop_bridge.py` | Local subprocess bridge to Gemini Desktop app helper (`agy`) CLI |
| `tools/video/video_stitch.py` | Multi-clip assembly (stitch, spatial, validate, preview) |
| `tools/video/video_compose.py` | Runtime-aware composition orchestrator — HyperFrames (primary default) / Remotion (secondary/fallback) / FFmpeg based on `edit_decisions.render_runtime` |
| `tools/video/hyperframes_compose.py` | HyperFrames runtime — templated workspace materialization plus authored-workspace unified `check`/`render`, FFmpeg floor check |
| `tools/audio/music_library.py` | Local royalty-free BGM track discovery tool, scanning `music_library/` |
| `music_library/` | Curated royalty-free BGM library (14 Kevin MacLeod CC-BY 4.0 tracks across 4 core genres) indexed by `manifest.json` |
| `assets/sfx/` | Comprehensive creator SFX library (23 sound effects: UI, transitions, impacts, glitches, ambient) indexed by `manifest.json` |
| `docs/AUDIO_SOUND_DESIGN_GUIDE.md` | Authoritative audio and sound design guide for AI agents and human creators |
| `tools/graphics/threejs_world.py` | Local semantic 3D-world authoring with explicit blockout/production fidelity tiers, region-aware terrain, diagnostics, and HyperFrames atelier workspaces |
| `tools/graphics/threejs_asset_catalog.py` | CC0 GLTF/GLB catalog acquisition, inventory, and provenance for production-fidelity world builds |
| `tools/graphics/atlas_3d.py` | Atlas Cloud Tripo H3.1 text-to-3D for unique textured/PBR GLB assets |
| `tools/graphics/fal_3d.py` | fal.ai Hunyuan 3D and SAM 3D routes for image-conditioned and multi-object GLB generation |
| `tools/graphics/blender_world.py` | Blender 4.5 LTS production world assembly, terrain, lighting, camera, and Eevee Next rendering |
| `tools/character/character_animation.py` | Local character-animation tools — character specs, SVG rig plans, pose libraries, action timelines, HyperFrames packages, and QA reports |
| `lib/hyperframes_style_bridge.py` | Playbook → CSS custom properties + `DESIGN.md` bridge for HyperFrames workspaces |
| `remotion-composer/src/components/` | 8 Remotion components (TextCard, StatCard, ProgressBar, CalloutBox, ComparisonCard + charts/) |
| `.agents/skills/hyperframes*/` | Vendored HyperFrames Layer 3 skills (authoring contract, CLI, registry, website-to-video) |
| `.agents/skills/threejs-world-generation/` | Layer 3 coarse-to-fine semantic world construction and render-guided refinement workflow |
| `skills/core/hyperframes.md` | Layer 2 — when CofVid should pick HyperFrames vs Remotion, artifact → workspace mapping |
| `schemas/styles/playbook.schema.json` | Playbook schema v2 with design tokens (chart_palette, scale_system, weight_matrix, color_rules) |
| `tests/qa/` | Quality validation test scripts for tool-by-tool output inspection |

## Available Pipelines

| Pipeline | Manifest | Type |
|----------|----------|------|
| `talking-head` | `pipeline_defs/talking-head.yaml` | Footage-based |
| `animated-explainer` | `pipeline_defs/animated-explainer.yaml` | AI-generated |
| `screen-demo` | `pipeline_defs/screen-demo.yaml` | Screen-recording |
| `clip-factory` | `pipeline_defs/clip-factory.yaml` | Short-form batch extraction |
| `podcast-repurpose` | `pipeline_defs/podcast-repurpose.yaml` | Podcast repurposing |
| `cinematic` | `pipeline_defs/cinematic.yaml` | Cinematic edit |
| `animation` | `pipeline_defs/animation.yaml` | Animation-first |
| `character-animation` | `pipeline_defs/character-animation.yaml` | Local rigged character animation |
| `hybrid` | `pipeline_defs/hybrid.yaml` | Source-plus-support hybrid |
| `avatar-spokesperson` | `pipeline_defs/avatar-spokesperson.yaml` | Avatar presenter |
| `localization-dub` | `pipeline_defs/localization-dub.yaml` | Localization and dubbing |
| `framework-smoke` | `pipeline_defs/framework-smoke.yaml` | Test harness |

## When Building New Pipelines

1. Create a YAML manifest in `pipeline_defs/` (validated by `pipeline_manifest.schema.json`)
2. Create stage director skills in `skills/pipelines/<pipeline-name>/` (7 skills: idea through publish)
3. Reference meta skills (reviewer, checkpoint-protocol) in the manifest
4. Add compatible playbooks to the manifest
5. Add contract tests in `tests/contracts/`

## When Building New Tools

1. Inherit from `tools/base_tool.py` `BaseTool`
2. Put the tool in the correct capability package (`tools/audio/`, `tools/video/`, `tools/enhancement/`, `tools/analysis/`, `tools/graphics/`, `tools/avatar/`, `tools/subtitle/`)
3. Prefer the selector-plus-provider pattern:
   - one capability router tool for agent convenience
   - one concrete tool per real provider/runtime path
4. Set all contract fields (name, version, tier, capability, provider, supports, fallback_tools, agent_skills, etc.)
5. Implement `execute()` returning a `ToolResult`
6. Let discovery happen through `tools/tool_registry.py`; do not depend on ad hoc imports
7. Add a JSON schema in `schemas/tools/` if the tool has complex I/O
8. Add tests only after the runtime path is correct
