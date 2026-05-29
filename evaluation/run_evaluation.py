import json
import time
import requests

BASE_URL = "http://127.0.0.1:8000/generate"

with open("evaluation/prompts.json", "r") as f:
    prompts = json.load(f)

all_prompts = (
    prompts["normal"] +
    prompts["edge_cases"]
)

results = []

success_count = 0

for prompt in all_prompts:

    start = time.time()

    try:

        response = requests.post(
            BASE_URL,
            json={
                "prompt": prompt
            }
        )

        latency = round(
            time.time() - start,
            2
        )

        data = response.json()

        success = (
            data["runtime"]["success"]
            and
            data["validation"]["is_valid"]
        )

        if success:
            success_count += 1

        results.append({
            "prompt": prompt,
            "success": success,
            "latency": latency
        })

    except Exception as e:

        results.append({
            "prompt": prompt,
            "success": False,
            "error": str(e)
        })

success_rate = round(
    success_count /
    len(all_prompts)
    * 100,
    2
)

avg_latency = round(
    sum(
        r.get("latency", 0)
        for r in results
    ) / len(results),
    2
)

summary = {
    "total_prompts": len(all_prompts),
    "success_rate": success_rate,
    "average_latency": avg_latency,
    "results": results
}

with open(
    "evaluation/results.json",
    "w"
) as f:

    json.dump(
        summary,
        f,
        indent=2
    )

print(summary)
    