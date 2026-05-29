import json
import re


def parse_json_response(response_text):

    try:
        return json.loads(response_text)

    except:

        pass

    try:

        cleaned = re.sub(
            r"^```json\s*|\s*```$",
            "",
            response_text.strip(),
            flags=re.MULTILINE
        )

        return json.loads(cleaned)

    except Exception:

        return None