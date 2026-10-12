
-- EcoPulse Day 12: SQL JOINs and Window Functions

-- 1. Create a table for energy categories
CREATE TABLE IF NOT EXISTS energy_categories (
    category_id INTEGER PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description VARCHAR(150)
);

-- 2. Insert sample category data
INSERT OR IGNORE INTO energy_categories
(category_id, category_name, description)
VALUES
(1, 'Energy', 'Electricity consumption'),
(2, 'Transport', 'Fuel and travel consumption'),
(3, 'Food', 'Food-related emissions'),
(4, 'Waste', 'Waste-related emissions'),
(5, 'Water', 'Water usage');

-- 3. INNER JOIN: Show activities with matching categories
SELECT
    ua.user_id,
    ua.activity_name,
    ua.category,
    ec.description,
    ua.carbon_emission_kg
FROM user_activities AS ua
INNER JOIN energy_categories AS ec
    ON ua.category = ec.category_name;

-- 4. LEFT JOIN: Show all categories, even without activities
SELECT
    ec.category_name,
    ua.activity_name,
    ua.user_id,
    ua.carbon_emission_kg
FROM energy_categories AS ec
LEFT JOIN user_activities AS ua
    ON ec.category_name = ua.category;

-- 5. RANK(): Rank users by total energy consumption
SELECT
    user_id,
    SUM(amount) AS total_energy_kwh,
    RANK() OVER (
        ORDER BY SUM(amount) DESC
    ) AS consumption_rank
FROM user_activities
WHERE category = 'Energy'
GROUP BY user_id;