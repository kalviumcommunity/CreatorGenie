"""
functions.py

This module defines tool functions for CreatorGenie, such as getting trending sounds, generating hashtags, and scheduling posts. These functions are designed to be used with OpenAI's function calling API.
"""

import random

def get_trending_sounds(platform: str = "Instagram"):
    """Return a list of trending sounds for the given platform."""
    # Dummy data for demonstration
    if platform.lower() == "instagram":
        return ["Sound A", "Sound B", "Sound C"]
    elif platform.lower() == "youtube":
        return ["Track X", "Track Y", "Track Z"]
    return []

def generate_hashtags(topic: str):
    """Generate a list of hashtags for a given topic."""
    # Dummy data for demonstration
    base = topic.replace(" ", "").lower()
    return [f"#{base}", f"#{base}life", f"#trending{random.randint(1,100)}"]

def schedule_post(date: str, platform: str, content: str):
    """Schedule a post (dummy implementation)."""
    return {"status": "scheduled", "date": date, "platform": platform, "content": content}
