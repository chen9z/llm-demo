import os

import openai


def get_completion(prompt, model="gpt-3.5-turbo") -> str:
    openai.api_key = os.getenv("MY_OPENAI_API_KEY")
    openai.api_base = os.getenv("MY_OPENAI_API_BASE")

    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]
