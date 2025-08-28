"""
Multi-Shot Prompting Example for CreatorGenie

This script demonstrates how to use the multi-shot system prompt with OpenAI's API to generate a structured content calendar response for a new use case.
"""

import os
import openai
from multi_shot_prompt import SYSTEM_PROMPT

openai.api_key = os.getenv("AIzaSyCxqnonVJyxlyYAHYbwJAxUelNfkI0EutA")

def get_multi_shot_content_calendar(user_prompt):
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
    user_prompt = "Create a 7-day Instagram content calendar for a tech startup."
    result = get_multi_shot_content_calendar(user_prompt)
    print("AI Response:\n", result)
