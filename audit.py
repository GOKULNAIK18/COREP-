def print_audit(report):
    print("\nAUDIT LOG – RULE TRACEABILITY")
    print("-" * 60)
    for f in report.fields:
        print(f"Row {f.row}: {f.description}")
        print(f"Rule Source: {f.rule_reference}\n")
