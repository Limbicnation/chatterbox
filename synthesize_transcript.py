import torchaudio as ta
import torch
import chatterbox
print(f"Chatterbox location: {chatterbox.__file__}")
from chatterbox.tts import ChatterboxTTS
import os

def main():
    # Automatically detect the best available device
    if torch.cuda.is_available():
        device = "cuda"
    elif torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"

    print(f"Using device: {device}")

    try:
        model = ChatterboxTTS.from_pretrained(device=device)
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    transcript_path = "refined_transcript.txt"
    try:
        with open(transcript_path, "r") as f:
            text = f.read().replace('\n', ' ').strip()
    except FileNotFoundError:
        print(f"Error: {transcript_path} not found.")
        return

    if not text:
        print("Error: Transcript is empty.")
        return

    print(f"Synthesizing text: {text[:50]}...")

    audio_prompt_path = "output_first_15_seconds.wav"
    if not os.path.exists(audio_prompt_path):
        print(f"Warning: {audio_prompt_path} not found. Using default voice.")
        audio_prompt_path = None
    else:
        print(f"Using audio prompt: {audio_prompt_path}")

    try:
        # Enhanced settings: cfg_weight=0.4, exaggeration=0.5
        wav = model.generate(text, audio_prompt_path=audio_prompt_path, cfg_weight=0.4, exaggeration=0.5)
        output_path = "transcript_audio_enhanced.wav"
        ta.save(output_path, wav, model.sr)
        print(f"Audio saved to {output_path}")
    except Exception as e:
        print(f"Error generating audio: {e}")

if __name__ == "__main__":
    main()
