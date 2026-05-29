from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import generate_design

intent = extract_intent(
    "Build a CRM with login, contacts, dashboard, payments and admin analytics"
)

design = generate_design(intent)

print(design)