
import asyncio
from elite_ai_agency.workflow import build_conditional_agent

async def test_agent():
    app = build_conditional_agent()
    initial_state = {
        "messages": [],
        "task": "Test conditional workflow execution",
        "result": "",
        "step_count": 0,
        "cost_total": 0.0
    }
    
    print("=== Running Conditional LangGraph Agent ===")
    async for event in app.astream(initial_state):
        print(f"Event: {event}")

if __name__ == "__main__":
    asyncio.run(test_agent())
