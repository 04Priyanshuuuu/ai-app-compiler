from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import generate_design
from pipeline.schema_generator import generate_schema


intent = extract_intent(
    "Build a CRM with login, contacts, dashboard, payments and admin analytics"
)

design = generate_design(intent)

schema = generate_schema(design)

print(schema)