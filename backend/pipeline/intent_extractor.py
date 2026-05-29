from utils.llm import generate_response
from utils.json_parser import parse_json_response

def extract_intent(user_prompt: str):

    prompt = f"""
You are an Intent Extraction Engine.

Analyze the user's application request.

Extract:

1. app_name
2. app_type
3. features
4. roles
5. assumptions

Return ONLY valid JSON.

Example:

{{
  "app_name":"CRM",
  "app_type":"CRM",
  "features":["login","contacts"],
  "roles":["admin","user"],
  "assumptions":[]
}}

User Request:

{user_prompt}
"""

    response = generate_response(prompt)

    try:
        parsed = parse_json_response(response)
        if parsed:
           return parsed
    
    except Exception:

        return {
            "error": "invalid_json",
            "raw_response": response
        }