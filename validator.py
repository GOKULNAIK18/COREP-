def validate(report):
    issues = []
    total = 0

    for f in report.fields:
        if "deduction" in f.description.lower() and f.amount > 0:
            issues.append(f"{f.row} must be reported as a deduction.")
        total += f.amount

    if total <= 0:
        issues.append("Computed total must be positive.")

    return issues, total
