# BigQuery AI Assistant

An AI-powered BigQuery assistant designed to safely convert natural-language requests into executable BigQuery scripts.

## Overview

The system uses an agent-based workflow with multiple validation and security layers to generate, validate, approve, and execute BigQuery scripts. It includes safeguards for PII, prompt injection, moderation, hallucination, and content scope.

## Key Features

* **Natural Language to BigQuery** – Generates BigQuery scripts from user requests.
* **Script Validation** – Validates generated scripts before execution.
* **Security Guards** – Includes PII detection, prompt guards, moderation, and content-scope validation.
* **Human Approval** – Supports human-in-the-loop approval before script execution.
* **Script Execution** – Executes approved BigQuery scripts.
* **Hallucination Detection** – Validates generated responses before returning the final output.
* **Summarization** – Produces a concise final response for the user.

## Workflow

**User → Security & Validation → AI Agent → Script Generation & Validation → Authorization → Human Approval → Execution → Output Validation → Final Response**

## Tech Stack

* Python
* LangChain / LangGraph
* BigQuery
* LLM-based Agents
* PII & Moderation Guards
* Human-in-the-Loop Approval
