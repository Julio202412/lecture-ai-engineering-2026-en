# Lecture 01 Answers

## Exercises

- Model's answer to the course-specific question (the 3 homework levels; a summary is fine):
- What you noticed when comparing it with the correct meaning in the glossary:
- Token counts you displayed (input / output):18 / 336 

## Homework

- Level attempted: Development | Advanced
- What you did: Added response-time measurement around each Gemini `send_message()` call in `app/ask.py`. Compared `gemini-3.5-flash-lite` and `gemini-3.8-flash` using the same prompt: "What is LoRA?"
- Results: `gemini-3.5-flash-lite` took 2.87 seconds and used 6 input / 661 output tokens. `gemini-3.8-flash` took 75.65 seconds and used 6 input / 830 output tokens. Both described LoRA as parameter-efficient fine-tuning, though their answers differed in length and detail.
- Observations and questions: The first `gemini-3.8-flash` attempt returned a temporary 503 "model is busy" error; the retry succeeded. This is different from a 429 rate-limit error. These single-run timings do not establish typical performance or free-tier quotas. How does latency vary across repeated trials, and what are each model's documented limits?
