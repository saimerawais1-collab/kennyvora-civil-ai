
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="KENNYVORA Civil AI",
    description="AI-powered Civil Engineering Platform",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Prototype only; restrict before production
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class EngineeringQuestion(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "project": "KENNYVORA",
        "status": "Backend foundation ready"
    }


@app.post("/ask")
def ask_engineering_ai(data: EngineeringQuestion):
    return {
        "project": "KENNYVORA",
        "question": data.question,
        "answer": (
            "Your question was received. "
            "The AI model will be connected in a future step."
        ),
        "ai_connected": False
    }
