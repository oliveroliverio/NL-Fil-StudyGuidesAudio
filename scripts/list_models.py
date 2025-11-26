import os
import google.generativeai as genai
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()
console = Console()

def main():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        console.print("[bold red]Error: GOOGLE_API_KEY not found in .env[/bold red]")
        return

    genai.configure(api_key=api_key)
    
    console.print("[bold green]Listing available models:[/bold green]")
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                console.print(f"- [bold]{m.name}[/bold]")
    except Exception as e:
        console.print(f"[bold red]Error listing models: {e}[/bold red]")

if __name__ == "__main__":
    main()
