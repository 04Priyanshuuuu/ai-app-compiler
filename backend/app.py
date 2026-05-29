from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pipeline.intent_extractor import extract_intent
from pipeline.validator import validate_intent
from pipeline.repair_engine import repair_intent

from pipeline.system_designer import generate_design
from pipeline.schema_generator import generate_schema

from pipeline.cross_validator import validate_schema_consistency

from pipeline.runtime_simulator import simulate_database


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
def generate(payload: dict):

    user_prompt = payload["prompt"]

    logs = []

    intent = extract_intent(user_prompt)
    
    

    if intent is None:
        return {
            "error": "LLM generation failed or rate limit exceeded",
            "stage": "intent_extraction"
        }



    logs.append({
        "stage": "intent_extraction",
        "status": "success"
    })

    validation = validate_intent(intent)

    if not validation["is_valid"]:

        intent = repair_intent(
            intent,
            validation
        )

        logs.append({
            "stage": "repair",
            "status": "executed"
        })

    design = generate_design(intent)

    logs.append({
        "stage": "system_design",
        "status": "success"
    })

    schema = generate_schema(design)

    logs.append({
        "stage": "schema_generation",
        "status": "success"
    })

    cross_validation = validate_schema_consistency(schema)

    logs.append({
        "stage": "cross_validation",
        "status": (
            "success"
            if cross_validation["is_valid"]
            else "failed"
        )
    })

    runtime = simulate_database(schema)

    logs.append({
        "stage": "runtime_simulation",
        "status": (
            "success"
            if runtime["success"]
            else "failed"
        )
    })

    metrics = {
    "pipeline_stages": len(logs),
    "validation_passed": cross_validation["is_valid"],
    "runtime_success": runtime["success"],
    "repair_count": 0
}

    return {

        "intent": intent,

        "design": design,

        "schema": schema,

        "validation": cross_validation,

        "runtime": runtime,

        "logs": logs,

        "metrics": metrics
    }