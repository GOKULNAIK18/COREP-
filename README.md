# LLM-Assisted PRA COREP Reporting Assistant (Prototype)

## Overview

This project is a prototype **LLM-assisted regulatory reporting assistant** designed to support UK banks in preparing **PRA COREP regulatory returns**.

COREP reporting is complex and error-prone because analysts must interpret dense PRA Rulebook requirements and EBA COREP instructions, then translate them accurately into structured reporting templates. This prototype demonstrates how **LLMs combined with regulatory text retrieval, validation, and auditability** can reduce manual effort and reporting risk.

The solution is intentionally scoped to a **well-defined subset of COREP**, as required by the assignment.

---

## Scope

- **Regulator**: UK Prudential Regulation Authority (PRA)
- **Regulatory framework**:
  - PRA Rulebook (Own Funds, Capital Requirements)
  - EBA COREP reporting instructions
- **COREP templates implemented**:
  - **C 01.00 – Own Funds**
  - **C 02.00 – Capital Requirements**

This constrained scope ensures the prototype is realistic, explainable, and suitable for demonstration.

---

## Key Features

- Natural-language user questions and simple reporting scenarios
- Semantic retrieval of relevant PRA Rulebook sections and COREP instructions
- LLM-assisted reasoning with **strict, schema-locked structured output**
- Automatic population of **human-readable COREP template extracts**
- Basic validation rules to flag missing or inconsistent data
- **Full audit log** mapping each populated field to regulatory rule references
- Graceful fallback to deterministic demo mode when live LLM access is unavailable

---

## End-to-End Workflow

The prototype demonstrates the following end-to-end behaviour:

User Question
→ Retrieval of PRA Rulebook & COREP Instructions
→ Structured LLM Output (JSON aligned to COREP schema)
→ COREP Template Extract (Human-Readable)
→ Validation Checks
→ Audit Log (Rule Traceability)


This directly matches the success criteria defined in the problem statement.

---

## How to Run the Project (macOS)

### Prerequisites
- macOS
- Python 3.9 or later
- Git

---

### Step 1: Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
Step 2: Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate
Step 3: Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
Step 4: (Optional) Set OpenAI API key
export OPENAI_API_KEY="your-openai-api-key"
If no API key is provided or API quota is unavailable, the system automatically runs in demo mode using deterministic mock LLM output.

Step 5: Run the application
python main.py
Step 6: Expected Output
COREP C 01.00 – Own Funds (tabular extract)

COREP C 02.00 – Capital Requirements (tabular extract)

Validation checks (if applicable)

Audit log mapping COREP rows to PRA Rulebook and COREP instruction references

Step 7: Deactivate the virtual environment (optional)
deactivate

---

