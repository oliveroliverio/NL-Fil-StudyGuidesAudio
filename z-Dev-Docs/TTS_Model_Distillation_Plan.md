# TTS Model Distillation Project Plan

This document outlines the strategy for creating a new project dedicated to training a high-quality TTS model using data generated from ElevenLabs.

## Instructions

### Objective
Create a robust, automated pipeline to:
1.  **Generate Data**: Use the existing "Study Guide" project to mass-produce audio (ElevenLabs) and text (Gemini) pairs.
2.  **Curate Data**: Automatically organize, validate, and preprocess this data for training.
3.  **Train Model**: Fine-tune a state-of-the-art base model (e.g., VITS, XTTS, or similar) on this high-quality synthetic dataset.
4.  **Evaluate**: Metrics to ensure the local model matches ElevenLabs' quality.

### Hardware Context
-   **GPU**: NVIDIA RTX 6000 Ada Generation (Blackwell/Ada architecture).
-   **VRAM**: 48GB.
-   **Capability**: Capable of full fine-tuning of large TTS models, batch processing, and rapid experimentation.

### Project Structure
The project should evolve from exploration (Notebooks) to a production-grade pipeline (Scripts).

---

## LLM Prompt for Project Setup

**Copy and paste the following prompt into a new chat to initialize the project:**

***

**Role**: You are a Senior AI Engineer specializing in Speech Synthesis and MLOps.

**Objective**: Initialize a new Python project for **TTS Model Distillation**. The goal is to train a local Text-to-Speech model that mimics the quality and style of ElevenLabs voices, using data we generate ourselves.

**Hardware**: I have a local workstation with an **NVIDIA RTX 6000 (48GB VRAM)**. Optimize all training configurations for this high-end hardware (e.g., large batch sizes, mixed precision `bf16`, efficient data loading).

**Project Scope**:
1.  **Data Factory**: A module that consumes my existing "Study Guide" content (Markdown -> Transcript -> Audio) to build a dataset.
    *   *Input*: Markdown files.
    *   *Process*: Generate Transcript (Gemini) -> Generate Audio (ElevenLabs).
    *   *Output*: `metadata.csv` (path|text|speaker), `/wavs` directory.
2.  **Data Engineering**:
    *   Audio preprocessing (resampling to 22050Hz/24000Hz, silence trimming, loudness normalization).
    *   Text cleaning (phonemization if needed).
    *   Quality Control (QC): Automated checks for audio length, silence, and alignment.
3.  **Model Training**:
    *   We will likely fine-tune a model like **Coqui XTTS v2**, **VITS**, or **StyleTTS2**.
    *   Implement training pipelines using PyTorch Lightning or similar robust frameworks.
    *   Support for Checkpointing, TensorBoard/WandB logging.
4.  **Evaluation**:
    *   Objective metrics: WER (using Whisper for ASR), MCD (Mel Cepstral Distortion).
    *   Subjective inference testing.

**Initial Deliverables**:

1.  **Directory Structure**:
    ```text
    tts-distillation/
    ├── notebooks/          # Exploration & Visualization
    ├── src/
    │   ├── data/           # Dataset creation & loading
    │   ├── model/          # Model architecture & config
    │   ├── training/       # Trainer loops
    │   └── utils/          # Audio processing tools
    ├── configs/            # YAML configs for training
    ├── datasets/           # Raw & Processed data
    ├── checkpoints/        # Model weights
    └── requirements.txt
    ```

2.  **`requirements.txt`**:
    *   Include `torch`, `torchaudio` (with CUDA support).
    *   `librosa`, `scipy`, `pandas`, `numpy`.
    *   `coqui-tts` (or specific repo dependencies).
    *   `transformers`, `accelerate`.
    *   `wandb`, `tensorboard`.
    *   `jupyterlab`.

3.  **Jupyter Notebook (`01_setup_and_data_prep.ipynb`)**:
    *   Code to initialize the workspace.
    *   A function to ingest the `output/` folder from my *other* project (Study Guides) and format it into a standard LJSpeech-style dataset.
    *   Visualization of Mel Spectrograms to verify audio quality.

**Action**:
Please generate the file structure, the `requirements.txt` optimized for my RTX 6000, and the code for the initial Jupyter Notebook to set up the data pipeline.
