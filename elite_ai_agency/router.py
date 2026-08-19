from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
from google import genai

router = APIRouter(prefix="/agency", tags=["AI Agency"])

class AgencyRequest(BaseModel):
    task_type: str = "onboarding"  # onboarding أو lead_gen
    input_value: str             # اسم العميل أو النشاط التجاري

@router.post("/run-agent")
async def run_agent(request: AgencyRequest):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="CRITICAL: GEMINI_API_KEY environment variable is missing on Railway.")
    
    try:
        client = genai.Client(api_key=api_key)
        
        # بناء الـ prompt بناءً على نوع المهمة
        if request.task_type.lower() == "onboarding":
            prompt_text = f"Create a comprehensive professional onboarding plan for the company/client: {request.input_value}"
        elif request.task_type.lower() == "lead_gen":
            prompt_text = f"Create a detailed lead generation strategy for the niche/business: {request.input_value}"
        else:
            prompt_text = f"Perform agency task '{request.task_type}' for: {request.input_value}"

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt_text,
        )
        return {
            "status": "success", 
            "task_type": request.task_type,
            "target": request.input_value,
            "response": response.text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gemini API Error details: {str(e)}")