import sys
import io
import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# ضبط الترميز لدعم اللغة العربية
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from elite_ai_agency.tasks import AgencyTaskManager

app = FastAPI(title="Elite AI Agency", version="1.0")
manager = AgencyTaskManager()

class AgencyRequest(BaseModel):
    task_type: str = "onboarding"  # القيمة الافتراضية للوضوح
    input_value: str

@app.get("/health")
def health_check():
    return {"status": "online", "message": "Elite AI Agency is active and running!"}

@app.post("/agency/run-agent", tags=["AI Agency"])
async def run_agent(request: AgencyRequest):
    try:
        task = request.task_type.lower()
        if task == "onboarding":
            manager.generate_and_save_onboarding_plan(request.input_value)
            return {"status": "success", "message": f"تم بنجاح إنشاء خطة Onboarding لـ: {request.input_value}"}
        
        elif task == "lead_gen":
            manager.generate_and_save_lead_gen_plan(request.input_value)
            return {"status": "success", "message": f"تم بنجاح إنشاء خطة Lead Generation لـ: {request.input_value}"}
        
        else:
            raise HTTPException(status_code=400, detail="نوع المهمة غير صحيح. استخدم 'onboarding' أو 'lead_gen'")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)