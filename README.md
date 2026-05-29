# AI App Compiler

A compiler-style AI system that converts natural language application requirements into validated, structured, and executable application configurations.

## Objective

Transform open-ended product requirements into:

- UI Schema
- API Schema
- Database Schema
- Authentication Rules
- Business Logic

while ensuring:

- Schema Validation
- Cross-Layer Consistency
- Repair Mechanisms
- Runtime Execution Validation

---

## Architecture

```text
User Prompt
      ↓
Intent Extraction
      ↓
Intent Validation
      ↓
Repair Engine
      ↓
System Design
      ↓
Schema Generation
      ↓
Cross Validation
      ↓
Runtime Simulation
      ↓
Executable Application Configuration
```

---

## Features

### Intent Extraction

Converts natural language requirements into structured intent.

Example:

```json
{
  "app_name": "CRM",
  "features": ["contacts", "dashboard"],
  "roles": ["admin", "user"]
}
```

---

### System Design Layer

Generates:

- Entities
- Pages
- Flows
- Roles

---

### Schema Generation

Produces:

- UI Schema
- API Schema
- Database Schema
- Auth Schema
- Business Logic

---

### Validation Engine

Detects:

- Missing fields
- Invalid structures
- Cross-layer inconsistencies
- Schema mismatches

---

### Repair Engine

Performs targeted regeneration instead of rerunning the full pipeline.

Examples:

- Missing roles
- Missing features
- Missing metadata

---

### Runtime Simulator

Validates generated schemas by:

- Creating SQLite tables
- Executing schema checks
- Verifying application structure

---

## Evaluation Framework

Dataset:

- 10 Real Product Prompts
- 10 Edge Case Prompts

Metrics Collected:

- Success Rate
- Average Latency
- Validation Status
- Runtime Success
- Repair Count

---

## Tech Stack

### Backend

- FastAPI
- Python
- Pydantic
- SQLite

### Frontend

- Next.js
- TypeScript
- TailwindCSS

### LLM

- Groq
- Llama 3.3 70B

---

## Running Locally

### Backend

```bash
cd backend

pip install -r requirements.txt

python -m uvicorn app:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## API Endpoint

### Generate Application Configuration

```http
POST /generate
```

Request:

```json
{
  "prompt": "Build a CRM with login and contacts"
}
```

Response:

```json
{
  "intent": {},
  "design": {},
  "schema": {},
  "validation": {},
  "runtime": {},
  "logs": [],
  "metrics": {}
}
```

---

## Future Improvements

- Multi-model fallback
- Advanced repair strategies
- Automatic code generation
- Deployment-ready runtime generation
- Visual architecture diagrams

---

## Author

Priyanshu Singh
