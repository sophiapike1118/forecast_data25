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
4. Creates and saves a box plot showing the distribution of values across months

Intended Users:
---------------
This script is intended for analysts or staff who want a quick visual summary of data in category 1.

How to use:
------------
Just run this file. It will clean the data, filter it, and create a box plot using matplotlib.
The resulting image will be saved as 'box_plot.png'.

"""

import matplotlib.pyplot as plt
from cleaned_nulls import NullCleaner


# Step 1: Load and clean the data using the NullCleaner class
file_path = "dummy_filter_format.csv"  # Replace with your actual file name
cleaner = NullCleaner(file_path)
cleaner.clean_nulls()
df = cleaner.cleaned_df

# Step 2: Filter the data where category == 1
df_filtered = df[df["category"] == 1]

# Step 3: Drop non-numeric columns so we can sum across them
non_data_columns = ["group", "category", "job_code"]
data_only = df_filtered.drop(columns=non_data_columns)

# Step 4: Prepare the data for box plot by transposing it so each column becomes a time period
# and each row is a different employee/job/group's value for that period
data_for_plot = data_only.transpose()
data_for_plot.index.name = "Date"

# Step 5: Create the box plot
plt.figure(figsize=(12, 6))
plt.boxplot(
    data_for_plot.transpose().values,
    tick_labels=data_for_plot.index,
    vert=True,
    patch_artist=True
)
plt.xticks(rotation=90)
plt.title("Distribution of Values Over Time (Category = 1)")
plt.ylabel("Value")
plt.xlabel("Time Period")
plt.tight_layout()

# Step 6: Save the plot
plt.savefig("box_plot.png", dpi=300)

# Step 7: Show the plot
plt.show()
