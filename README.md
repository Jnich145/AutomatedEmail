# AutomatedEmail

An earlier Python experiment by [Justin Nichols](https://github.com/Jnich145) in combining market research with outreach drafting. It asks about an industry or company, generates research queries, gathers model-generated research summaries, and prints an email draft for review.

**Status:** historical experiment. Provider models are hardcoded and dependencies are unpinned. Current provider compatibility has not been verified. The script does **not** send email or manage a mailing list.

## How it works

The implementation is contained in [main.py](main.py):

1. Collect the target and optional context interactively.
2. Use Together AI to suggest search queries.
3. Use Perplexity through an OpenAI-compatible client to research each query.
4. Use Together AI again to produce the draft, then print it to the terminal.

The code also constructs a Groq client at startup, but does not call it. This is not an Ollama-based or offline application.

## Inspect and prepare locally

```bash
git clone https://github.com/Jnich145/AutomatedEmail.git
cd AutomatedEmail
python3 -m venv .venv
source .venv/bin/activate
python -m pip install python-dotenv groq together openai
```

On Windows, activate the environment with `.venv\Scripts\activate` instead. The repository does not currently contain a dependency lockfile or a tested package-version matrix.

Create a local `.env` with your own credentials, or export the corresponding environment variables:

```dotenv
TOGETHER_API_KEY=your-together-key
OPENAI_API_KEY=your-perplexity-key
GROQ_API_KEY=your-groq-key
```

Despite its name, `OPENAI_API_KEY` is passed to the **Perplexity** endpoint (`https://api.perplexity.ai`). Because the unused Groq client is created eagerly, omitting `GROQ_API_KEY` may still prevent startup with the installed SDK. Keep credentials out of commits.

Before running, check the model identifiers in `get_llama_response` and `get_perplexity_response` against your provider accounts. They currently name `meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo` and `llama-3-sonar-large-32k-online`; this README does not assert those historical identifiers are still available.

```bash
python main.py
```

Running the script sends the supplied input to external providers and can incur API charges. It was not run against live providers during this documentation refresh.

## Limits and useful next steps

- Research summaries and draft claims require human source checking; there is no structured citation validation.
- Each research summary is truncated before the final drafting prompt.
- There is no retry/recovery workflow, cost budget, or automated test suite in this repository.
- A maintenance pass should remove the unused client, adopt supported model configuration, pin dependencies, and add mocked provider tests before making reliability claims.

The intended output is a draft someone reads and edits. Sending or scheduling messages is outside this script's behavior.
