# Meesho Reseller Analytics Project

## Overview

This project analyses reseller and order data generated from a seeded dataset and implements a complete reporting workflow consisting of:

- SQL analytics
- Growth monitoring engine
- Narrative generation
- Agent workflow simulation

No external APIs or API keys are required.

---

# Project Structure

```text
data/
part1_sql/
part2_engine/
part3_narrative/
part4_agent/
README.md
```

---

# How To Run

## Step 1 - Generate Dataset

```bash
python data/generate_dataset.py
```

Creates:

- resellers.csv
- orders.csv
- meesho_reseller.db

---

## Step 2 - Run SQL Analytics

```bash
python part1_sql/queries.py
```

Generates:

- monthly_category_revenue.csv
- region_wise_revenue.csv
- top_resellers.csv
- no_order_resellers.csv
- count_proof.csv
- june_aov.csv

---

## Step 3 - Run Tests

```bash
python part2_engine/test_growth_engine.py
```

Runs:

- mom_growth tests
- is_flagged tests
- feed validation tests

---

## Step 4 - Narrative Components

Contents:

- prompt_pack.md
- narrative_report.md
- masking.py

Run:

```bash
python part3_narrative/masking.py
```

---

## Step 5 - Agent Workflow

Run:

```bash
python part4_agent/mock_agent_runner.py
```

Produces structured JSON output.

---

# Workflow Mapping

## Part 1

SQL generates trusted business metrics from raw data.

## Part 2

Python engine validates inputs and calculates growth indicators.

## Part 3

Narrative layer converts verified metrics into stakeholder-ready insights.

## Part 4

Agent workflow simulates an automated monitoring and reporting process.

---

# Technology

- Python
- SQLite
- Pandas
- Markdown

---

# API Keys

No API keys are required.

The entire solution runs locally using generated data and Python.