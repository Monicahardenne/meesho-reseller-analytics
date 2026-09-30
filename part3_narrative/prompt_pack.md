# Reusable Prompt Pack

## Trigger

Run this prompt when a category's `is_flagged()` result is `"flagged"`.

---

## Input List

- {category}
- {previous_revenue}
- {current_revenue}
- {mom_pct}
- {month}
- {prev_month}

---

## Prompt

You are preparing a business update for a regional manager.

Using only the values provided below:

Category: {category}

Previous Month Revenue: {previous_revenue}

Current Month Revenue: {current_revenue}

Month-on-Month Growth (%): {mom_pct}

Current Month: {month}

Previous Month: {prev_month}

Write a short business narrative using this structure:

Context:
Explain what is being measured and over which period.

Insight:
State the exact revenue change and growth percentage as a fact.

Implication:
Provide one actionable recommendation.

Rules:

- Use Context → Insight → Implication structure.
- Never invent any number.
- Never use numbers that are not supplied in the inputs.
- Clearly label facts and hypotheses.
- Keep the language suitable for a regional manager.

---

## Checklist

1. Does every number exactly match a supplied input value?
2. Are all claims clearly identified as fact or hypothesis?
3. Is the recommendation specific and actionable?
4. Are category names and months correct?
5. Are no reseller names included?