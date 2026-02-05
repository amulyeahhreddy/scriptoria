import requests
from config import Config

# def generate_text(prompt, model="gemini", temperature=0.7):
#     if model == "gemini":
#         return call_gemini(prompt, temperature)
#     else:
#         raise ValueError("Unsupported LLM")

# def call_gemini(prompt, temperature):
#     return f"[GEMINI GENERATED OUTPUT]\n{prompt}"

def generate_text(prompt, model="gemini", temperature=0.7):
    if model == "gemini":
        return call_gemini(prompt, temperature)
    else:
        raise ValueError(f"Unsupported LLM: {model}")

def call_gemini(prompt, temperature):
    return {
        "provider": "gemini",
        "temperature": temperature,
        "output": f"[GEMINI GENERATED OUTPUT]\n{prompt}"
    }
