"""
File: box_plot_two.py
Author: Sophia Pike
Date: June 25, 2025

Description:
-------------
This script loads financial data from a CSV file and allows the user to:
1. View available companies and financial metrics
2. Select two companies to compare
3. Choose a metric for comparison
4. Generate and save a side-by-side boxplot comparing the selected metric for both companies
5. Print the average value of that metric for both companies

Instructions:
-------------
1. Place your cleaned CSV file (e.g., 'Financial_Statements.csv') in the same directory
2. Run this script using a Python environment with matplotlib and pandas installed
"""

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
file_path = "Financial_Statements.csv"
df = pd.read_csv(file_path)
df.columns = df.columns.str.strip()  # Strip whitespace from column names

# Step 2: Display available columns and companies
print("\nAvailable columns in the dataset:")
print(list(df.columns))

# Check for 'Company' column
if 'Company' not in df.columns:
    raise ValueError("Dataset must contain a 'Company' column for this script to work.")

# Show available companies
companies = df['Company'].dropna().unique()
print("\nAvailable companies:")
for c in companies:
    print(f"- {c}")

# Show available financial metrics
numeric_columns = df.select_dtypes(include='number').columns.tolist()
print("\nAvailable numeric financial metrics:")
for col in numeric_columns:
    print(f"- {col}")

# Step 3: User input
company1 = input("\nEnter the name of the first company: ").strip()
company2 = input("Enter the name of the second company: ").strip()
metric = input("Enter the name of the financial metric to compare: ").strip()

# Step 4: Validate
if company1 not in companies or company2 not in companies:
    raise ValueError("One or both company names are invalid. Please check spelling and try again.")

if metric not in df.columns:
    raise ValueError(f"'{metric}' is not a valid column in the dataset.")

# Step 5: Get data
data1 = df[df['Company'] == company1][metric].dropna()
data2 = df[df['Company'] == company2][metric].dropna()

# Step 6: Print numeric averages
avg1 = data1.mean()
avg2 = data2.mean()

print(f"\nAverage {metric} for {company1}: {avg1:,.2f}")
print(f"Average {metric} for {company2}: {avg2:,.2f}")

# Step 7: Plot
plt.figure(figsize=(10, 6))
box = plt.boxplot([data1, data2],
                  patch_artist=True,
                  tick_labels=[company1, company2],
                  medianprops=dict(color='black'))

# Set colors: first company = lightblue, second = lightcoral
box['boxes'][0].set_facecolor('lightblue')
box['boxes'][1].set_facecolor('lightcoral')

plt.title(f"Comparison of {metric} Between {company1} and {company2}")
plt.ylabel(metric)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("company_metric_comparison.png", dpi=300)
plt.show()
