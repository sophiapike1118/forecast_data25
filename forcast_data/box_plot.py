"""
File: box_plot.py
Author: Sophia Pike
Date: June 17th, 2025

Description:
-------------
This script generates a box plot visualization using cleaned data imported from the `NullCleaner` class
defined in `cleaned_nulls.py`.

The plot focuses only on rows where `category == 1` (e.g., a specific group of employees or metric type).
It then aggregates all values — across all employees, job codes, and groups — to show the distribution
of data over time.

This is useful for:
- Understanding overall trends or outliers in a specific category
- Summarizing large time-series datasets for quick visual analysis

What this file does:
---------------------
1. Imports and uses the `NullCleaner` class to load and clean the data
2. Filters the cleaned data to only include rows where `category == 1`
3. Sums values across all employees, job codes, and groups for each time column
4. Creates and saves a box plot showing the distribution of values across years

Intended Users:
---------------
This script is intended for analysts or staff who want a quick visual summary of data in category 1 for each year.

How to use:
------------
Just run this file. It will clean the data, filter it, and create a box plot using matplotlib.
The resulting image will be saved as 'box_plot.png'.

"""

import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict
from cleaned_nulls import NullCleaner

# Step 1: Load and clean the data
file_path = "dummy_filter_format.csv"
cleaner = NullCleaner(file_path)
cleaner.clean_nulls()
df = cleaner.cleaned_df

# Step 2: Filter for category == 1
df_filtered = df[df["category"] == 1]

# Step 3: Drop non-numeric columns
non_data_columns = ["group", "category", "job_code"]
data_only = df_filtered.drop(columns=non_data_columns)

# Step 4: Group column values by year
year_data = defaultdict(list)

for col in data_only.columns:
    try:
        year = col.split("_")[0]
        year_data[year].extend(data_only[col].dropna().tolist())
    except IndexError:
        continue

# Step 5: Create box plot for each year
plt.figure(figsize=(10, 6))
plt.boxplot(
    [year_data[y] for y in sorted(year_data)],
    tick_labels=sorted(year_data),
    patch_artist=True
)
plt.title("Yearly Distribution of Values (Category = 1)")
plt.xlabel("Year")
plt.ylabel("Value")
plt.tight_layout()
plt.savefig("box_plot_by_year.png", dpi=300)
plt.show()


# --- Graph Two: Compare Two Groups Across Years with Contrasting Colors ---
import seaborn as sns  # Optional: for nicer colors

# Step A: Prompt for two groups
available_groups = df_filtered["group"].unique()
print("Available groups to graph:", list(available_groups))

group_1 = input("Enter the first group to compare: ").strip()
group_2 = input("Enter the second group to compare: ").strip()

if group_1 not in available_groups or group_2 not in available_groups:
    print("One or both group names are invalid. Please check the group names and try again.")
else:
    # Step B: Filter data for the two groups
    group1_df = df_filtered[df_filtered["group"] == group_1]
    group2_df = df_filtered[df_filtered["group"] == group_2]

    def get_yearly_data(df_group):
        yearly = defaultdict(list)
        for col in df_group.drop(columns=non_data_columns).columns:
            try:
                year = col.split("_")[0]
                yearly[year].extend(df_group[col].dropna().tolist())
            except IndexError:
                continue
        return yearly

    group1_year_data = get_yearly_data(group1_df)
    group2_year_data = get_yearly_data(group2_df)
    all_years = sorted(set(group1_year_data.keys()) | set(group2_year_data.keys()))

    # Step C: Plot the two groups
    plt.figure(figsize=(10, 6))
    positions_1 = [i - 0.2 for i in range(1, len(all_years)+1)]
    positions_2 = [i + 0.2 for i in range(1, len(all_years)+1)]

    plt.boxplot(
        [group1_year_data.get(y, []) for y in all_years],
        positions=positions_1,
        widths=0.3,
        patch_artist=True,
        boxprops=dict(facecolor='lightcoral', color='red'),
        medianprops=dict(color='black'),
        whiskerprops=dict(color='red'),
        capprops=dict(color='red'),
        flierprops=dict(markerfacecolor='lightcoral', marker='o', markersize=4, linestyle='none', markeredgecolor='red')
    )

    plt.boxplot(
        [group2_year_data.get(y, []) for y in all_years],
        positions=positions_2,
        widths=0.3,
        patch_artist=True,
        boxprops=dict(facecolor='mediumseagreen', color='darkgreen'),
        medianprops=dict(color='black'),
        whiskerprops=dict(color='darkgreen'),
        capprops=dict(color='darkgreen'),
        flierprops=dict(markerfacecolor='mediumseagreen', marker='o', markersize=4, linestyle='none', markeredgecolor='darkgreen')
    )

    plt.xticks(range(1, len(all_years)+1), all_years)
    plt.title(f"Yearly Comparison: {group_1} vs {group_2}")
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.legend([f"{group_1}", f"{group_2}"], loc="upper right")
    plt.tight_layout()
    plt.savefig("group_comparison_by_year.png", dpi=300)
    plt.show()