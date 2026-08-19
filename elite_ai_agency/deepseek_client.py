import httpx
from tenacity import retry, stop_after_attempt, wait_exponential
from elite_ai_agency.config import settings
from elite_ai_agency.utils.token_estimator import count_tokens
from elite_ai_agency.utils.budget_tracker import record_call
from elite_ai_agency.utils.cost_calculator import ModelType, calculate_cost

class DeepSeekClient:
    def __init__(self):
        self.api_key = settings.deepseek_api_key
        self.api_url = "https://api.deepseek.com/v1/chat/completions"
        self.model_name = "deepseek-chat"

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    def generate_response(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}]
        }
        
        try:
            with httpx.Client(timeout=30.0) as client:
                response = client.post(self.api_url, json=payload, headers=headers)
                response.raise_for_status()
                data = response.json()
                
                content = data["choices"][0]["message"]["content"]
                prompt_tokens = count_tokens(prompt)
                completion_tokens = count_tokens(content)
                
                # تسجيل التكلفة واستخدام الميزانية
                record_call(ModelType.DEEPSEEK_CHAT, prompt_tokens, completion_tokens)
                
                return content
        except Exception as e:
            raise RuntimeError(f"DeepSeek API Error: {str(e)}")