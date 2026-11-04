# CofVid Audio & Sound Design Guide

> **Scope**: Mandatory sound design standards, asset library discovery, cue placement rules, and runtime audio wiring for AI agents and human creators in the CofVid ecosystem.

---

## 1. Core Sound Design Philosophy in CofVid

In professional video production, **sound is 50% of the viewer's experience**. A visually stunning motion graphic or video clip rendered in complete silence or paired with an uninspired, flat musical loop feels unfinished, robotic, and emotionally detached.

### The Tri-Layer Audio Mix
Every CofVid composition must be built around a balanced, three-layer auditory hierarchy:

```
+-------------------------------------------------------+
| 1. Foreground Dialogue & Voiceover (Narration / Host) |  0 dB reference (-14 LUFS dialogue)
+-------------------------------------------------------+
| 2. Tactile Sound Effects (Micro-interactions, Cuts)  |  -6 dB to -14 dB (synced to animation)
+-------------------------------------------------------+
| 3. Emotional Foundation (Dynamic Background Music)    |  -14 dB to -18 dB (ducked under speech)
+-------------------------------------------------------+
```

### Core Invariants
1. **Never leave videos silent**: Even minimalist, typographic, or data-viz pieces require clean ambient sound or gentle underscore.
2. **Never leave videos music-only** (unless producing an instrumental music video): Educational, explainer, marketing, and demo pieces require voice narration and synchronized micro-SFX to anchor user attention.
3. **Decide audio at proposal**: Background music genre, voice identity, and sound design intensity are approved during the proposal stage—never retrofitted as an afterthought during final compose.

---

## 2. Asset Discovery & Manifest Contracts

CofVid ships with zero-cost, offline-ready, pre-indexed sound libraries residing directly in the workspace.

### A. Music Library (`music_library/`)
The background music library contains 14 curated royalty-free tracks by Kevin MacLeod (licensed under **CC-BY 4.0** with full commercial and derivative rights).

- **Tool Discovery**: Accessible by AI agents via `tools/audio/music_library.py` (Tool capability: `music_library`).
- **File Manifest**: Located at `music_library/manifest.json`.
- **Metadata Contract**:
```json
{
  "id": "cool-vibes",
  "filename": "Cool Vibes.mp3",
  "title": "Cool Vibes",
  "artist": "Kevin MacLeod",
  "license": "Creative Commons Attribution 4.0 International (CC-BY 4.0)",
  "genre": "Tech / Jazz Ambient",
  "mood": "Smooth, focused, corporate, curious",
  "tempo_bpm": 125,
  "duration_s": 218.38,
  "tags": ["tech", "corporate", "explainer", "focused", "curious", "software", "ambient"],
  "best_for": "Tech explainers, software feature walk-throughs, architecture breakdowns, problem-solving"
}
```

### B. Sound Effects Library (`assets/sfx/`)
The SFX library provides 23 versatile sound effects spanning UI feedback, camera snapshots, transitions, bass drops, and digital textures.

- **File Manifest**: Located at `assets/sfx/manifest.json`.
- **Metadata Contract**:
```json
{
  "pop": {
    "id": "pop",
    "file": "pop.mp3",
    "duration": 0.72,
    "category": "ui",
    "tags": ["pop", "bubble", "spawn", "badge", "chip", "element"],
    "description": "Quick pop — element appear/spawn, chip/tag/badge in. Small precise accent.",
    "recommended_use": "Sync to cards scaling up, icons appearing, or stickers popping into view."
  }
}
```

---

## 3. Background Music Selection & Narrative Arc Pacing

### The 4 Core Video Styles

| Video Style | Recommended Tracks in `music_library/` | Character & Atmosphere |
| :--- | :--- | :--- |
| **Lo-fi / Chill** | `Carefree.mp3`, `Bossa Antigua.mp3`, `Airport Lounge.mp3` | Relaxed acoustic guitars, bossa nova rhythms, mellow lounge jazz. Best for vlogs, coffee-table chats, lifestyle, and casual SaaS onboarding. |
| **Tech & Corporate / Explainer** | `Cool Vibes.mp3`, `Daily Beetle.mp3`, `Life of Riley.mp3`, `Sneaky Snitch.mp3` | Modern, optimistic, focused, curious, and witty. Best for architecture breakdowns, product walk-throughs, and problem-solution narratives. |
| **Cinematic & Dramatic** | `Impact Moderato.mp3`, `Black Vortex.mp3`, `The Complex.mp3`, `Heartbreaking.mp3`, `Prelude and Action.mp3` | Orchestral tension, propulsive percussion, deep strings, and emotional piano. Best for high-stakes teasers, product launch countdowns, and crisis overviews. |
| **Upbeat & Modern** | `Monkeys Spinning Monkeys.mp3`, `Fluffing a Duck.mp3` | Bouncy, comical, viral, and fast. Best for TikTok/Reels short-form edits, bloopers, fast tips, and lighthearted animations. |

### Narrative Arc Pacing (Intro -> Build -> Climax -> Outro)
When arranging scenes, align the musical dynamic with the dramatic structure:

```
Energy Level
    ^
    |                                   [CLIMAX] (Hero Reveal / Peak Stat)
    |                                      /\
    |                 [BUILD]             /  \
    |             (Feature Stacks)       /    \
    |                  /---\            /      \      [OUTRO] (CTA & Resolution)
    |     [INTRO]     /     \----------/        \----------------
    |   (Hook Line)  /
    +---------------------------------------------------------------> Time (s)
```

1. **Intro (0:00 - 0:05)**: Let the music enter with a gentle 0.5s fade-in. Keep volume low so the opening vocal hook lands with maximum clarity.
2. **Build (0:05 - 0:30)**: Use steady rhythmic tracks (`Cool Vibes`, `Daily Beetle`, `Carefree`) that carry forward momentum without overwhelming the spoken information.
3. **Climax (Reveal Beat)**: Align major announcements or product unveilings with a musical beat hit, preceded by a short 1-2 second cinematic riser (`assets/sfx/riser.mp3`) or brief audio silence.
4. **Outro (Resolution & CTA)**: Fade out music smoothly over 1.5s - 2.5s as the final call-to-action card resolves.

---

## 4. Concrete SFX Cue Placement Rules

Never sprinkle random sound effects without a visual anchor. **Every SFX must punctuate an on-screen state change.**

```
+----------------------------------------------------------------------------------------------------+
| Visual Event                     | Recommended SFX (assets/sfx/)      | Placement Rule            |
+----------------------------------+------------------------------------+----------------------------+
| Fast scene cut / swipe / slide   | swoosh-fast.mp3 / whoosh-short.mp3 | Peak aligns with cut edge  |
| Major section transition         | whoosh-cinematic.mp3 / riser.mp3   | Riser crests on scene in   |
| Button press / link click        | click.mp3 / mouse-click.mp3        | Exact frame of click/press |
| Tag / badge / chip / pill popup  | pop.mp3                            | Frame scale animation hits |
| Code or terminal text streaming  | typing.mp3 / key-press.mp3         | Start of text reveal       |
| Hero logo drop / big stat slam   | impact-bass-1.mp3 / impact-bass-2  | Frame of impact landing    |
| Tip reveal / 'aha!' moment       | ding.mp3 / chime.mp3               | Visual pop-in of tip card  |
| Premium badge / gold glow        | sparkle.mp3                        | Peak of shimmer sweep      |
| Screenshot / frame freeze        | camera-shutter.mp3                 | Instant of frame freeze    |
| Warning / error banner           | error.mp3                          | Appearance of red alert    |
| Cyber / glitch transition        | glitch-1.mp3 / glitch-2.mp3        | Exact frame of distortion  |
+----------------------------------------------------------------------------------------------------+
```

### Density Guideline
- **Explainer & Motion Graphics**: 1 sound effect every 2.5 to 5.0 seconds.
- **Micro-Interactions (UI Demos)**: SFX only on meaningful actions (submitting, navigating, freezing); avoid clicking on every single keystroke.

---

## 5. Audio Ducking & Mixing Standards

To deliver broadcast-ready audio complying with **EBU R128 / ITU-R BS.1770**:

### Loudness Targets
- **Master Output**: -14 to -16 LUFS integrated loudness; True Peak $\le -1.0\text{ dBFS}$.
- **Dialogue / Voiceover**: Master reference level (0 dB reference, normalized to -14 LUFS dialogue).

### Dynamic BGM Ducking Curves
```
BGM Volume
  0 dB  |                   [Pause in Speech]                    [Outro]
        |                    +---------------+                     +----+
        |                   /                 \                   /      \
-14 dB  |-----+            /                   +-----------------+        \ (Fade)
-18 dB  |     \-----------+                     [Voice Talking]            +----> Time
        |       [Voice Starts]
```

- **Under Active Voiceover**: Duck BGM by **-14 dB to -18 dB** (linear volume `0.12` to `0.18`).
- **During Voice Pauses (> 1.5s gap)**: Swell BGM smoothly back to **-3 dB to 0 dB** (linear volume `0.70` to `0.85`) over 300ms.
- **SFX Levels**:
  - UI Clicks & Keypresses: `0.20` to `0.35` (-9 dB to -14 dB)
  - Pops & Notifications: `0.35` to `0.50` (-6 dB to -9 dB)
  - Bass Impacts & Risers: `0.50` to `0.75` (-2 dB to -6 dB)

---

## 6. Wiring Audio into HyperFrames Compositions

HyperFrames is the primary default composition runtime in CofVid. There are three seamless ways to wire audio into HyperFrames projects:

### Approach A: The Media Audio Engine (`audio_request.json` & `scripts/audio.mjs`)
Recommended for all standard pipelines. In the composition directory, author `audio_request.json`:

```json
{
  "provider": "auto",
  "lang": "en",
  "speed": 1.0,
  "lines": [
    {
      "id": "01",
      "text": "Welcome to CofVid, the autonomous video engineering studio.",
      "sfx": ["swoosh-fast", "pop"]
    },
    {
      "id": "02",
      "text": "Here is how real-time rendering transforms production pipelines.",
      "sfx": ["ding", "impact-bass-1"]
    }
  ],
  "bgm": {
    "mode": "retrieve",
    "query": "cool vibes tech explainer",
    "file": "../../music_library/Cool Vibes.mp3"
  }
}
```
Run the engine:
```bash
node .agents/skills/hyperframes-media/scripts/audio.mjs --hyperframes . --sfx-lib assets/sfx
```
This automatically produces `audio_meta.json` with word-level speech timestamps, synced SFX offsets, and ducked BGM tracks.

### Approach B: HTML Audio Declarations in HyperFrames Compositions
For bespoke or atelier compositions, declare audio elements directly inside `index.html`:

```html
<!-- Background Music Track with automatic looping and volume -->
<audio
  data-track="bgm"
  src="../../music_library/Carefree.mp3"
  loop
  data-volume="0.15"
  autoplay>
</audio>

<!-- Synchronized SFX Cues tied to timeline seconds -->
<audio
  data-track="sfx"
  data-cue-time="0.0"
  src="../../assets/sfx/swoosh-fast.mp3"
  data-volume="0.35">
</audio>

<audio
  data-track="sfx"
  data-cue-time="3.2"
  src="../../assets/sfx/pop.mp3"
  data-volume="0.40">
</audio>

<audio
  data-track="sfx"
  data-cue-time="7.8"
  src="../../assets/sfx/impact-bass-1.mp3"
  data-volume="0.60">
</audio>
```

### Approach C: Programmatic GSAP Audio Triggers
In GSAP-driven compositions (`composition.js`), trigger sound cues exactly at timeline keyframe labels:

```javascript
const tl = gsap.timeline();

tl.to(".hero-title", {
  duration: 0.6,
  y: 0,
  opacity: 1,
  ease: "back.out(1.7)",
  onStart: () => playSfx("assets/sfx/pop.mp3", 0.4)
})
.to(".stat-counter", {
  duration: 1.2,
  scale: 1,
  ease: "power3.out",
  onStart: () => playSfx("assets/sfx/impact-bass-1.mp3", 0.6)
}, "+=0.3");
```

---

## 7. AI Agent Review Checklist for Audio

Before completing the `edit` or `compose` stage, every AI agent must audit the audio against this checklist:
- [ ] Is background music configured and credited properly?
- [ ] Are voiceover levels distinct and intelligible over BGM (ducking applied)?
- [ ] Does every scene cut have a corresponding whoosh/swoosh transition sound?
- [ ] Do key visual entrances (chips, cards, statistics, alerts) have synchronized micro-SFX?
- [ ] Does the final render pass ffprobe verification without audio clipping?
EOF
