from app.config import OPENAI_API_KEY, OPENAI_MODEL
from app.prompt_loader import load_system_prompt
from app.ai_client import ask_ai

print("Coffee AI Receptionist")
print("-" * 30)

print(f"Model: {OPENAI_MODEL}")
print(f"API Key Loaded: {bool(OPENAI_API_KEY)}")

user_message = "Hello"
system_prompt = load_system_prompt()

try:
    response = ask_ai(system_prompt, user_message)

    print("\nAI Response:\n")
    print(response)

except ValueError as error:
    print("\nConfiguration Error")
    print("-" * 30)
    print(error)

print("\nSystem Prompt:")
print("-" * 30)
print(system_prompt)