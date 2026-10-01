import json

with open("sample_jev_answer.json", encoding="utf-8") as f:
    jev_data = json.load(f)

with open("sample_answer.json", encoding="utf-8") as f:
    answer_data = json.load(f)

answer_map = {item["문항번호"]: item for item in answer_data}

correct = 0
wrong = 0
total_score = 0
max_score = 0

print(f"{'문제':>4}  {'정답':>4}  {'jev':>4}  {'결과':>4}  {'배점':>4}  confidence")
print("-" * 50)

for result in jev_data["results"]:
    number = result["number"]
    if number not in answer_map:
        continue

    correct_answer = str(answer_map[number]["정답"])
    score = answer_map[number]["배점"]
    max_score += score

    q = result["questions"].get("answer", {})
    jev_choice = str(q.get("choice", "?"))
    confidence = q.get("confidence", 0)

    is_correct = jev_choice == correct_answer
    mark = "O" if is_correct else "X"
    if is_correct:
        correct += 1
        total_score += score
    else:
        wrong += 1

    print(f"{number:>4}  {correct_answer:>4}  {jev_choice:>4}  {mark:>4}  {score:>4}점  {confidence:.0%}")

print("-" * 50)
print(f"맞은 문제: {correct}  /  틀린 문제: {wrong}  /  총 {correct + wrong}문제")
print(f"점수: {total_score} / {max_score}")
