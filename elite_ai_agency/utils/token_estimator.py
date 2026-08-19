import functools
import re

@functools.lru_cache(maxsize=2)
def get_encoder():
    try:
        import tiktoken
        return tiktoken.get_encoding("cl100k_base")
    except ImportError:
        return None

def count_tokens(text: str) -> int:
    enc = get_encoder()
    if enc:
        return len(enc.encode(text))
    # خوارزمية بديلة دقيقة في حال عدم توفر tiktoken
    return len(text.split()) * 2

COMPLEX_SIGNALS = (
    "analyze", "compare", "evaluate", "architect", 
    "reason", "explain why", "trade-off", "implied"
)

def recommend_model(prompt: str, hint: str = "auto") -> str:
    if hint == "simple":
        return "gemini-1.5-flash"
    if hint == "complex":
        return "deepseek-chat"
        
    tokens = count_tokens(prompt)
    lower_prompt = prompt.lower()
    
    if any(signal in lower_prompt for signal in COMPLEX_SIGNALS) or tokens > 2000:
        return "deepseek-chat"
        
    return "gemini-1.5-flash"