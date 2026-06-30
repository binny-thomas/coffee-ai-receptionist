from fastapi import FastAPI

from app.models.chat import ChatRequest
from app.mock_ai_client import ask_ai
from app.prompt_loader import load_system_prompt

app = FastAPI()

system_prompt = load_system_prompt()


@app.get("/")
def root():
    return {
        "message": "Coffee AI Receptionist API is running!"
    }


@app.post("/chat")
def chat(chat_request: ChatRequest):
    reply = ask_ai(
        system_prompt,
        chat_request.message
    )

    return {
        "reply": reply
    }