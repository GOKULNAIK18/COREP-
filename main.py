from schema import CorepField, CorepReport
from retriever import retrieve_relevant_text
from llm_engine import generate_corep
from validator import validate
from reporter import print_report
from audit import print_audit

def load_documents():
    docs = []
    for file in [
        "data/pra_rulebook.txt",
        "data/corep_c01_instructions.txt",
        "data/corep_c02_instructions.txt",
    ]:
        with open(file) as f:
            docs.extend([p for p in f.read().split("\n\n") if p.strip()])
    return docs

def run(template_name):
    question = f"How should {template_name} be reported for a UK bank?"
    scenario = """
    Share capital: 100
    Retained earnings: 40
    Intangible assets: 10
    Risk exposure amount: 800
    """

    documents = load_documents()
    regulatory_text = retrieve_relevant_text(question, documents)

    prompt = f"""
Regulatory Text:
{regulatory_text}

Scenario:
{scenario}

Return STRICT JSON aligned to COREP schema.
"""

    output = generate_corep(prompt, template_name)


    report = CorepReport(
        template=output["template"],
        fields=[CorepField(**f) for f in output["fields"]]
    )

    issues, total = validate(report)
    print_report(report, total)

    if issues:
        print("\nVALIDATION ISSUES")
        for i in issues:
            print("-", i)

    print_audit(report)

if __name__ == "__main__":
    run("COREP C 01.00 – Own Funds")
    run("COREP C 02.00 – Capital Requirements")
