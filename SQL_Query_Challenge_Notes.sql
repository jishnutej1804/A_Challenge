-- Day 18: SQL Query Design Challenge
-- Topics: GROUP BY, HAVING, Self-Joins, E-commerce, Sustainability
-- Dialect: PostgreSQL

-- ============================================================
-- 1. E-COMMERCE SCHEMA
-- ============================================================

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    referred_by INT REFERENCES customers(customer_id)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customers(customer_id),
    order_date DATE NOT NULL,
    total_amount NUMERIC(12, 2) NOT NULL CHECK (total_amount >= 0)
);

CREATE TABLE monthly_emissions (
    month_start DATE PRIMARY KEY,
    emissions_kg NUMERIC(14, 2) NOT NULL CHECK (emissions_kg >= 0)
);

-- ============================================================
-- 2. HAVING: CUSTOMERS WITH HIGH-VALUE PURCHASES
-- Find customers whose total spending exceeds 1,000.
-- ============================================================

SELECT
    c.customer_id,
    c.customer_name,
    SUM(o.total_amount) AS total_spent
FROM customers AS c
JOIN orders AS o
    ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING SUM(o.total_amount) > 1000
ORDER BY total_spent DESC;

-- Why HAVING?
-- WHERE filters individual rows before aggregation.
-- HAVING filters groups after GROUP BY.

-- ============================================================
-- 3. HAVING: MONTHS WITH HIGH SALES
-- Find months with at least 50 orders and revenue above 10,000.
-- ============================================================

SELECT
    DATE_TRUNC('month', order_date)::DATE AS month_start,
    COUNT(*) AS order_count,
    SUM(total_amount) AS monthly_revenue
FROM orders
GROUP BY DATE_TRUNC('month', order_date)::DATE
HAVING COUNT(*) >= 50
   AND SUM(total_amount) > 10000
ORDER BY month_start;

-- ============================================================
-- 4. SELF-JOIN: CUSTOMER REFERRALS
-- Show each customer and the customer who referred them.
-- ============================================================

SELECT
    referred.customer_id,
    referred.customer_name,
    referrer.customer_name AS referred_by_name
FROM customers AS referred
LEFT JOIN customers AS referrer
    ON referred.referred_by = referrer.customer_id
ORDER BY referred.customer_id;

-- A self-join joins a table to itself using different aliases.
-- LEFT JOIN preserves customers who have no referrer.

-- ============================================================
-- 5. SELF-JOIN: CUSTOMERS WITH THE SAME REFERRER
-- Return each distinct pair once.
-- ============================================================

SELECT
    a.customer_name AS customer_a,
    b.customer_name AS customer_b,
    a.referred_by AS referrer_id
FROM customers AS a
JOIN customers AS b
    ON a.referred_by = b.referred_by
   AND a.customer_id < b.customer_id
WHERE a.referred_by IS NOT NULL
ORDER BY referrer_id, customer_a, customer_b;

-- The less-than condition avoids duplicate pairs and self-pairs.

-- ============================================================
-- 6. SUSTAINABILITY: MONTH-OVER-MONTH EMISSIONS REDUCTION
-- Compare each month with the previous calendar month.
-- Positive reduction means emissions decreased.
-- ============================================================

WITH monthly_comparison AS (
    SELECT
        month_start,
        emissions_kg,
        LAG(month_start) OVER (ORDER BY month_start) AS previous_month,
        LAG(emissions_kg) OVER (ORDER BY month_start) AS previous_emissions_kg
    FROM monthly_emissions
)
SELECT
    month_start,
    emissions_kg,
    previous_month,
    previous_emissions_kg,
    previous_emissions_kg - emissions_kg AS reduction_kg,
    ROUND(
        100.0 * (previous_emissions_kg - emissions_kg)
        / NULLIF(previous_emissions_kg, 0),
        2
    ) AS reduction_percentage
FROM monthly_comparison
WHERE previous_month = (month_start - INTERVAL '1 month')::DATE
ORDER BY month_start;

-- LAG accesses the preceding available row.
-- The WHERE condition ensures it is the previous calendar month,
-- not merely the previous recorded month.
-- NULLIF prevents division by zero.
-- The first month has no prior month and is excluded.

-- ============================================================
-- 7. SUSTAINABILITY: MONTHS WITH AT LEAST 5% REDUCTION
-- ============================================================

WITH monthly_comparison AS (
    SELECT
        month_start,
        emissions_kg,
        LAG(month_start) OVER (ORDER BY month_start) AS previous_month,
        LAG(emissions_kg) OVER (ORDER BY month_start) AS previous_emissions_kg
    FROM monthly_emissions
),
reductions AS (
    SELECT
        month_start,
        emissions_kg,
        previous_month,
        previous_emissions_kg,
        100.0 * (previous_emissions_kg - emissions_kg)
            / NULLIF(previous_emissions_kg, 0) AS reduction_percentage
    FROM monthly_comparison
    WHERE previous_month = (month_start - INTERVAL '1 month')::DATE
)
SELECT
    month_start,
    previous_emissions_kg,
    emissions_kg,
    ROUND(reduction_percentage, 2) AS reduction_percentage
FROM reductions
WHERE reduction_percentage >= 5
ORDER BY month_start;

-- ============================================================
-- 8. INTERPRETATION EXAMPLE
-- Previous month: 1,000 kg CO2e
-- Current month:    850 kg CO2e
-- Reduction:        150 kg CO2e
-- Reduction rate:   (1,000 - 850) / 1,000 * 100 = 15%
--
-- If emissions increase, reduction_percentage becomes negative.
-- A missing month is not treated as a valid month-over-month pair.
-- ============================================================
