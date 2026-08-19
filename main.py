import sys
import io
import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# ضبط الترميز لدعم اللغة العربية بشكل كامل
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from elite_ai_agency.tasks import AgencyTaskManager

app = FastAPI(title="Elite AI Agency", version="1.0")
manager = AgencyTaskManager()

# نموذج البيانات الذي يتم استقباله عبر الـ API
class AgencyRequest(BaseModel):
    task_type: str       # نوع المهمة: onboarding أو lead_gen
    input_value: str     # اسم العميل أو النشاط التجاري

@app.get("/health")
def health_check():
    return {"status": "online", "message": "Elite AI Agency is active and running!"}

@app.post("/agency/run-agent")
async def run_agent(request: AgencyRequest):
    try:
        if request.task_type.lower() == "onboarding":
            print(f"\n[Agency] Processing Onboarding Plan for: {request.input_value}")
            manager.generate_and_save_onboarding_plan(request.input_value)
            return {
                "status": "success",
                "message": f"تم بنجاح إنشاء وحفظ خطة Onboarding لـ: {request.input_value} داخل مجلد reports/"
            }
        
        elif request.task_type.lower() == "lead_gen":
            print(f"\n[Agency] Processing Lead Generation Plan for: {request.input_value}")
            manager.generate_and_save_lead_gen_plan(request.input_value)
            return {
                "status": "success",
                "message": f"تم بنجاح إنشاء وحفظ خطة Lead Generation لـ: {request.input_value} داخل مجلد reports/"
            }
        
        else:
            return {
                "status": "error",
                "message": "نوع المهمة غير معروف. يرجى استخدام task_type بقيمة 'onboarding' أو 'lead_gen'."
            }
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)