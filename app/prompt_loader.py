from pathlib import Path

def load_system_prompt():
    """Load and return the system prompt """

    prompt_path = Path("prompts/system_prompt.txt")

    return prompt_path.read_text(encoding="utf-8")

