# Chatterbox TTS

## Project Overview

Chatterbox TTS is a production-grade, open-source Text-to-Speech (TTS) and Voice Conversion (VC) model developed by Resemble AI. It is built on a 0.5B Llama backbone and trained on 0.5M hours of cleaned data. Key features include state-of-the-art zero-shot TTS, unique emotion exaggeration control, and built-in invisible watermarking (Perth) for responsible AI usage.

**Key Features:**

* **Zero-shot TTS:** High-quality speech synthesis from text.
* **Voice Conversion:** Convert voice characteristics between audio files.
* **Emotion Control:** `exaggeration` parameter to control emotional intensity.
* **Pacing Control:** `cfg_weight` to adjust speech speed and stability.
* **Watermarking:** Implicitly adds imperceptible watermarks to generated audio.

## Environment Setup

### Prerequisites

* Python >= 3.8
* CUDA-capable GPU (highly recommended for performance), MPS (Mac), or CPU.
* FFmpeg (usually required by `librosa`/`torchaudio` for audio processing).

### Installation

To install the package in the current environment (development mode):

```bash
pip install -e .
```

Or install dependencies from `pyproject.toml`:

```bash
pip install -r requirements.txt  # If a requirements file exists, otherwise rely on pyproject.toml
```

*Note: The project uses `pyproject.toml` for dependency management.*

## Usage Guide

### 1. Python API

The core class is `ChatterboxTTS`.

```python
import torchaudio as ta
from chatterbox.tts import ChatterboxTTS

# Load model (automatically selects CUDA/MPS/CPU)
model = ChatterboxTTS.from_pretrained()

# Simple Generation
text = "Hello, world! This is a test of Chatterbox TTS."
wav = model.generate(text)
ta.save("output.wav", wav, model.sr)

# Voice Cloning (Zero-shot)
# Provide a reference audio file path
wav_cloned = model.generate(text, audio_prompt_path="reference_voice.wav")
ta.save("output_cloned.wav", wav_cloned, model.sr)

# Advanced Controls
# exaggeration: 0.5 (neutral) -> higher for more emotion/speed
# cfg_weight: 0.5 (default) -> lower (~0.3) for slower, more deliberate pacing
wav_custom = model.generate(text, exaggeration=0.7, cfg_weight=0.3)
```

### 2. Running Examples

The repository includes example scripts to get started quickly:

* **TTS Example:**

    ```bash
    python example_tts.py
    ```

* **Voice Conversion Example:**

    ```bash
    python example_vc.py
    ```

### 3. Batch Audio Generation

For generating audio from a text file (transcript) using a voice clone:

1. **Prepare Audio Reference (Recommended):**
    Denoise and normalize your reference audio for best results.

    ```bash
    ffmpeg -y -i input_voice.wav -af "highpass=f=80, afftdn, loudnorm=I=-16:TP=-1.5" cleaned_voice.wav
    ```

2. **Run Generation Script:**

    ```bash
    python generate_custom_audio.py --text transcript.txt --voice cleaned_voice.wav --outdir outputs/
    ```

### 4. Interactive Web UI (Gradio)

Launch the local web interface for testing and experimentation.

* **TTS Application:**

    ```bash
    python gradio_tts_app.py
    ```

* **Voice Conversion Application:**

    ```bash
    python gradio_vc_app.py
    ```

    *Access the UI at the URL provided in the terminal (usually `http://127.0.0.1:7860`).*

## Key File Locations

* `src/chatterbox/tts.py`: Main entry point for the TTS logic (`ChatterboxTTS` class).
* `src/chatterbox/vc.py`: Main entry point for Voice Conversion logic.
* `src/chatterbox/models/`: Contains the neural network sub-modules:
  * `t3/`: Llama-based backbone model.
  * `s3gen/`: Generation modules.
  * `voice_encoder/`: Voice encoding logic.
* `gradio_*.py`: Gradio application entry points.
* `pyproject.toml`: Project configuration and dependencies.

## Technical Details

* **Architecture:** Llama-based backbone (T3) + S3Gen.
* **Watermarking:** Uses `resemble-perth` for invisible watermarking.
* **Sampling Rate:** The model typically operates at a specific sample rate (check `model.sr`, usually 24kHz or 44.1kHz).
* **Input Limits:** The Gradio app suggests a soft limit of around 300 characters for optimal stability.
