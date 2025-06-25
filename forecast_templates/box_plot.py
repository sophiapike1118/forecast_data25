"""
File: box_plot.py
Author: Sophia Pike
Date: June 20th, 2025

Description:
-------------
This script generates two visualizations using cleaned data imported from the `NullCleaner` class
defined in `cleaned_nulls.py`.

Graph 1: Total Value by Job Code (Category = 1)
------------------------------------------------
- Filters the cleaned dataset to only include rows where `category == 1`
- Aggregates total values across all time periods for each job code
- Creates a bar chart showing the total value per job code

Graph 2: Comparison of Two Groups by Job Code
---------------------------------------------
- Prompts the user to select two group names
- Filters data for each group where `category == 1`
- Aggregates total values across all time periods for each job code within each group
- Plots a side-by-side bar chart comparing the two groups by job code using contrasting colors

These visualizations help analysts explore how different job codes contribute to total values
and compare performance across different employee groups.

How to use:
------------
Just run this file. It will:
1. Clean the data using `NullCleaner`
2. Generate the two plots (saving them as PNGs)
3. Prompt user input for group comparison in Graph 2

"""

import matplotlib.pyplot as plt
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

# --- Graph 1: Total Value by Job Code ---

jobcode_data = df_filtered.groupby("job_code").sum(numeric_only=True)
jobcode_totals = jobcode_data.sum(axis=1)

plt.figure(figsize=(12, 6))
jobcode_totals.plot(kind='bar', color='skyblue')
plt.title("Total Value by Job Code (Category = 1)")
plt.xlabel("Job Code")
plt.ylabel("Total Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_plot_by_jobcode.png", dpi=300)
plt.show()

# --- Graph 2: Compare Two Groups by Job Code ---

available_groups = df_filtered["group"].unique()
print("Available groups to graph:", list(available_groups))

group_1 = input("Enter the first group to compare: ").strip()
group_2 = input("Enter the second group to compare: ").strip()

if group_1 not in available_groups or group_2 not in available_groups:
    print("One or both group names are invalid. Please check the group names and try again.")
else:
    group1_df = df_filtered[df_filtered["group"] == group_1]
    group2_df = df_filtered[df_filtered["group"] == group_2]

    group1_job_totals = group1_df.groupby("job_code").sum(numeric_only=True).sum(axis=1)
    group2_job_totals = group2_df.groupby("job_code").sum(numeric_only=True).sum(axis=1)

    all_job_codes = sorted(set(group1_job_totals.index) | set(group2_job_totals.index))
    group1_vals = [group1_job_totals.get(code, 0) for code in all_job_codes]
    group2_vals = [group2_job_totals.get(code, 0) for code in all_job_codes]

    x = range(len(all_job_codes))
    width = 0.35

    plt.figure(figsize=(12, 6))
    plt.bar([i - width/2 for i in x], group1_vals, width=width, label=group_1, color='lightcoral')
    plt.bar([i + width/2 for i in x], group2_vals, width=width, label=group_2, color='mediumseagreen')
    plt.xticks(ticks=x, labels=all_job_codes, rotation=45)
    plt.title(f"Total Value by Job Code: {group_1} vs {group_2}")
    plt.xlabel("Job Code")
    plt.ylabel("Total Value")
    plt.legend()
    plt.tight_layout()
    plt.savefig("group_comparison_by_jobcode.png", dpi=300)
    plt.show()
