"""
Function Calling Example for CreatorGenie

This script demonstrates how to use OpenAI's function calling API to let the LLM call Python functions for tasks like getting trending sounds, generating hashtags, or scheduling posts.
"""

import os
import openai
import json
from functions import get_trending_sounds, generate_hashtags, schedule_post

openai.api_key = os.getenv("AIzaSyCxqnonVJyxlyYAHYbwJAxUelNfkI0EutA")

# Define function specs for OpenAI function calling
function_specs = [
    {
        "name": "get_trending_sounds",
        "description": "Get a list of trending sounds for a platform.",
        "parameters": {
            "type": "object",
            "properties": {
                "platform": {"type": "string", "description": "Platform name (Instagram or YouTube)"}
            },
            "required": ["platform"]
        }
    },
    {
        "name": "generate_hashtags",
        "description": "Generate hashtags for a topic.",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {"type": "string", "description": "Topic for hashtags"}
            },
            "required": ["topic"]
        }
    },
    {
        "name": "schedule_post",
        "description": "Schedule a post on a platform.",
        "parameters": {
            "type": "object",
            "properties": {
                "date": {"type": "string", "description": "Date to schedule post (YYYY-MM-DD)"},
                "platform": {"type": "string", "description": "Platform name"},
                "content": {"type": "string", "description": "Content to post"}
            },
            "required": ["date", "platform", "content"]
        }
    }
]

SYSTEM_PROMPT = """
You are CreatorGenie, an AI assistant for content creators. You can call functions to fetch trending sounds, generate hashtags, or schedule posts if needed. If the user asks for trends, hashtags, or scheduling, call the appropriate function and return the result.
"""

def ai_with_function_calling(user_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        functions=function_specs,
        function_call="auto",
        temperature=0.7,
        max_tokens=500
    )
    message = response["choices"][0]["message"]
    if message.get("function_call"):
        fn_name = message["function_call"]["name"]
        args = json.loads(message["function_call"]["arguments"])
        if fn_name == "get_trending_sounds":
            result = get_trending_sounds(**args)
        elif fn_name == "generate_hashtags":
            result = generate_hashtags(**args)
        elif fn_name == "schedule_post":
            result = schedule_post(**args)
        else:
            result = {"error": "Unknown function"}
        return f"Function called: {fn_name}\nResult: {result}"
    else:
        return message["content"]

if __name__ == "__main__":
    user_prompt = "Get trending sounds for Instagram."
    result = ai_with_function_calling(user_prompt)
    print("AI Response:\n", result)
