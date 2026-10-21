
import sqlite3

conn = sqlite3.connect(":memory:")

with open("Projects/EcoPulse/db/schema_and_queries.sql") as f:
    conn.executescript(f.read())

with open("Projects/EcoPulse/db/window_functions.sql") as f:
    conn.executescript(f.read())

print("SQL script executed successfully!")

print("\nEnergy consumption ranking:")
query = """
SELECT user_id,
       SUM(amount) AS total_energy_kwh,
       RANK() OVER (ORDER BY SUM(amount) DESC) AS consumption_rank
FROM user_activities
WHERE category = 'Energy'
GROUP BY user_id
"""
for row in conn.execute(query):
    print(row)

print("\nCategories with no activities:")
query = """
SELECT ec.category_name
FROM energy_categories ec
LEFT JOIN user_activities ua
ON ec.category_name = ua.category
WHERE ua.activity_id IS NULL
"""
for row in conn.execute(query):
    print(row)

conn.close()