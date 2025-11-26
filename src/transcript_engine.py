import os
import yaml
from abc import ABC, abstractmethod
from openai import OpenAI
import google.generativeai as genai
from pathlib import Path
from src.parser import read_markdown_file

class LLMProvider(ABC):
    @abstractmethod
    def generate_text(self, system_prompt: str, user_prompt: str) -> str:
        pass

class OpenAILLMProvider(LLMProvider):
    def __init__(self, config):
        self.config = config
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_text(self, system_prompt: str, user_prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.config['transcript']['openai']['model'],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=self.config['transcript']['temperature']
        )
        return response.choices[0].message.content

class GeminiLLMProvider(LLMProvider):
    def __init__(self, config):
        self.config = config
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel(
            model_name=self.config['transcript']['gemini']['model'],
            system_instruction=None # Gemini 1.5 Pro supports system instructions via constructor, but we'll pass it in the prompt or configure it here if we read it early.
            # Actually, let's keep it simple and pass system prompt in the generate call if possible, 
            # or configure the model with it. 
            # For 1.5 Pro, system_instruction is a valid argument.
        )

    def generate_text(self, system_prompt: str, user_prompt: str) -> str:
        # Re-instantiate model with system prompt if we want to use the native system instruction feature effectively
        # Or just prepend it. Native is better.
        model = genai.GenerativeModel(
            model_name=self.config['transcript']['gemini']['model'],
            system_instruction=system_prompt
        )
        
        response = model.generate_content(
            user_prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=self.config['transcript']['temperature']
            )
        )
        return response.text

class TranscriptEngine:
    def __init__(self, config_path="config/settings.yaml"):
        self.config = self._load_config(config_path)
        self.provider = self._get_provider()
        
    def _load_config(self, path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    def _get_provider(self):
        provider_name = self.config['transcript'].get('provider', 'openai')
        if provider_name == 'openai':
            return OpenAILLMProvider(self.config)
        elif provider_name == 'gemini':
            return GeminiLLMProvider(self.config)
        else:
            raise ValueError(f"Unknown transcript provider: {provider_name}")

    def generate_transcript(self, input_file: str, output_file: str = None) -> str:
        """
        Generates a transcript from a markdown file.
        """
        raw_content = read_markdown_file(input_file)
        
        system_prompt_path = self.config['transcript']['system_prompt_path']
        system_prompt = read_markdown_file(system_prompt_path)
        
        user_prompt = f"Here is the raw content:\n\n{raw_content}"
        
        transcript = self.provider.generate_text(system_prompt, user_prompt)
        
        if output_file:
            self._save_transcript(transcript, output_file)
            
        return transcript

    def _save_transcript(self, content: str, path: str):
        output_path = Path(path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
