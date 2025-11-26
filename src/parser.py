from pathlib import Path

def read_markdown_file(file_path: str) -> str:
    """
    Reads a markdown file and returns its content as a string.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
