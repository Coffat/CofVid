---
name: vieneu-tts
description: High-quality Vietnamese text-to-speech using VieNeu-TTS v3-Turbo running offline on Apple Silicon / CPU via ONNX Runtime. Use as the primary and default Vietnamese narration and voiceover tool in CofVid with zero cost, high fidelity, and 100% local privacy.
license: Apache-2.0
compatibility: Runs completely offline locally on Apple Silicon (MPS / CoreML) and CPU via ONNX Runtime. No API keys required.
---

# VieNeu-TTS — Local Vietnamese Text-to-Speech

Generate natural, expressive Vietnamese narration using **VieNeu-TTS v3-Turbo** running completely offline via ONNX Runtime. In CofVid, this capability is exposed through the `vieneu_tts` tool (`capability=tts`, `provider=vieneu`).

VieNeu-TTS is the **primary, default TTS provider** for Vietnamese voiceover in CofVid. It incurs zero API cost, requires no cloud network connection, ensures complete data privacy, and delivers studio-grade 48kHz speech.

---

## Model Architecture & Performance

- **Model Engine:** VieNeu-TTS `v3turbo` architecture.
- **Runtime:** ONNX Runtime local inference optimized for Apple Silicon (CoreML / MPS) and multi-core CPU.
- **Audio Output:** 48,000 Hz, 16-bit uncompressed PCM WAV.
- **Cost:** **$0.00** (Free, 100% offline).
- **Latency:** Near real-time inference on Apple Silicon (M1/M2/M3/M4) without GPU server dependencies.

---

## Voice Profiles & Persona Selection

VieNeu-TTS v3-Turbo features two high-quality preset voice personas:

### 1. `Hải Đăng` (Male - Northern / Standard Vietnamese)
- **Characteristics:** Deep, authoritative, warm, articulate, and confident.
- **Best for:**
  - Technical & animated explainers (`animated-explainer`, `screen-demo`)
  - Documentaries and historical essays
  - Corporate presentations and investor pitches
  - News, educational overviews, and serious storytelling
- **Script Example:**
  ```yaml
  voice: "Hải Đăng"
  tone: "confident, steady, professional"
  ```

### 2. `Mai Anh` (Female - Northern / Standard Vietnamese)
- **Characteristics:** Bright, clear, gentle, natural, and expressive.
- **Best for:**
  - Storytelling and narrative shorts
  - Lifestyle, travel, food, and culture features
  - Commercial ads, social video promos, and friendly tutorials
  - Conversational, warm explainer videos
- **Script Example:**
  ```yaml
  voice: "Mai Anh"
  tone: "warm, engaging, pleasant"
  ```

---

## Vietnamese Text Preprocessing Rules

Neural TTS models like VieNeu-TTS synthesize speech with highest quality when the text is phonetically unambiguous and punctuated for rhythmic breathing.

Before sending text to `vieneu_tts`, apply the following preprocessing rules in the Script and Asset stages:

### 1. Punctuation & Natural Pacing (Dấu câu & Ngắt nghỉ)
- Break long complex sentences into shorter phonetic clauses using commas (`,`), periods (`.`), or em-dashes (`—`).
- Avoid giant run-on sentences without punctuation; the model uses punctuation to determine breath groups and intonation drops.
- Use ellipses (`...`) sparingly for intentional dramatic pauses.

### 2. Numbers & Dates (Số đếm & Ngày tháng)
Always expand numeric digits into full Vietnamese words:
- **Cardinal Numbers:**
  - `2026` → `hai nghìn không trăm hai mươi sáu`
  - `150` → `một trăm năm mươi`
  - `3.5` → `ba phẩy năm`
- **Percentages:**
  - `50%` → `năm mươi phần trăm`
  - `99.9%` → `chín mươi chín phẩy chín phần trăm`
- **Dates & Times:**
  - `15/08/2026` → `ngày mười lăm tháng tám năm hai nghìn không trăm hai mươi sáu`
  - `8h30` → `tám giờ ba mươi phút`

### 3. Currency & Units of Measurement (Tiền tệ & Đơn vị đo)
- `$100` → `một trăm đô la`
- `500.000 VNĐ` / `500k` → `năm trăm nghìn đồng`
- `100km/h` → `một trăm ki-lô-mét một giờ`
- `50kg` → `năm mươi ki-lô-gam`
- `10GB` → `mười ghi-ga-byte`

### 4. Acronyms & English Borrowed Terms (Từ viết tắt & Thuật ngữ)
Phoneticize foreign terms or translate them into accessible Vietnamese:
- `AI` → `trí tuệ nhân tạo` hoặc `A-I`
- `API` → `A-P-I`
- `CEO` → `C-E-O`
- `CPU` / `GPU` → `C-P-U` / `G-P-U`
- `CofVid` → `Cốp Vít` hoặc `Cof-Vid`

---

## Pipeline & Code Integration

### Route via `tts_selector` (Recommended)
`tts_selector` automatically prioritizes `vieneu_tts` for Vietnamese language requests:

```python
from tools.tool_registry import registry
registry.discover()
selector = registry._tools["tts_selector"]

result = selector.execute({
    "text": "Chào mừng bạn đến với CofVid, hệ thống sản xuất video tự động bằng trí tuệ nhân tạo.",
    "voice": "Hải Đăng",
    "language": "vi",
    "output_path": "output/narration_scene1.wav"
})
```

### Direct Tool Invocation
To call `vieneu_tts` directly:

```python
from tools.tool_registry import registry
registry.discover()
vieneu = registry._tools["vieneu_tts"]

result = vieneu.execute({
    "text": "Trí tuệ nhân tạo đang thay đổi cách chúng ta sáng tạo nội dung mỗi ngày.",
    "voice": "Mai Anh",
    "output_path": "output/narration_mai_anh.wav"
})

if result.success:
    print(f"Generated audio: {result.data['audio_path']}")
    print(f"Duration: {result.data['duration']}s")
```

---

## Quality Checklist

- [ ] Has the text been normalized (numbers expanded, abbreviations clarified)?
- [ ] Is the chosen voice (`Hải Đăng` vs `Mai Anh`) aligned with the video's tone?
- [ ] Are sentence clauses separated by appropriate punctuation for rhythmic breath pauses?
- [ ] Is the audio output file verified via ffprobe or sound level check?
