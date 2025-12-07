import torchaudio as ta
import torch
from chatterbox.tts import ChatterboxTTS

# Automatically detect the best available device
if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"

print(f"Using device: {device}")

model = ChatterboxTTS.from_pretrained(device=device)

text = ("hello this is a short video on my latest custom node transparency background remover "
       "i recently got an update version 1.0.2 you can download that from here from the comfy ui "
       "registry or the easiest way would be go into custom node manager and then search for transparency "
       "background remover 1.0.2 and click on install I've already done that.")

# Generate with default improved settings (slower, more deliberate speech)
wav = model.generate(text)
ta.save("test-1.wav", wav, model.sr)

# If you want to synthesize with a different voice, specify the audio prompt
AUDIO_PROMPT_PATH = "trimmed_audio.wav"
wav = model.generate(text, audio_prompt_path=AUDIO_PROMPT_PATH)
ta.save("test-2.wav", wav, model.sr)

# Example of different pacing settings:
# Very slow/deliberate speech
wav_slow = model.generate(text, cfg_weight=0.2, exaggeration=0.3)
ta.save("test-slow.wav", wav_slow, model.sr)

# Normal to slightly slow speech  
wav_normal = model.generate(text, cfg_weight=0.4, exaggeration=0.5)
ta.save("test-normal.wav", wav_normal, model.sr)
