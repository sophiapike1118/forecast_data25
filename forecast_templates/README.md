# Forecast Data Analysis & Visualization

## Project Overview

This project uses Python to clean, process, and visualize datasets for exploratory data analysis and comparison. It focuses on preparing data for analysis, handling missing values, and creating visualizations that make patterns and differences easier to identify.

The project includes reusable Python scripts designed to support data preprocessing and exploratory analysis, particularly for datasets involving financial or operational information.

## Technologies Used

- **Python:** Data processing and analysis
- **Pandas:** CSV file manipulation, data cleaning, and DataFrame operations
- **Matplotlib:** Data visualization and plotting
- **Git & GitHub:** Version control and project organization

## Key Features

### 1. Data Cleaning

The `cleaned_nulls.py` script defines a reusable `NullCleaner` class that:

- Imports data from CSV files using Pandas.
- Replaces missing values with zero.
- Stores cleaned data in a DataFrame for further analysis.
- Exports cleaned datasets to a new CSV file.
- Includes error handling and reusable methods.

**Note:** Replacing missing values with zero is appropriate only when zero is a meaningful substitute. Other datasets may require different cleaning strategies.

### 2. Data Visualization

The project includes Python scripts for generating visualizations, including:

- Box plots for exploring data distributions.
- Bar plots for comparing categories.
- Visual comparisons across different groups or time periods.

These visualizations can help identify patterns, differences, and potential outliers.

### 3. Reusable Code

The scripts are organized to support reuse across multiple datasets and analyses. For example, the `NullCleaner` class can be imported into other Python programs without automatically executing its main script.

## Getting Started

**Requirements:**

- Python 3
- Pandas
- Matplotlib

Install the required libraries:

```bash
pip install pandas matplotlib
```

To run the data-cleaning script:

```bash
python cleaned_nulls.py
```

By default, the script reads `dummy_filter_format.csv`, replaces missing values with zero, and saves the result as `updated_nulls.csv`.

To use a different dataset, update the input file path in the script.

## Skills Used

- Python programming and object-oriented design
- Data cleaning and preprocessing
- CSV file manipulation using Pandas
- Exploratory data analysis
- Data visualization
- Writing reusable, documented code
- Version control with Git and GitHub

## Author

**Sophia Pike**

Academic Python Programming & Data Analysis Project | 2025
