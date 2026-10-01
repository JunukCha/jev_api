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
