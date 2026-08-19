import google.generativeai as genai
from tenacity import retry, stop_after_attempt, wait_exponential
from elite_ai_agency.config import settings
from elite_ai_agency.utils.token_estimator import count_tokens
from elite_ai_agency.utils.budget_tracker import record_call
from elite_ai_agency.utils.cost_calculator import ModelType, calculate_cost

class GeminiClient:
    def __init__(self):
        if settings.gemini_api_key:
            genai.configure(api_key=settings.gemini_api_key)
        elif settings.api_key:
            genai.configure(api_key=settings.api_key)
        self.model_name = "gemini-1.5-flash"
        self.model = genai.GenerativeModel(self.model_name)

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    def generate_response(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            prompt_tokens = count_tokens(prompt)
            completion_tokens = count_tokens(response.text)
            
            # تسجيل التكلفة واستخدام الميزانية
            record_call(ModelType.GEMINI_FLASH, prompt_tokens, completion_tokens)
            
            return response.text
        except Exception as e:
            raise RuntimeError(f"Gemini API Error: {str(e)}")