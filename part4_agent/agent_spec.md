# Agent Specification

## Goal

Keep Meesho category managers informed of any category whose month-on-month revenue changes by more than the 8% threshold, with all messages drafted and held for human approval.

---

## Tools

The agent uses:

- validate_feed()
- mom_growth()
- is_flagged()
- Prompt Pack Template

---

## Memory / State

The agent must remember:

- Previous month revenue
- Current month revenue
- Category names
- Flagging decisions
- Validation results

---

## Planner

1. Load monthly revenue feed
2. Run validate_feed()
3. Hard Stop if validation fails
4. Compute month-on-month growth
5. Run is_flagged()
6. Sort flagged categories by absolute growth
7. Draft messages for top 3 flagged categories
8. Suppress remaining flagged categories
9. Escalate exact-boundary categories
10. Produce JSON output

---

## Feedback Loop

All drafted messages are held for human approval.

No message is automatically sent.

---

# Guardrails

## Input Guardrail

validate_feed() must pass before any analysis begins.

## Action Guardrail

Messages are drafted only and never auto-sent.

## Output Guardrail

Every value in a message must come directly from validated Part 1 or Part 2 calculations.

---

# Success Condition

Validation succeeds and drafts are generated with traceable calculations.

---

# Error Condition

Validation fails.

The workflow performs a Hard Stop and returns validation errors.

---

# Given-When-Then Specifications

## Scenario 1

Given Ethnic Wear revenue increases from 104520.77 to 185107.61

When growth is calculated

Then growth equals 77.1 and status equals flagged.

---

## Scenario 2

Given Beauty & Personal Care revenue increases from 35542.11 to 37559.07

When growth is calculated

Then growth equals 5.67 and status equals not_flagged.

---

## Scenario 3

Given previous=100000 and current=108000

When growth is calculated

Then growth equals 8.0 and status equals escalate_exact_boundary.

---

## Scenario 4

Given corrupted_feed.csv

When validate_feed() runs

Then validation fails with exactly three validation errors.