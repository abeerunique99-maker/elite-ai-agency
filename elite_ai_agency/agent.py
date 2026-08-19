import os
import logging
from elite_ai_agency.config import settings
from elite_ai_agency.tasks import TaskManager
from google import genai

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class AIAgencyAgent:
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        self.model_name = model_name
        self.gemini_key = settings.GEMINI_API_KEY
        self.task_manager = TaskManager()
        
        if not self.gemini_key:
            logging.error("مفتاح Gemini غير موجود في ملف البيئة .env")
        elif not self.gemini_key.startswith("AQ"):
            logging.warning("تنبيه: مفتاح Gemini لا يبدأ بالبادئة المتوقعة AQ.")
            
        try:
            self.client = genai.Client(api_key=self.gemini_key)
        except Exception as e:
            logging.error(f"فشل في تهيئة عميل Gemini: {str(e)}")
            self.client = None

    def run_task(self, prompt: str) -> str:
        """
        تنفيذ المهمة عبر استدعاء نموذج Gemini مع حماية كاملة ضد الأخطاء
        """
        if not self.client:
            return "خطأ: عميل الذكاء الاصطناعي غير مهيأ بشكل صحيح."

        try:
            logging.info(f"جاري إرسال الطلب إلى النموذج {self.model_name}...")
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
            )
            return response.text
        except Exception as e:
            error_msg = f"حدث خطأ أثناء الاتصال بالنموذج أو تنفيذ المهمة: {str(e)}"
            logging.error(error_msg)
            return error_msg