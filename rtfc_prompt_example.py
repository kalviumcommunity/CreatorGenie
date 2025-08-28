"""
RTFC Prompting Example for CreatorGenie

This script demonstrates how to use the RTFC-based system and user prompts with OpenAI's API to generate a structured content calendar response.
"""

import os
import openai
from rtfc_prompt import SYSTEM_PROMPT, USER_PROMPT

openai.api_key = os.getenv("AIzaSyCxqnonVJyxlyYAHYbwJAxUelNfkI0EutA")

def get_rtfc_content_calendar():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT}
        ],
        temperature=0.7,
        max_tokens=500
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    result = get_rtfc_content_calendar()
    print("AI Response:\n", result)
