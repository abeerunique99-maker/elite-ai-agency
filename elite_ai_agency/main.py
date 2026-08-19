from fastapi import FastAPI
from elite_ai_agency.router import router

app = FastAPI(title="Elite AI Agency", version="0.1.0")

app.include_router(router)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "agency": "Elite AI Agency is online"}