# forcast_data

This project analyzes forecasting data using cleaned time-series values.

## Features
- Replaces missing values with 0 using `cleaned_nulls.py`
- Filters and visualizes data using `box_plot.py` (category = 1)
- Designed to be reusable for analysts, especially in finance contexts

## Getting Started
1. Ensure `pandas` and `matplotlib` are installed
2. Run `cleaned_nulls.py` to clean your input CSV
3. Run `box_plot.py` to generate a box plot of cleaned data
4. Output will be saved as `updated_nulls.csv` and `box_plot.png`

## Author
Sophia Pike
