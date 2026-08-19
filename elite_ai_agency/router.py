from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
from google import genai

router = APIRouter(prefix="/agency", tags=["AI Agency"])

class AgencyRequest(BaseModel):
    prompt: str

@router.post("/run-agent")
async def run_agent(request: AgencyRequest):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="CRITICAL: GEMINI_API_KEY environment variable is missing on Railway.")
    
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=request.prompt,
        )
        return {"status": "success", "response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gemini API Error details: {str(e)}")