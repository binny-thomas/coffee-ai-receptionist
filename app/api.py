from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.chat import ChatRequest
from app.ai_client import ask_ai
from app.prompt_loader import load_system_prompt
from app.memory_service import add_message
from app.memory_service import get_conversation

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
system_prompt = load_system_prompt()

@app.get("/")
def root():
    return {
        "message": "Coffee AI Receptionist API is running!"
    }

@app.post("/chat")
def chat(chat_request: ChatRequest):
    session_id = chat_request.session_id
    message = chat_request.message
    add_message(session_id, "user", message)
    conversation = get_conversation(session_id)
    reply = ask_ai(system_prompt, conversation)
    add_message(session_id, "assistant", reply)
    return {
        "reply": reply
    }
