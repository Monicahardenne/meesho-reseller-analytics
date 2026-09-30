import csv


def mom_growth(previous: float, current: float) -> float:
    """
    Calculate Month-on-Month growth percentage.
    """
    return round((current - previous) / previous * 100, 2)


def is_flagged(mom_pct: float, threshold: float = 8.0) -> str:
    """
    Return:
    - flagged
    - not_flagged
    - escalate_exact_boundary
    """

    if abs(mom_pct) > threshold:
        return "flagged"

    elif abs(mom_pct) < threshold:
        return "not_flagged"

    else:
        return "escalate_exact_boundary"


def validate_feed(csv_path: str):
    """
    Validate monthly revenue feed.
    """

    errors = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for line_num, row in enumerate(reader, start=2):

            month = row["month"]
            category = row["category"]
            revenue = row["revenue"]

            if not category:
                errors.append(
                    f"line {line_num}: missing category (month={month})"
                )

            if revenue == "":
                errors.append(
                    f"line {line_num}: missing revenue (category={category})"
                )
                continue

            try:
                revenue_value = float(revenue)

                if revenue_value < 0:
                    errors.append(
                        f"line {line_num}: negative revenue ({revenue_value}) for category={category}"
                    )

            except ValueError:
                errors.append(
                    f"line {line_num}: revenue not numeric: {revenue!r}"
                )

    return (len(errors) == 0, errors)