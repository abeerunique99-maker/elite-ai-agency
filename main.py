import sys
import io
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from elite_ai_agency.tasks import AgencyTaskManager

app = FastAPI(title="Elite AI Agency", version="1.0")
manager = AgencyTaskManager()

class AgencyRequest(BaseModel):
    task: str = ""
    client_name: str = "Nexus Corp"
    niche: str = "Real Estate Agency"

@app.get("/health")
def health_check():
    return {"status": "online", "agency": "Elite AI Agency is running!"}

@app.post("/agency/run-agent")
async def run_agent(request: AgencyRequest):
    try:
        # سنقوم بتشغيل المهمة حسب المدخلات أو الطلب
        if "onboarding" in request.task.lower() or request.client_name:
            # افتراضياً سننفذ خطة Onboarding أو نستغل الـ manager
            manager.generate_and_save_onboarding_plan(request.client_name)
            return {
                "status": "success",
                "message": f"Onboarding plan generated and saved for client: {request.client_name}"
            }
        else:
            manager.generate_and_save_lead_gen_plan(request.niche)
            return {
                "status": "success",
                "message": f"Lead Generation plan generated and saved for niche: {request.niche}"
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)