"""
Chain-of-Thought Prompting Example for CreatorGenie

This script demonstrates how to use the chain-of-thought system prompt with OpenAI's API to generate a content calendar with explicit reasoning steps.
"""

import os
import openai
from cot_prompt import SYSTEM_PROMPT

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_cot_content_calendar(user_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=800
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    user_prompt = "Create a 7-day Instagram content calendar for a mental health awareness campaign."
    result = get_cot_content_calendar(user_prompt)
    print("AI Response:\n", result)
