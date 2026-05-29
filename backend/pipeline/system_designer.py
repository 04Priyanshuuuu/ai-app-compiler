import json

from utils.llm import generate_response
from utils.json_parser import parse_json_response


def generate_design(intent):

    prompt = f"""
You are a System Design Engine.

Convert this intent into application architecture.

Generate:

1. entities
2. pages
3. flows
4. roles

Return ONLY valid JSON.

Intent:

{json.dumps(intent, indent=2)}
"""

    response = generate_response(prompt)

    parsed = parse_json_response(response)

    if parsed:
        return parsed

    return {
        "error": "invalid_design_json",
        "raw_response": response
    }