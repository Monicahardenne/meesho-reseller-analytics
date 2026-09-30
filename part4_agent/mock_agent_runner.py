import json
import pandas as pd
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from part2_engine.growth_engine import (
    validate_feed,
    mom_growth,
    is_flagged
)


def run(month: str, csv_path: str):

    valid, errors = validate_feed(csv_path)

    if not valid:
        return {
            "run_month": month,
            "validation_status": "invalid",
            "validation_errors": errors,
            "flagged_categories": [],
            "suppressed_categories": [],
            "escalated_categories": [],
            "action_taken": "hard_stop"
        }

    df = pd.read_csv(csv_path)

    months = ["April", "May", "June"]

    if month not in months or month == "April":
        raise ValueError(
            "Use May or June for comparison runs."
        )

    current_idx = months.index(month)
    previous_month = months[current_idx - 1]

    current_df = df[df["month"] == month]
    previous_df = df[df["month"] == previous_month]

    flagged_categories = []
    suppressed_categories = []
    escalated_categories = []

    for category in current_df["category"]:

        current_rev = float(
            current_df[
                current_df["category"] == category
            ]["revenue"].iloc[0]
        )

        previous_rev = float(
            previous_df[
                previous_df["category"] == category
            ]["revenue"].iloc[0]
        )

        growth = mom_growth(
            previous_rev,
            current_rev
        )

        status = is_flagged(growth)

        if status == "flagged":
            flagged_categories.append({
                "category": category,
                "mom_pct": growth,
                "previous_revenue": previous_rev,
                "current_revenue": current_rev
            })

        elif status == "escalate_exact_boundary":
            escalated_categories.append(category)

    flagged_categories.sort(
        key=lambda x: abs(x["mom_pct"]),
        reverse=True
    )

    drafted = flagged_categories[:3]
    suppressed = flagged_categories[3:]

    for item in drafted:

        item["drafted"] = True

        item["message"] = (
            f"{item['category']} changed by "
            f"{item['mom_pct']}% from "
            f"{previous_month} to {month}."
        )

    suppressed_categories = [
        item["category"]
        for item in suppressed
    ]

    result = {
        "run_month": month,
        "validation_status": "valid",
        "validation_errors": [],
        "flagged_categories": drafted,
        "suppressed_categories": suppressed_categories,
        "escalated_categories": escalated_categories,
        "action_taken": "drafted_and_held_for_approval"
    }

    return result


if __name__ == "__main__":

    result = run(
        "May",
        "part2_engine/fixtures/monthly_category_revenue.csv"
    )

    print(
        json.dumps(
            result,
            indent=4
        )
    )