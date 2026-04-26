from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Audit Banking System")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "AI Audit System Running 🚀"}