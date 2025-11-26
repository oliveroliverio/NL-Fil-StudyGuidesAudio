import argparse
import os
from dotenv import load_dotenv
from src.transcript_engine import TranscriptEngine
from rich.console import Console

load_dotenv()
console = Console()

def main():
    parser = argparse.ArgumentParser(description="Generate audio transcript from markdown.")
    parser.add_argument("input_file", help="Path to the input markdown file")
    parser.add_argument("--output", "-o", help="Path to the output transcript file", default=None)
    
    args = parser.parse_args()
    
    if not args.output:
        # Default output name based on input
        base_name = os.path.splitext(os.path.basename(args.input_file))[0]
        args.output = f"output/{base_name}_transcript.md"

    console.print(f"[bold green]Generating transcript for:[/bold green] {args.input_file}")
    
    try:
        engine = TranscriptEngine()
        transcript = engine.generate_transcript(args.input_file, args.output)
        console.print(f"[bold blue]Transcript saved to:[/bold blue] {args.output}")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    main()
