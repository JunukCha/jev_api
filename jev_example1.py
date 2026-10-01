import os
import requests
from dotenv import load_dotenv

load_dotenv(".env.local")

API_KEY = os.getenv("TYPESAFE_API_KEY")
if not API_KEY:
    raise ValueError("TYPESAFE_API_KEY is not set. Please check your .env.local file.")

ENDPOINT = "https://api.typesafe.ai/v1/systemone"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}


total_tokens_used = {"input": 0, "output": 0}


def ask_jev(state: str, questions: dict) -> dict:
    payload = {
        "model": "jev-latest",
        "state": state,
        "questions": questions,
    }
    response = requests.post(ENDPOINT, headers=HEADERS, json=payload)
    if not response.ok:
        raise RuntimeError(f"HTTP {response.status_code}: {response.text}")
    data = response.json()

    usage = data.get("usage", {})
    input_tokens = usage.get("input_tokens", 0)
    output_tokens = usage.get("output_tokens", 0)
    total_tokens_used["input"] += input_tokens
    total_tokens_used["output"] += output_tokens

    return data


def print_result(label: str, data: dict) -> None:
    print(f"\n=== {label} ===")
    for key, val in data.get("answers", {}).items():
        print(f"  {key}: {val}")
    usage = data.get("usage", {})
    print(f"  tokens: input={usage.get('input_tokens', 0)}, output={usage.get('output_tokens', 0)}")


if __name__ == "__main__":
    # Example 1: noul (yes/no decision)
    print_result("noul example", ask_jev(
        state="I would like a refund please.",
        questions={
            "is_refund_request": {
                "type": "noul",
                "instructions": "Is this message a refund request?",
            },
            "is_urgent": {
                "type": "noul",
                "instructions": "Is this request urgent?",
            },
        },
    ))

    print_result("choice example", ask_jev(
        state="I cannot log in to my account.",
        questions={
            "category": {
                "type": "choice",
                "instructions": "Which category does this inquiry belong to?",
                "criteria": {
                    "auth": "Authentication / login issue",
                    "billing": "Billing issue",
                    "bug": "Bug report",
                    "general": "General inquiry",
                },
            },
        },
    ))

    print_result("score example", ask_jev(
        state="I absolutely love this product! I will definitely buy it again.",
        questions={
            "sentiment": {
                "type": "score",
                "instructions": "What is the sentiment score of this review?",
                "criteria": [
                    "Very negative",
                    "Negative",
                    "Neutral",
                    "Positive",
                    "Very positive",
                ],
            },
        },
    ))

    total = total_tokens_used["input"] + total_tokens_used["output"]
    print(f"\n=== total token usage ===")
    print(f"  input:  {total_tokens_used['input']}")
    print(f"  output: {total_tokens_used['output']}")
    print(f"  total:  {total}")
