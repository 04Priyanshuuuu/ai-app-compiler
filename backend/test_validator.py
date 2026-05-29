from pipeline.validator import validate_intent

intent = {
    "app_name":"CRM",
    "app_type":"CRM",
    "features":["login"],
    "roles":[]
}

result = validate_intent(intent)

print(result)