from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Coffee AI Receptionist API is running!"
    }