from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.chat import ChatRequest
from app.ai_client import ask_ai
from app.prompt_loader import load_system_prompt
from app.memory_service import add_message
from app.memory_service import get_conversation
from app.knowledge_service import retrieve_relevant_knowledge

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
    ai_conversation = conversation.copy()
    knowledge = retrieve_relevant_knowledge(message)
    if knowledge:
        knowledge_context = "\n\n".join(knowledge)

        ai_conversation.insert(
            0,
            {
                "role": "system",
                "content": f"Relevant Business Knowledge:\n\n{knowledge_context}",
            },
        )

    reply = ask_ai(system_prompt, ai_conversation)
    add_message(session_id, "assistant", reply)
    return {
        "reply": reply
    }
