from dataclasses import dataclass
from enum import Enum

class ModelType(Enum):
    DEEPSEEK_CHAT = "deepseek-chat"
    DEEPSEEK_REASONER = "deepseek-reasoner"
    GEMINI_FLASH = "gemini-1.5-flash"
    GEMINI_PRO = "gemini-1.5-pro"

@dataclass(frozen=True)
class ModelCost:
    input_per_million: float
    output_per_million: float

MODEL_COSTS: dict[ModelType, ModelCost] = {
    ModelType.DEEPSEEK_CHAT: ModelCost(0.14, 0.28),
    ModelType.DEEPSEEK_REASONER: ModelCost(0.55, 2.19),
    ModelType.GEMINI_FLASH: ModelCost(0.075, 0.30),
    ModelType.GEMINI_PRO: ModelCost(3.50, 10.50),
}

def calculate_cost(model: ModelType, input_tokens: int, output_tokens: int) -> float:
    costs = MODEL_COSTS[model]
    return round(
        (input_tokens / 1_000_000) * costs.input_per_million +
        (output_tokens / 1_000_000) * costs.output_per_million, 6
    )