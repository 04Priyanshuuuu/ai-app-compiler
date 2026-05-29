from pipeline.validator import validate_intent
from pipeline.repair_engine import repair_intent

intent = {
    "app_name":"CRM",
    "app_type":"CRM",
    "features":["login"],
    "roles":[]
}

validation = validate_intent(intent)

fixed = repair_intent(
    intent,
    validation
)

print(fixed)