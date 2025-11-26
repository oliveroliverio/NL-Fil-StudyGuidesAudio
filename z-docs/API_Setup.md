# API Key Setup Guide

This guide explains how to obtain the necessary API keys for **Google Gemini** (Transcript Generation) and **ElevenLabs** (Audio Generation).

## 1. Google Gemini (GOOGLE_API_KEY)
We use Google's **Gemini 1.5 Pro** model for generating high-quality transcripts.

1.  **Visit Google AI Studio**: Go to [https://aistudio.google.com/](https://aistudio.google.com/).
2.  **Sign In**: Log in with your Google Account.
3.  **Get API Key**:
    *   Click on the **"Get API key"** button in the top-left sidebar (or the key icon).
    *   Click **"Create API key"**.
    *   You can create a key in a new project or an existing Google Cloud project.
4.  **Copy the Key**:
    *   Copy the generated string (starts with `AIza...`).
    *   Paste it into your `.env` file as `GOOGLE_API_KEY`.

## 2. ElevenLabs (ELEVENLABS_API_KEY)
We use **ElevenLabs** for "audiobook-quality" speech synthesis.

1.  **Visit ElevenLabs**: Go to [https://elevenlabs.io/](https://elevenlabs.io/).
2.  **Sign Up / Log In**: Create an account or log in.
3.  **Access Profile**:
    *   Click on your profile icon in the bottom-left (or top-right depending on the UI version).
    *   Select **"Profile + API Key"**.
4.  **Get API Key**:
    *   You will see your API Key hidden. Click the "Eye" icon to reveal it.
    *   Click the copy button.
5.  **Copy the Key**:
    *   Paste it into your `.env` file as `ELEVENLABS_API_KEY`.

## 3. Configure Your Environment
1.  **Duplicate the Example**:
    ```bash
    cp .env.example .env
    ```
2.  **Edit `.env`**:
    Open the `.env` file and fill in your keys:
    ```env
    GOOGLE_API_KEY=AIzaSyD...
    ELEVENLABS_API_KEY=2085...
    ```
