import argparse
import os
import torch
import torchaudio as ta
from chatterbox.tts import ChatterboxTTS

def generate(text_path, voice_path, output_dir):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Loading model on {device}...")
    model = ChatterboxTTS.from_pretrained(device=device)

    with open(text_path, 'r') as f:
        # Read lines and filter empty ones
        lines = [l.strip() for l in f if l.strip()]

    print(f"Found {len(lines)} lines/paragraphs to synthesize.")
    
    os.makedirs(output_dir, exist_ok=True)

    full_wavs = []
    
    for i, line in enumerate(lines):
        print(f"Generating line {i+1}/{len(lines)}: {line[:50]}...")
        if not line: continue
        try:
            # Using parameters suggested for stability/quality in user memory or defaults
            # Memory mentioned cfg_weight=0.4, exaggeration=0.5 for controlled pacing
            wav = model.generate(line, audio_prompt_path=voice_path, cfg_weight=0.4, exaggeration=0.5)
            # Ensure wav is on CPU before list append to save GPU mem
            full_wavs.append(wav.cpu())
        except Exception as e:
            print(f"Error on line {i}: {e}")

    if full_wavs:
        # Concatenate along time axis (last dimension)
        # Assuming shape [Channels, Time]
        final_wav = torch.cat(full_wavs, dim=-1)
        
        base_name = os.path.basename(text_path)
        name_no_ext = os.path.splitext(base_name)[0]
        out_file = os.path.join(output_dir, f"{name_no_ext}_audio.wav")
        
        ta.save(out_file, final_wav, model.sr)
        print(f"Saved generated audio to {out_file}")
    else:
        print("No audio generated.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True, help="Path to text transcript")
    parser.add_argument("--voice", required=True, help="Path to voice clone reference wav")
    parser.add_argument("--outdir", required=True, help="Output directory")
    args = parser.parse_args()
    
    generate(args.text, args.voice, args.outdir)
