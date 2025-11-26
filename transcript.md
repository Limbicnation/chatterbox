# Video Transcript: Streamlining Dataset Creation with Multi-Vision Toolkit v2

**Title:** How to Create High-Quality LoRA Datasets in Minutes (Local & Private)

---

## **0:00 - Introduction**

**(Visual: B-roll of the Multi-Vision Toolkit UI, showing images being sorted and captioned)**

**Speaker:**
"If you've ever tried to train a LoRA or fine-tune a model, you know the pain. You spend hours collecting images, manually cropping them, and writing captions one by one. It's tedious, it's slow, and honestly, it's the reason most people quit before they even start training."

**(Visual: Cut to speaker)**

**Speaker:**
"Today, I'm going to show you a better way. I've updated my open-source **Multi-Vision Toolkit** to version 2. It now runs the state-of-the-art **Qwen2.5-VL** and **Qwen3-VL** models locally on your machine. It's got Flash Attention for 4x faster speeds, a dark mode UI, and a workflow designed specifically for AI-Toolkit."

"In this video, we're going to go from a raw folder of messy images to a perfectly curated, captioned, and formatted dataset ready for training—in just a few minutes."

---

## **1:00 - Step 1: Curation & Pre-processing**

**(Visual: Screen recording of the "Review" tab in the toolkit)**

**Speaker:**
"First, let's talk curation. Quality beats quantity every time. You don't need 100 mediocre images; you need 15 to 20 great ones."

"I've dragged my raw folder into the toolkit. Now, I can use the arrow keys to navigate. 'A' to approve, 'R' to reject. I'm looking for clear subjects, good lighting, and variety."

**(Visual: Rapidly sorting images)**

**Speaker:**
"Notice how fast this is? The app preloads the next image so there's zero lag. Once I'm done, I have my 'Approved' folder ready to go."

---

## **3:00 - Step 2: Automated Captioning with Qwen3**

**(Visual: Switching to the "Captioning" tab/mode)**

**Speaker:**
"Now for the magic. Writing captions is the worst part, so we're going to let the AI do it. I'm selecting the **Qwen3-VL-4B-Instruct** model here."

**(Visual: Showing the settings panel)**

**Speaker:**
"I can choose a template—let's go with 'Detailed'. I can also add a trigger word if I'm training a specific character. Let's hit 'Batch Process'."

**(Visual: Progress bar moving quickly)**

**Speaker:**
"Look at that speed. That's Flash Attention in action. It's analyzing every image, detecting objects, reading text, and describing the style. It's not just 'a cat'; it's 'a close-up of a fluffy tabby cat sitting on a wooden fence during golden hour'."

---

## **6:00 - Step 3: Formatting for AI-Toolkit**

**(Visual: Opening the output folder)**

**Speaker:**
"Process complete. Let's look at the files. We have our images and matching `.txt` files with our captions. This is exactly the format **AI-Toolkit** needs."

**(Visual: Briefly showing a config.yaml file)**

**Speaker:**
"All I have to do now is point my training config to this folder. The toolkit has even generated a summary report for me, so I can double-check everything before I burn GPU hours."

---

## **8:00 - Conclusion**

**(Visual: Back to speaker)**

**Speaker:**
"And that's it. What used to take me all afternoon just took us less than 10 minutes. The Multi-Vision Toolkit is 100% free and open-source. It runs locally, so your data stays private."

"I've put the link to the GitHub repo in the description. Download it, give it a try, and let me know what you create. Don't forget to like and subscribe for more AI workflows. See you in the next one!"

**(Visual: Outro screen with links to GitHub and previous videos)**
