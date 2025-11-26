import os
import yaml
from openai import OpenAI
from pathlib import Path
from src.parser import read_markdown_file

class TranscriptEngine:
    def __init__(self, config_path="config/settings.yaml"):
        self.config = self._load_config(config_path)
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
    def _load_config(self, path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    def generate_transcript(self, input_file: str, output_file: str = None) -> str:
        """
        Generates a transcript from a markdown file using OpenAI.
        """
        raw_content = read_markdown_file(input_file)
        
        system_prompt_path = self.config['transcript']['system_prompt_path']
        system_prompt = read_markdown_file(system_prompt_path)
        
        response = self.client.chat.completions.create(
            model=self.config['transcript']['default_model'],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Here is the raw content:\n\n{raw_content}"}
            ],
            temperature=self.config['transcript']['temperature']
        )
        
        transcript = response.choices[0].message.content
        
        if output_file:
            self._save_transcript(transcript, output_file)
            
        return transcript

    def _save_transcript(self, content: str, path: str):
        output_path = Path(path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
