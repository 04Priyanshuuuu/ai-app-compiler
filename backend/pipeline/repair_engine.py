import json

from utils.llm import generate_response
from utils.json_parser import parse_json_response


def repair_intent(intent, validation_result):

    repaired = intent.copy()

    for error in validation_result["errors"]:

        if error == "missing_roles":

            repair_prompt = f"""
You are a Repair Engine.

The application intent is missing roles.

Generate ONLY the roles field.

Intent:

{json.dumps(intent, indent=2)}

Return JSON only.

Example:

{{
  "roles": ["admin", "user"]
}}
"""

            response = generate_response(repair_prompt)

            parsed = parse_json_response(response)

            if parsed and "roles" in parsed:

                repaired["roles"] = parsed["roles"]

        elif error == "missing_features":

            repair_prompt = f"""
You are a Repair Engine.

The application intent is missing features.

Generate ONLY the features field.

Intent:

{json.dumps(intent, indent=2)}

Return JSON only.

Example:

{{
  "features": ["dashboard", "authentication"]
}}
"""

            response = generate_response(repair_prompt)

            parsed = parse_json_response(response)

            if parsed and "features" in parsed:

                repaired["features"] = parsed["features"]

        elif error == "missing_app_name":

            repair_prompt = f"""
You are a Repair Engine.

Generate ONLY app_name.

Intent:

{json.dumps(intent, indent=2)}

Return JSON only.

Example:

{{
  "app_name": "CRM"
}}
"""

            response = generate_response(repair_prompt)

            parsed = parse_json_response(response)

            if parsed and "app_name" in parsed:

                repaired["app_name"] = parsed["app_name"]

        elif error == "missing_app_type":

            repair_prompt = f"""
You are a Repair Engine.

Generate ONLY app_type.

Intent:

{json.dumps(intent, indent=2)}

Return JSON only.

Example:

{{
  "app_type": "CRM"
}}
"""

            response = generate_response(repair_prompt)

            parsed = parse_json_response(response)

            if parsed and "app_type" in parsed:

                repaired["app_type"] = parsed["app_type"]

    return repaired