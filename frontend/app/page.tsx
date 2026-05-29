"use client";

import { useState } from "react";

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const generateApp = async () => {
    try {
      setLoading(true);

      const response = await fetch(
        "http://127.0.0.1:8000/generate",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            prompt,
          }),
        }
      );

      const data = await response.json();

      setResult(data);
    } catch (error) {
      console.error(error);
      alert("Failed to generate");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen p-8 max-w-7xl mx-auto">
      <h1 className="text-4xl font-bold mb-6">
        AI App Compiler
      </h1>

      <textarea
        className="w-full border rounded-lg p-4 h-40"
        placeholder="Build a CRM with login, contacts, dashboard, payments and admin analytics..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <button
        onClick={generateApp}
        disabled={loading}
        className="mt-4 px-6 py-3 rounded-lg border"
      >
        {loading ? "Generating..." : "Generate"}
      </button>

      {result && (
        <>
          <div className="mt-10">
            <h2 className="text-2xl font-semibold mb-3">
              Pipeline Logs
            </h2>

            <pre className="border p-4 rounded-lg overflow-auto">
              {JSON.stringify(result.logs, null, 2)}
            </pre>
          </div>

          <div className="mt-10">
            <h2 className="text-2xl font-semibold mb-3">
              Metrics
            </h2>

            <pre className="border p-4 rounded-lg overflow-auto">
              {JSON.stringify(result.metrics, null, 2)}
            </pre>
          </div>

          <div className="mt-10">
            <h2 className="text-2xl font-semibold mb-3">
              Generated Configuration
            </h2>

            <pre className="border p-4 rounded-lg overflow-auto max-h-[700px]">
              {JSON.stringify(result, null, 2)}
            </pre>
          </div>
        </>
      )}
    </main>
  );
}