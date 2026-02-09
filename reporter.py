def print_report(report, total):
    print(f"\n{report.template}")
    print("-" * 60)
    print("Row   Description                           Amount")
    print("-" * 60)
    for f in report.fields:
        print(f"{f.row:<5} {f.description:<35} {f.amount}")
    print("-" * 60)
    print(f"TOTAL: {total}")
