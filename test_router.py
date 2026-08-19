from elite_ai_agency.utils.token_estimator import count_tokens, recommend_model
from elite_ai_agency.utils.budget_tracker import record_call
from elite_ai_agency.utils.cost_calculator import ModelType

def test_system():
    prompt = "What is 2+2, and analyze the architectural trade-offs of microservices."
    tokens = count_tokens(prompt)
    model = recommend_model(prompt)
    
    print(f"[✔] عدد الـ Tokens المقدرة: {tokens}")
    print(f"[✔] النموذج المقترح للمهمة: {model}")
    
    # تسجيل استدعاء تجريبي في حارس الميزانية
    usage_res = record_call(ModelType.GEMINI_FLASH, tokens, 100)
    print(f"[✔] تقرير الميزانية المالي: {usage_res}")

if __name__ == "__main__":
    test_system()