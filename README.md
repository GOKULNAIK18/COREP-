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


