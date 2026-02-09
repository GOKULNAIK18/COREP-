# import openai
# import json
# import os

# openai.api_key = os.getenv("OPENAI_API_KEY")

# def generate_corep(prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": "You are a regulatory reporting assistant."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0
#     )
#     return json.loads(response.choices[0].message.content)

# import os
# import json
# from openai import OpenAI

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def generate_corep(prompt: str) -> dict:
#     """
#     Calls GPT-4o and expects STRICT JSON output aligned to COREP schema.
#     """

#     response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {
#                 "role": "system",
#                 "content": (
#                     "You are a PRA regulatory reporting assistant. "
#                     "You must respond ONLY with valid JSON. "
#                     "Do not include explanations or extra text."
#                 ),
#             },
#             {
#                 "role": "user",
#                 "content": prompt,
#             },
#         ],
#         temperature=0,
#     )

#     content = response.choices[0].message.content

#     try:
#         return json.loads(content)
#     except json.JSONDecodeError:
#         raise ValueError(
#             "LLM response was not valid JSON. Response was:\n" + content
#         )

import os
import json
from openai import OpenAI, OpenAIError, RateLimitError

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def _mock_corep_response(template_name: str) -> dict:
    print("\n[INFO] Running in DEMO MODE (mock LLM output)\n")

    if "C 01.00" in template_name:
        return {
            "template": "COREP C 01.00 – Own Funds",
            "fields": [
                {
                    "row": "010",
                    "description": "Share capital",
                    "amount": 100,
                    "rule_reference": "PRA Rulebook Art. 26; COREP C01 Row 010"
                },
                {
                    "row": "020",
                    "description": "Retained earnings",
                    "amount": 40,
                    "rule_reference": "PRA Rulebook Art. 26; COREP C01 Row 020"
                },
                {
                    "row": "060",
                    "description": "Intangible assets (deduction)",
                    "amount": -10,
                    "rule_reference": "PRA Rulebook Art. 36; COREP C01 Row 060"
                }
            ]
        }

    return {
        "template": "COREP C 02.00 – Capital Requirements",
        "fields": [
            {
                "row": "010",
                "description": "Total risk exposure amount",
                "amount": 800,
                "rule_reference": "PRA Rulebook Art. 92; COREP C02 Row 010"
            },
            {
                "row": "020",
                "description": "CET1 capital requirement",
                "amount": 52,
                "rule_reference": "COREP C02 Instructions"
            },
            {
                "row": "030",
                "description": "Total capital requirement",
                "amount": 96,
                "rule_reference": "COREP C02 Instructions"
            }
        ]
    }

def generate_corep(prompt: str, template_name: str) -> dict:
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a PRA regulatory reporting assistant. "
                        "Respond ONLY with valid JSON aligned to the COREP schema."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0,
        )

        return json.loads(response.choices[0].message.content)

    except (RateLimitError, OpenAIError):
        return _mock_corep_response(template_name)
