"""
One-Shot Prompting Example for CreatorGenie

This script demonstrates how to use the one-shot system prompt with OpenAI's API to generate a structured content calendar response for a new use case.
"""

import os
import openai
from one_shot_prompt import SYSTEM_PROMPT

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_one_shot_content_calendar(user_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    user_prompt = "Create a 7-day Instagram content calendar for a fitness brand."
    result = get_one_shot_content_calendar(user_prompt)
    print("AI Response:\n", result)
