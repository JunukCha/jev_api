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


def ask_jev(state: str, questions: dict) -> dict:
    payload = {
        "model": "jev-latest",
        "state": state,
        "questions": questions,
    }
    response = requests.post(ENDPOINT, headers=HEADERS, json=payload)
    if not response.ok:
        raise RuntimeError(f"HTTP {response.status_code}: {response.text}")
    return response.json()


def print_result(label: str, data: dict) -> None:
    print(f"\n=== {label} ===")
    for key, val in data.get("answers", {}).items():
        print(f"  {key}: {val}")
    usage = data.get("usage", {})
    print(f"  tokens: input={usage.get('input_tokens', 0)}, output={usage.get('output_tokens', 0)}")


if __name__ == "__main__":
    print_result("choice 한글 예시", ask_jev(
        state="계정에 로그인이 안 됩니다.",
        questions={
            "category": {
                "type": "choice",
                "instructions": "이 문의는 어떤 카테고리에 해당하나요?",
                "criteria": {
                    "auth": "인증 / 로그인 문제",
                    "billing": "결제 문제",
                    "bug": "버그 제보",
                    "general": "일반 문의",
                },
            },
        },
    ))

    print_result("choice 한글 예시", ask_jev(
        state="이중 결제가 되었어요.",
        questions={
            "category": {
                "type": "choice",
                "instructions": "이 문의는 어떤 카테고리에 해당하나요?",
                "criteria": {
                    "auth": "인증 / 로그인 문제",
                    "billing": "결제 문제",
                    "bug": "버그 제보",
                    "general": "일반 문의",
                },
            },
        },
    ))

    print_result("choice 한글 예시", ask_jev(
        state="캐릭터가 벽을 뚫고 지나가요.",
        questions={
            "category": {
                "type": "choice",
                "instructions": "이 문의는 어떤 카테고리에 해당하나요?",
                "criteria": {
                    "auth": "인증 / 로그인 문제",
                    "billing": "결제 문제",
                    "bug": "버그 제보",
                    "general": "일반 문의",
                },
            },
        },
    ))

    print_result("choice 한글 영어 혼합 예시", ask_jev(
        state="캐릭터가 벽을 뚫고 지나가요.",
        questions={
            "category": {
                "type": "choice",
                "instructions": "이 문의는 어떤 카테고리에 해당하나요?",
                "criteria": {
                    "auth": "Authentication / login issue",
                    "billing": "Billing issue",
                    "bug": "Bug report",
                    "general": "General inquiry",
                },
            },
        },
    ))