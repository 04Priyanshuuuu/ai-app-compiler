from pipeline.intent_extractor import extract_intent

result = extract_intent(
    "Build a CRM with login, contacts, dashboard, payments and admin analytics"
)

print(result)