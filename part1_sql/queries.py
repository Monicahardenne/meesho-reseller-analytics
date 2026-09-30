import sqlite3
import pandas as pd
import os

# Connect to database
db_path = "data/meesho_reseller.db"
conn = sqlite3.connect(db_path)

# Query 1: Monthly Revenue by Category
query = """
SELECT
    month,
    category,
    ROUND(SUM(quantity * unit_price), 2) AS revenue,
    COUNT(*) AS n_orders
FROM orders
GROUP BY month, category
ORDER BY
    CASE month
        WHEN 'April' THEN 1
        WHEN 'May' THEN 2
        WHEN 'June' THEN 3
    END,
    category;
"""

df = pd.read_sql_query(query, conn)

# Create output folder if it doesn't exist
os.makedirs("output", exist_ok=True)

# Save CSV
df.to_csv(
    "part1_sql/output/monthly_category_revenue.csv",
    index=False
)

print(df)
print("\nCSV saved successfully!")

# Query 2: Region-wise total revenue and order count

query2 = """
SELECT
    r.region,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS revenue,
    COUNT(*) AS order_count
FROM orders o
JOIN resellers r
ON o.reseller_id = r.reseller_id
GROUP BY r.region
ORDER BY revenue DESC;
"""

region_df = pd.read_sql_query(query2, conn)

region_df.to_csv(
    "part1_sql/output/region_wise_revenue.csv",
    index=False
)

print("\nRegion Wise Revenue")
print(region_df)

# Query 3: Top Resellers by Total Spend

query3 = """
SELECT
    r.reseller_id,
    r.reseller_name,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS total_spend
FROM orders o
JOIN resellers r
ON o.reseller_id = r.reseller_id
GROUP BY r.reseller_id, r.reseller_name
HAVING total_spend > 50000
ORDER BY total_spend DESC
LIMIT 5;
"""

top_reseller_df = pd.read_sql_query(query3, conn)

top_reseller_df.to_csv(
    "part1_sql/output/top_resellers.csv",
    index=False
)

print("\nTop Resellers")
print(top_reseller_df)

# Query 4: Resellers with No Orders

query4 = """
SELECT
    r.reseller_id,
    r.reseller_name,
    r.region
FROM resellers r
LEFT JOIN orders o
ON r.reseller_id = o.reseller_id
WHERE o.order_id IS NULL;
"""

no_order_df = pd.read_sql_query(query4, conn)

no_order_df.to_csv(
    "part1_sql/output/no_order_resellers.csv",
    index=False
)

print("\nResellers With No Orders")
print(no_order_df)

# Query 4B: COUNT(*) vs COUNT(order_id) Proof

query4b = """
SELECT
    r.reseller_id,
    COUNT(*) AS count_star,
    COUNT(o.order_id) AS count_order_id
FROM resellers r
LEFT JOIN orders o
ON r.reseller_id = o.reseller_id
WHERE r.reseller_id = 'RS024'
GROUP BY r.reseller_id;
"""

proof_df = pd.read_sql_query(query4b, conn)

proof_df.to_csv(
    "part1_sql/output/count_proof.csv",
    index=False
)

print("\nCOUNT Proof")
print(proof_df)
# Query 5: June Delivered AOV

query5 = """
SELECT
    ROUND(
        SUM(quantity * unit_price) / COUNT(*),
        2
    ) AS aov
FROM orders
WHERE month = 'June'
AND status = 'Delivered';
"""

aov_df = pd.read_sql_query(query5, conn)

aov_df.to_csv(
    "part1_sql/output/june_aov.csv",
    index=False
)

print("\nJune Delivered AOV")
print(aov_df)

conn.close()
