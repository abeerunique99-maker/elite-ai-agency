
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator

class AgentState(TypedDict):
    messages: Annotated[list[str], operator.add]
    task: str
    result: str
    step_count: int
    cost_total: float

async def analyze_node(state: AgentState) -> dict:
    print("--- Analysing task ---")
    return {
        "messages": ["Analysis completed"],
        "step_count": state.get("step_count", 0) + 1
    }

async def execute_node(state: AgentState) -> dict:
    print("--- Executing task ---")
    return {
        "result": "Execution success",
        "messages": ["Execution completed"],
        "step_count": state.get("step_count", 0) + 1,
        "cost_total": 0.001
    }

def quality_gate(state: AgentState) -> str:
    print("--- Checking Quality Gate ---")
    if "success" in state.get("result", ""):
        return "end"
    return "retry"

def build_conditional_agent():
    workflow = StateGraph(AgentState)
    
    workflow.add_node("analyze", analyze_node)
    workflow.add_node("execute", execute_node)
    
    workflow.set_entry_point("analyze")
    workflow.add_edge("analyze", "execute")
    
    workflow.add_conditional_edges(
        "execute",
        quality_gate,
        {
            "end": END,
            "retry": "execute"
        }
    )
    
    return workflow.compile()
