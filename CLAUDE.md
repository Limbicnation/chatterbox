# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Chatterbox TTS is Resemble AI's open-source text-to-speech and voice conversion system. It features:

- Zero-shot TTS with voice cloning from a reference audio file
- Voice conversion between audio files
- Emotion/exaggeration control
- Built-in Perth watermarking on all generated audio

## Common Commands

### Installation

```bash
pip install -e .  # Development install
```

### Running Examples

```bash
python example_tts.py           # Basic TTS example
python example_vc.py            # Voice conversion example
python synthesize_transcript.py # Full transcript synthesis
```

### Batch Audio Generation

```bash
# Denoise reference audio first (recommended)
ffmpeg -y -i input_voice.wav -af "highpass=f=80, afftdn, loudnorm=I=-16:TP=-1.5" cleaned_voice.wav

# Generate audio from text file
python generate_custom_audio.py --text transcript.txt --voice cleaned_voice.wav --outdir outputs/
```

### Interactive Web UI

```bash
python gradio_tts_app.py  # TTS interface at http://127.0.0.1:7860
python gradio_vc_app.py   # Voice conversion interface
```

## Architecture

### Core Classes

**`ChatterboxTTS`** (`src/chatterbox/tts.py`):

- Main TTS entry point
- `from_pretrained(device)` - loads model from HuggingFace
- `generate(text, audio_prompt_path=None, exaggeration=0.3, cfg_weight=0.3, temperature=0.8)` - synthesizes audio
- `sr` - output sample rate (24kHz via S3GEN_SR)

**`ChatterboxVC`** (`src/chatterbox/vc.py`):

- Voice conversion entry point
- `generate(audio, target_voice_path=None)` - converts voice

### Model Pipeline

```
Text Input
    ↓
EnTokenizer (tokenization)
    ↓
T3 (Llama backbone) → speech tokens
    ↓
S3Gen (token→mel→wav) → raw audio
    ↓
Perth Watermarker → final watermarked audio
```

### Key Submodules

- **`models/t3/`**: Token-to-Token model using Llama backbone for text→speech token generation
- **`models/s3gen/`**: S3Token2Wav converts speech tokens to mel spectrograms via flow matching, then to waveforms via HiFiGAN
- **`models/voice_encoder/`**: Speaker embedding extraction for voice cloning
- **`models/s3tokenizer/`**: Speech tokenization at 16kHz (S3_SR)

### Sample Rates

- `S3_SR = 16000` - input for tokenizer and voice encoder
- `S3GEN_SR = 24000` - output sample rate

## Generation Parameters

| Parameter | Range | Effect |
|-----------|-------|--------|
| `exaggeration` | 0.25-2.0 | Higher = more emotional/faster speech. Default 0.3-0.5 |
| `cfg_weight` | 0.0-1.0 | Lower (~0.3) = slower, more deliberate. Higher = faster, follows prompt style |
| `temperature` | 0.05-5.0 | Sampling temperature. Default 0.8 |

**Recommended settings:**

- General use: `exaggeration=0.5, cfg_weight=0.5`
- Expressive/dramatic: `exaggeration=0.7+, cfg_weight=0.3`
- Fast reference speaker: lower `cfg_weight` to ~0.3

## Text Guidelines

- Text is normalized via `punc_norm()` which handles punctuation cleanup
- Soft limit ~300 characters for stability
- For longer content, split into chunks and process separately (see `generate_chunks.py`)

## Voice Cloning Workflow

### Voice Reference (Gero)

- **Location**: `Voice_Reference_Gero_2025/`
- **Primary file**: `gero_voice_reference_clean_1.wav` (17.85s)
- **Cleaned version**: `gero_voice_cleaned.wav` (24kHz mono, noise-reduced)

### Audio Cleanup Command

```bash
ffmpeg -y -i input.wav -af "highpass=f=80, afftdn=nf=-25, loudnorm=I=-16:TP=-1.5, aresample=24000" -ac 1 output_cleaned.wav
```

### Batch Voice Cloning Script

```bash
python generate_memory_breach.py  # Generates voiceover with voice cloning
```

**Script settings for cinematic narration:**

| Parameter | Value | Effect |
|-----------|-------|--------|
| `cfg_weight` | 0.1-0.2 | Ultra-slow, dramatic pacing |
| `exaggeration` | 0.75-0.8 | High emotional expressiveness |
| `temperature` | 0.85-0.9 | Natural cadence variation |

### Output Directories

- `outputs/memory_breach/` - Default voice
- `outputs/memory_breach_slow/` - Ultra-slow pacing
- `outputs/memory_breach_gero/` - Gero's cloned voice ✓
