# Jev API Examples

Python examples for [TypeSafe's Jev](https://console.typesafe.ai) — a decision model that returns typed answers (yes/no, choice, or score) from natural language input.

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/JunukCha/jev_api.git
cd jev_api
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate.bat

# Linux / macOS
# source .venv/bin/activate

pip install -r requirements.txt
```

**3. Set your API key**

Copy `.env.example` to `.env.local`:

```bash
# Windows
copy .env.example .env.local

# Linux / macOS
# cp .env.example .env.local
```

Then add your API key to `.env.local`:

```env
TYPESAFE_API_KEY=apikey_your_key_here
```

Get a key at [console.typesafe.ai](https://console.typesafe.ai) → **API Keys**.

## Examples

| File | Description |
|------|-------------|
| `jev_basic.py` | All three question types: `noul`, `choice`, `score` |
| `jev_context_sensitivity.py` | How adding a word ("very quickly") changes `noul` output |
| `jev_korean.py` | Korean instructions/criteria, and mixing Korean with English |
| `jev_solve.py` | Solve English reading comprehension questions from `sample_problem.json` |
| `jev_compare.py` | Compare `sample_jev_answer.json` against `sample_answer.json` and print a score |

```cmd
python jev_basic.py
python jev_context_sensitivity.py
python jev_korean.py
python jev_solve.py      # saves results to sample_jev_answer.json
python jev_compare.py    # requires sample_jev_answer.json
```

## Question types

| Type | Description | Returns |
|------|-------------|---------|
| `noul` | Yes/no judgment | Probability (0–1) |
| `choice` | Classify into one of several options | Chosen key + per-option probabilities |
| `score` | Position on a scale | Level value |

## Output example (`jev_compare.py`)

```
문제  정답   jev  결과  배점  confidence
--------------------------------------------------
  18     2     2     O     2점  100%
  19     1     1     O     2점   95%
  20     2     2     O     2점  100%
--------------------------------------------------
맞은 문제: 3  /  틀린 문제: 0  /  총 3문제
점수: 6 / 6
```
