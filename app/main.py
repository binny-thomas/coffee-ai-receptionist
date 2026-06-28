from app.config import OPENAI_API_KEY, OPENAI_MODEL
from app.prompt_loader import load_system_prompt


print("Coffee AI Receptionist")
print("-" * 30)

print(f"Model: {OPENAI_MODEL}")
print(f"API Key Loaded: {bool(OPENAI_API_KEY)}")

system_prompt = load_system_prompt()

print("\nSystem Prompt:")
print("-" * 30)
print(system_prompt)