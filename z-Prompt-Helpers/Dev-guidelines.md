# 🎧 **OBJECTIVE**

Build a complete audio-content generation system that:

1. Takes **raw markdown content** (study notes, grammar explanations, bullet lists, stories, lessons)
2. Generates a **professional audio transcript** suitable for: * Audio lessons * Story-based learning * Audiobook-style narration * Dialogue scenes * Guided language practice
3. Saves that transcript into a text or markdown file
4. A second script converts the transcript into **audio files** using either: * Premium APIs (OpenAI TTS, ElevenLabs, Gemini TTS, Azure Neural Voices, etc.) * Free/local options (Coqui TTS, Piper, Bark, OpenVoice) * Modal selection based on user settings
5. Outputs clean, high-quality `.mp3` or `.wav` files.

# 🧩 **PIPELINE REQUIREMENTS**

## **Stage 1: Transcript Generator (Python Script A)**

This script must:

* Accept raw markdown text as input
* Parse headings, lists, examples, dialogues, sections
* Convert the content into a **spoken-friendly** audio lesson transcript
* Add natural transitions between topics
* Make decisions about: * Tone (friendly, professional, narrator, teacher, dramatic, etc.) * Speaking style (slow for beginners, normal for advanced) * Optional multiple voices * Optional explanations, analogies, or micro-stories * Optional Q&A or practice prompts
* Produce **clearly segmented transcript blocks** (chapters, segments, scenes)

Also include:

* Markdown → structured JSON parsing
* Tags for voice changes or SFX cues
* User-adjustable parameters (tone, pacing, persona, voice-selection markers)

Output:

* `transcript.md` or `transcript.txt`
* Optional JSON version (`transcript.json`)

## **Stage 2: Audio Generator (Python Script B)**

This script must:

* Accept transcript from Script A
* Optionally parse voice tags or scene metadata
* Convert each transcript block into audio with the chosen TTS engine
* Stitch or export files as: * One full audio file * Multiple chapter tracks * Optional intro/outro music
* Be modular and extensible

It must support:

* **Premium APIs (high quality)**
* **Open-source local TTS (free)**

Design it so I can easily:

* Switch voice providers
* Adjust settings
* Add more engines later
* Add noise reduction or normalization later

# ⚙️ **CODE REQUIREMENTS**

When generating code:

* Include clear folder structures
* Provide CLI usage examples
* Include environment variable management `.env`
* Include config presets (YAML or JSON)
* Use modern Python patterns (dataclasses, pathlib, rich for CLI formatting if needed)
* Keep scripts clean and modular
* Avoid unnecessary complexity
* Include logging

# 📦 **PACKAGING & LONG-TERM DESIGN**

When guiding me, also explain how I can:

* Package this pipeline into a **reusable template repo**
* Use it with Antigravity or local automation
* Integrate it with my existing PDF pipeline
* Provide both “static PDF” + “audio edition” as Gumroad products
* Convert content into multilingual audio
* Scale into large content libraries

# 🧠 **HOW YOU SHOULD RESPOND**

When I ask questions or request refinements:

* Provide beginner-friendly explanations
* Provide complete code examples
* Offer alternative architectures
* Give best practices from audiobook production
* Suggest optional improvements, but keep the core simple
* Ask clarifying questions when needed
* Never hallucinate details about APIs—always ask if unsure

