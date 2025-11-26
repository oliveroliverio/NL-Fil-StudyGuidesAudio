import os
import yaml
from abc import ABC, abstractmethod
from openai import OpenAI
from gtts import gTTS
from pathlib import Path
from elevenlabs import ElevenLabs

class TTSProvider(ABC):
    @abstractmethod
    def generate_audio(self, text: str, output_file: str):
        pass

class OpenAITTSProvider(TTSProvider):
    def __init__(self, config):
        self.config = config
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_audio(self, text: str, output_file: str):
        response = self.client.audio.speech.create(
            model=self.config['audio']['openai']['model'],
            voice=self.config['audio']['openai']['voice'],
            input=text
        )
        response.stream_to_file(output_file)

class LocalTTSProvider(TTSProvider):
    def __init__(self, config):
        self.config = config

    def generate_audio(self, text: str, output_file: str):
        tts = gTTS(text=text, lang=self.config['audio']['local']['lang'])
        tts.save(output_file)

class ElevenLabsTTSProvider(TTSProvider):
    def __init__(self, config):
        self.config = config
        self.client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

    def generate_audio(self, text: str, output_file: str):
        audio_generator = self.client.text_to_speech.convert(
            text=text,
            voice_id=self.config['audio']['elevenlabs']['voice_id'],
            model_id=self.config['audio']['elevenlabs']['model']
        )
        
        # ElevenLabs returns a generator of bytes
        with open(output_file, 'wb') as f:
            for chunk in audio_generator:
                f.write(chunk)

class TTSEngine:
    def __init__(self, config_path="config/settings.yaml"):
        self.config = self._load_config(config_path)
        self.provider = self._get_provider()

    def _load_config(self, path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    def _get_provider(self):
        provider_name = self.config['audio']['provider']
        if provider_name == 'openai':
            return OpenAITTSProvider(self.config)
        elif provider_name == 'local':
            return LocalTTSProvider(self.config)
        elif provider_name == 'elevenlabs':
            return ElevenLabsTTSProvider(self.config)
        else:
            raise ValueError(f"Unknown TTS provider: {provider_name}")

    def generate_audio(self, text: str, output_file: str):
        """
        Generates audio from text using the configured provider.
        """
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        self.provider.generate_audio(text, output_file)
