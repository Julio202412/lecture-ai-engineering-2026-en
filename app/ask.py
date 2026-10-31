"""Lecture 01: a script that asks an LLM questions in one conversation.

Usage:
    uv run python -m app.ask "What is LoRA?"
    uv run python -m app.ask            # Start with a course-specific question

After the first answer, enter follow-up questions. Enter a blank line or :quit to exit.

A chat with no tools, retaining conversation history between questions.
Check that, when asked about course-specific information, it either says "I don't know"
or gives a plausible general answer (which differs from the actual course).
(In Lecture 03, improve it by making an agent that can search the glossary.)
"""

import argparse
from time import perf_counter

from google import genai
from google.genai import errors

from app.config import MODEL, api_error_message, get_api_key

# A course-specific question. The correct answer is in homework-levels in data/glossary.json
DEFAULT_QUESTION = "What are the 3 homework levels in the AIE2026 course?"


def ask(question: str, chat=None) -> str:
    if chat is None:
        client = genai.Client(api_key=get_api_key())
        chat = client.chats.create(model=MODEL)

    started_at = perf_counter()
    response = chat.send_message(question)
    elapsed_seconds = perf_counter() - started_at

    print(f"[time] response={elapsed_seconds:.2f}s")

    usage = response.usage_metadata
    if usage is not None:
        print(
            f"[tokens] input={usage.prompt_token_count} "
            f"output={usage.candidates_token_count}"
        )

    return response.text


def main() -> None:
    parser = argparse.ArgumentParser(description="Ask an LLM questions in one conversation")
    parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    args = parser.parse_args()

    print(f"[model] {MODEL}")
    try:
        client = genai.Client(api_key=get_api_key())
        chat = client.chats.create(model=MODEL)
        question = args.question

        while True:
            print(f"[question] {question}\n")
            print(ask(question, chat))

            try:
                question = input("\n[you] ").strip()
            except EOFError:
                break
            if not question or question.lower() == ":quit":
                break
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
