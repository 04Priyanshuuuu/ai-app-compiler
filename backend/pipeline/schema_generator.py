import json

from utils.llm import generate_response
from utils.json_parser import parse_json_response


def generate_schema(design):

    prompt = f"""
You are a Schema Generation Engine.

Generate:

1. ui
2. api
3. database
4. auth
5. business_logic

Return ONLY valid JSON.

Architecture:

{json.dumps(design, indent=2)}
"""

    response = generate_response(prompt)

    parsed = parse_json_response(response)

    if parsed:
        return parsed

    return {
        "error":"invalid_schema_json",
        "raw_response":response
    }