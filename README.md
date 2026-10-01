# Jev API Examples

Python examples for [TypeSafe's Jev](https://console.typesafe.ai) — a decision model that returns typed answers (yes/no, choice, or score) from natural language input.

## Setup (Windows)

**1. Clone and create a virtual environment**

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

**2. Set your API key**

Copy `.env.example` to `.env.local` and fill in your key:

```cmd
copy .env.example .env.local
```

```env
TYPESAFE_API_KEY=apikey_your_key_here
```

Get a key at [console.typesafe.ai](https://console.typesafe.ai) → API Keys.

## Examples

| File | Description |
|------|-------------|
| `jev_example1.py` | All three question types: `noul`, `choice`, `score` |
| `jev_example2.py` | `noul` with urgency detection |

```cmd
python jev_example1.py
python jev_example2.py
```

## Question types

| Type | Description | Returns |
|------|-------------|---------|
| `noul` | Yes/no judgment | Probability (0–1) |
| `choice` | Classify into one of several options | Chosen key |
| `score` | Position on a scale | Level value |

## Output format

Each example prints answers and per-call token usage, followed by a total:

```
=== noul example ===
  is_refund_request: {'type': 'noul', 'noul': 0.99}
  is_urgent: {'type': 'noul', 'noul': 0.93}
  tokens: input=294, output=42

=== total token usage ===
  input:  294
  output: 42
  total:  336
```
