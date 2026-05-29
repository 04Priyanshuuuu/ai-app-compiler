from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import generate_design
from pipeline.schema_generator import generate_schema

from pipeline.runtime_simulator import simulate_database


intent = extract_intent(
    "Build CRM with contacts and payments"
)

design = generate_design(intent)

schema = generate_schema(design)

result = simulate_database(schema)

print(result)