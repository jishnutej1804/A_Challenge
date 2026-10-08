# EcoPulse - Carbon Emission Exploratory Data Analysis
# Tool: Pandas
# Purpose: Analyze sample energy and waste activity data

import pandas as pd


# Sample dataset
data = {
    "category": [
        "Energy", "Energy", "Energy",
        "Waste", "Waste", "Waste",
        "Transport", "Transport", "Transport"
    ],
    "activity": [
        "Electricity", "LPG", "Electricity",
        "Plastic", "Food Waste", "Plastic",
        "Car", "Bus", "Car"
    ],
    "amount": [
        80, 4, 60,
        5, 10, 3,
        100, 50, 80
    ],
    "unit": [
        "kWh", "kg", "kWh",
        "kg", "kg", "kg",
        "km", "km", "km"
    ],
    "carbon_emission_kg": [
        56.0, 12.0, 42.0,
        2.5, 5.0, 1.5,
        17.0, 3.0, 13.6
    ]
}

df = pd.DataFrame(data)


# Display the dataset
print("=== EcoPulse Carbon Dataset ===")
print(df)


# Summary statistics
print("\n=== Summary Statistics ===")
print(df.describe())


# Total emissions by category
print("\n=== Emissions by Category ===")
category_emissions = df.groupby("category")["carbon_emission_kg"].sum()
print(category_emissions)


# Average emission by category
print("\n=== Average Emission by Category ===")
category_average = df.groupby("category")["carbon_emission_kg"].mean()
print(category_average)