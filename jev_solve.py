import os
import json
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


if __name__ == "__main__":
    with open("sample_problem.json", encoding="utf-8") as f:
        items = json.load(f)

    total_input = 0
    total_output = 0
    results = []

    for item in items:
        if item["number"] == 25:
            continue
        number = item["number"]
        state = item["state"]
        questions = item["questions"]

        print(f"풀이 중... 문제 {number}")

        data = ask_jev(state, questions)

        question_results = {}
        for q_key, answer in data.get("answers", {}).items():
            q = questions[q_key]
            chosen = answer.get("choice") if isinstance(answer, dict) else answer
            confidence = answer.get("confidence", None) if isinstance(answer, dict) else None
            probs = answer.get("probabilities", {}) if isinstance(answer, dict) else {}
            question_results[q_key] = {
                "instructions": q["instructions"],
                "choice": chosen,
                "confidence": confidence,
                "options": {
                    k: {"text": v, "probability": probs.get(str(k))}
                    for k, v in q["criteria"].items()
                },
            }

        usage = data.get("usage", {})
        input_t = usage.get("input_tokens", 0)
        output_t = usage.get("output_tokens", 0)
        total_input += input_t
        total_output += output_t

        results.append({
            "number": number,
            "questions": question_results,
            "tokens": {"input": input_t, "output": output_t},
        })

    output = {
        "results": results,
        "total_tokens": {
            "input": total_input,
            "output": total_output,
            "total": total_input + total_output,
        },
    }

    with open("sample_jev_answer.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n완료! 결과가 sample_jev_answer.json에 저장되었습니다.")
    print(f"총 토큰: input={total_input}, output={total_output}, total={total_input + total_output}")
