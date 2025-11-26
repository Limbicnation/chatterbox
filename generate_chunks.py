import torchaudio as ta
import torch
from chatterbox.tts import ChatterboxTTS
import os

def main():
    # Setup device
    if torch.cuda.is_available():
        device = "cuda"
    elif torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"
    print(f"Using device: {device}")

    # Load model
    try:
        model = ChatterboxTTS.from_pretrained(device=device)
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    # Define the 6 chunks manually based on transcript.md
    chunks = [
        # Chunk 1: Intro Part 1 (The Hook)
        "If you've ever tried to train a LoRA or fine-tune a model, you know the pain. You spend hours collecting images, manually cropping them, and writing captions one by one. It's tedious, it's slow, and honestly, it's the reason most people quit before they even start training.",
        
        # Chunk 2: Intro Part 2 (The Solution)
        "Today, I'm going to show you a better way. I've updated my open-source Multi-Vision Toolkit to version 2. It now runs the state-of-the-art Qwen2.5-VL and Qwen3-VL models locally on your machine. It's got Flash Attention for 4x faster speeds, a dark mode UI, and a workflow designed specifically for AI-Toolkit. In this video, we're going to go from a raw folder of messy images to a perfectly curated, captioned, and formatted dataset ready for training—in just a few minutes.",
        
        # Chunk 3: Step 1
        "First, let's talk curation. Quality beats quantity every time. You don't need 100 mediocre images; you need 15 to 20 great ones. I've dragged my raw folder into the toolkit. Now, I can use the arrow keys to navigate. 'A' to approve, 'R' to reject. I'm looking for clear subjects, good lighting, and variety. Notice how fast this is? The app preloads the next image so there's zero lag. Once I'm done, I have my 'Approved' folder ready to go.",
        
        # Chunk 4: Step 2
        "Now for the magic. Writing captions is the worst part, so we're going to let the AI do it. I'm selecting the Qwen3-VL-4B-Instruct model here. I can choose a template—let's go with 'Detailed'. I can also add a trigger word if I'm training a specific character. Let's hit 'Batch Process'. Look at that speed. That's Flash Attention in action. It's analyzing every image, detecting objects, reading text, and describing the style. It's not just 'a cat'; it's 'a close-up of a fluffy tabby cat sitting on a wooden fence during golden hour'.",
        
        # Chunk 5: Step 3
        "Process complete. Let's look at the files. We have our images and matching .txt files with our captions. This is exactly the format AI-Toolkit needs. All I have to do now is point my training config to this folder. The toolkit has even generated a summary report for me, so I can double-check everything before I burn GPU hours.",
        
        # Chunk 6: Conclusion
        "And that's it. What used to take me all afternoon just took us less than 10 minutes. The Multi-Vision Toolkit is 100% free and open-source. It runs locally, so your data stays private. I've put the link to the GitHub repo in the description. Download it, give it a try, and let me know what you create. Don't forget to like and subscribe for more AI workflows. See you in the next one!"
    ]

    # Audio prompt
    audio_prompt_path = "transcript_audio.wav"
    if not os.path.exists(audio_prompt_path):
        print(f"Error: {audio_prompt_path} not found.")
        return
    
    print(f"Using audio prompt: {audio_prompt_path}")

    # Generate audio for each chunk
    for i, text in enumerate(chunks):
        chunk_num = i + 1
        print(f"\nProcessing Chunk {chunk_num}...")
        print(f"Text: {text[:50]}...")
        
        try:
            wav = model.generate(text, audio_prompt_path=audio_prompt_path, cfg_weight=0.4, exaggeration=0.5)
            output_path = os.path.join("generated_audio", f"output_chunk_{chunk_num}.wav")
            ta.save(output_path, wav, model.sr)
            print(f"Saved {output_path}")
        except Exception as e:
            print(f"Error generating chunk {chunk_num}: {e}")

if __name__ == "__main__":
    main()
