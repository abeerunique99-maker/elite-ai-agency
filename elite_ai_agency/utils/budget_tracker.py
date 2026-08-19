import json
from pathlib import Path
from datetime import date
from elite_ai_agency.utils.cost_calculator import calculate_cost, ModelType

BUDGET_FILE = Path("data/budget_tracker.json")
MONTHLY_LIMIT = 25.0

def _load() -> dict:
    if not BUDGET_FILE.exists():
        BUDGET_FILE.parent.mkdir(exist_ok=True)
        return {"month": str(date.today()).replace(date.today().strftime("-%d"), ""), "spent": 0.0, "calls": 0}
    return json.loads(BUDGET_FILE.read_text(encoding="utf-8"))

def _save(data: dict) -> None:
    BUDGET_FILE.write_text(json.dumps(data, indent=4), encoding="utf-8")

def record_call(model: ModelType, input_tokens: int, output_tokens: int) -> dict:
    data = _load()
    this_month = str(date.today()).replace(date.today().strftime("-%d"), "")
    
    if data["month"] != this_month:
        data = {"month": this_month, "spent": 0.0, "calls": 0}
    
    cost = calculate_cost(model, input_tokens, output_tokens)
    data["spent"] = round(data["spent"] + cost, 6)
    data["calls"] += 1
    
    _save(data)
    
    remaining = MONTHLY_LIMIT - data["spent"]
    return {
        "call_cost": cost,
        "total_spent": data["spent"],
        "remaining": round(max(0, remaining), 4),
        "budget_warning": data["spent"] >= (MONTHLY_LIMIT * 0.8),
        "budget_exhausted": data["spent"] >= MONTHLY_LIMIT
    }