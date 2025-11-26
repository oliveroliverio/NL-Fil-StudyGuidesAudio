I think I want to switch to the Gemini 3 API rather than OpenAI. 

This is a great first start!  But I think I want a 3rd party API for audio file generation that specializes in audiobook creation for more natural sounding oral audio.  We can keep the the current LLM (or switch to Gemini 3) for creating the transcripts for stories and lessons.  But for oral audio generation, I want to explore better options, possibly even paid ones if the output is audible audiobook sounding. 

Don't code anything for now, simply write your ideas and next steps in this file.  


# Ideas & Next Steps: Gemini & Audiobook-Quality TTS

## 1. Switching to Gemini API (Transcript Generation)
You mentioned "Gemini 3". Currently, the latest stable and powerful models are **Gemini 1.5 Pro** and **Gemini 1.5 Flash**. 
-   **Gemini 1.5 Pro**: Excellent for creative writing, nuance, and handling large context (great for keeping consistent tone across a whole chapter).
-   **Library**: We will switch from `openai` to `google-generativeai` (the official Python SDK).
-   **Implementation**:
    -   Update `TranscriptEngine` to use a generic `LLMProvider` interface.
    -   Implement `GeminiLLMProvider`.
    -   Update `.env` to require `GOOGLE_API_KEY`.

## 2. "Audible-Quality" TTS Options
For "natural sounding oral audio" that rivals audiobooks, **OpenAI's TTS** is good but often lacks the dramatic range or "breathiness" of a real narrator. Here are the top contenders:

### **Option A: ElevenLabs (Highly Recommended)**
This is widely considered the gold standard for AI narration today.
-   **Why**: They specialize in "long-form" and "speech synthesis" that captures emotion, pacing, and intonation better than anyone else.
-   **Models**: `eleven_multilingual_v2` or `eleven_turbo_v2_5`.
-   **Pros**:
    -   **Voice Design**: You can clone a specific voice or pick from a massive library of "Storyteller" voices.
    -   **Context Awareness**: Better at understanding that a sentence is a question or an exclamation.
-   **Cons**: It is a paid service and can get expensive for very long audiobooks (pricing is per character).

### **Option B: Play.ht**
-   **Why**: Their "Parrot" and "Peregrine" models are very strong.
-   **Pros**: High fidelity, good cloning.
-   **Cons**: API can be a bit more complex than ElevenLabs; pricing varies.

### **Option C: Azure AI Speech (Neural)**
-   **Why**: Microsoft's Neural voices are incredibly smooth and "perfect".
-   **Pros**: Very stable, cheaper than ElevenLabs.
-   **Cons**: Can sometimes sound *too* perfect (like a news anchor rather than a storyteller), though they have "Audiobook" speaking styles for some voices.

## 3. Proposed Next Steps

### Step 1: Update Dependencies
-   Add `google-generativeai` (for Gemini).
-   Add `elevenlabs` (official SDK).

### Step 2: Refactor Configuration
-   Update `settings.yaml` to allow selecting:
    -   `transcript_provider`: `gemini` (default) or `openai`.
    -   `audio_provider`: `elevenlabs` (default for quality), `openai`, or `local`.

### Step 3: Refactor Codebase
1.  **Abstract LLM**: Create a base class for the Transcript Engine so we can easily swap OpenAI/Gemini.
2.  **Implement Gemini**: Connect the `google-generativeai` logic.
3.  **Implement ElevenLabs**: Add a new `ElevenLabsTTSProvider` in `src/tts_engine.py`.

### Step 4: Testing
-   Generate a transcript using Gemini 1.5 Pro.
-   Generate audio using an ElevenLabs "Storyteller" voice (e.g., "Rachel" or "Drew").
-   Compare the "acting" quality against the OpenAI version.

## Questions for You
1.  Do you have a **Google AI Studio API Key** (for Gemini)?
2.  Do you have an **ElevenLabs API Key** (or are you willing to sign up for a paid plan to test)?
3.  Shall we proceed with **ElevenLabs** as the primary "Premium" choice?
