import pytest
from elite_ai_agency.utils.token_estimator import count_tokens, recommend_model
from elite_ai_agency.utils.budget_tracker import record_call
from elite_ai_agency.utils.cost_calculator import ModelType, calculate_cost

def test_token_counting():
    text = "Hello world from Elite AI Agency"
    tokens = count_tokens(text)
    assert tokens > 0

def test_model_recommendation():
    complex_prompt = "Analyze the architectural trade-offs of microservices and evaluate latency."
    model = recommend_model(complex_prompt)
    assert model == "deepseek-chat"

    simple_prompt = "What is 2+2?"
    simple_model = recommend_model(simple_prompt)
    assert simple_model == "gemini-1.5-flash"

def test_cost_and_budget():
    cost = calculate_cost(ModelType.GEMINI_FLASH, 1000, 500)
    assert cost > 0
    
    usage = record_call(ModelType.GEMINI_FLASH, 1000, 500)
    assert "total_spent" in usage
    assert usage["remaining"] < 25.0