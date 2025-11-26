import argparse
import os
from dotenv import load_dotenv
from src.tts_engine import TTSEngine
from src.parser import read_markdown_file
from rich.console import Console

load_dotenv()
console = Console()

def main():
    parser = argparse.ArgumentParser(description="Generate audio from transcript.")
    parser.add_argument("input_file", help="Path to the transcript file (markdown or text)")
    parser.add_argument("--output", "-o", help="Path to the output audio file", default=None)
    
    args = parser.parse_args()
    
    if not args.output:
        # Default output name based on input
        base_name = os.path.splitext(os.path.basename(args.input_file))[0]
        # Remove _transcript suffix if present to avoid duplication
        base_name = base_name.replace("_transcript", "")
        args.output = f"output/{base_name}.mp3"

    console.print(f"[bold green]Generating audio for:[/bold green] {args.input_file}")
    
    try:
        # Read the transcript content
        # Note: Ideally we should parse the transcript to remove headers/metadata if needed,
        # but for now we'll pass the whole text or a simple cleaned version.
        # For this iteration, we assume the transcript is clean enough or we just read it all.
        text = read_markdown_file(args.input_file)
        
        # Simple cleanup: Remove markdown headers if they are just structural?
        # Actually, let's keep it simple: The LLM should have produced a "script".
        # If there are headers like "# Introduction", the TTS will read "Hashtag Introduction" or just "Introduction".
        # We might want to strip lines starting with # for better experience, but let's see.
        # For now, let's strip lines starting with # to avoid reading headers.
        lines = [line for line in text.split('\n') if not line.strip().startswith('#')]
        clean_text = "\n".join(lines)

        engine = TTSEngine()
        engine.generate_audio(clean_text, args.output)
        console.print(f"[bold blue]Audio saved to:[/bold blue] {args.output}")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    main()
