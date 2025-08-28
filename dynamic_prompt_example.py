"""
Dynamic Prompting Example for CreatorGenie

This script demonstrates how to use a dynamic system prompt with OpenAI's API, injecting brand voice and trends at runtime.
"""

import os
import openai
from dynamic_prompt import build_dynamic_prompt

openai.api_key = os.getenv("AIzaSyCxqnonVJyxlyYAHYbwJAxUelNfkI0EutA")

def get_dynamic_content_calendar(user_prompt, brand_voice, trends):
    system_prompt = build_dynamic_prompt(brand_voice, trends)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    user_prompt = "Create a 7-day Instagram content calendar for a travel blog."
    brand_voice = "Friendly, adventurous, and informative."
    trends = "Solo travel, eco-friendly destinations, travel hacks."
    result = get_dynamic_content_calendar(user_prompt, brand_voice, trends)
    print("AI Response:\n", result)
