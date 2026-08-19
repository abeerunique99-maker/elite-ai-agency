
import json
from typing import Dict, Any

class TokenCostTracker:
    # أسعار تقريبية لكل 1 مليون رمز (Tokens) كمثال تسعيري احترافي
    PRICING_MODELS = {
        "gemini-pro": {"input": 1.25, "output": 5.00},
        "deepseek-chat": {"input": 0.14, "output": 0.28}
    }

    def __init__(self, model_name: str = "gemini-pro"):
        self.model_name = model_name
        self.total_input_tokens = 0
        self.total_output_tokens = 0

    def add_usage(self, input_tokens: int, output_tokens: int):
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens

    def calculate_cost(self) -> Dict[str, Any]:
        rates = self.PRICING_MODELS.get(self.model_name, {"input": 1.0, "output": 2.0})
        
        input_cost = (self.total_input_tokens / 1_000_000) * rates["input"]
        output_cost = (self.total_output_tokens / 1_000_000) * rates["output"]
        total_cost = input_cost + output_cost

        report = {
            "model": self.model_name,
            "input_tokens": self.total_input_tokens,
            "output_tokens": self.total_output_tokens,
            "input_cost_usd": round(input_cost, 6),
            "output_cost_usd": round(output_cost, 6),
            "total_cost_usd": round(total_cost, 6)
        }
        return report

    def export_report(self, filename: str = "cost_report.json"):
        report = self.calculate_cost()
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4, ensure_ascii=False)
        print(f"--- Cost report successfully saved to {filename} ---")
        return report
