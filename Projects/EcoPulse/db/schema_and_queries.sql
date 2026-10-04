-- EcoPulse Database Schema
-- Table: user_activities

CREATE TABLE user_activities (
    activity_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    activity_date DATE NOT NULL,
    category VARCHAR(50) NOT NULL,
    activity_name VARCHAR(100) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    unit VARCHAR(20) NOT NULL,
    carbon_emission_kg DECIMAL(10,2) NOT NULL
);

-- Sample Activity Data

INSERT INTO user_activities
(activity_id, user_id, activity_date, category, activity_name, amount, unit, carbon_emission_kg)
VALUES
(1, 101, '2026-10-01', 'Transport', 'Bus Travel', 10, 'km', 0.50),
(2, 101, '2026-10-01', 'Energy', 'Electricity Usage', 5, 'kWh', 2.00),
(3, 101, '2026-10-02', 'Food', 'Vegetarian Meal', 2, 'meals', 1.20),
(4, 102, '2026-10-02', 'Transport', 'Car Travel', 15, 'km', 3.00),
(5, 102, '2026-10-03', 'Energy', 'Electricity Usage', 8, 'kWh', 3.20),
(6, 103, '2026-10-03', 'Waste', 'Plastic Waste', 2, 'kg', 0.40);

-- Query 1: Display all user activities

SELECT
    user_id,
    activity_date,
    category,
    activity_name,
    carbon_emission_kg
FROM user_activities;

-- Query 2: Total carbon emission by category

SELECT
    category,
    SUM(carbon_emission_kg) AS total_emission_kg
FROM user_activities
GROUP BY category;

-- Query 3: Total carbon emission per user

SELECT
    user_id,
    SUM(carbon_emission_kg) AS total_emission_kg
FROM user_activities
GROUP BY user_id;