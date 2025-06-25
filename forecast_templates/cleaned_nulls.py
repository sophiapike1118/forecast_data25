"""
File: cleaned_nulls.py
Author: Sophia Pike
Date: June 17th, 2025

Description:
-------------
This Python module defines a class called `NullCleaner` used to clean data by replacing all null (missing) values
in a CSV file with zeroes. This is useful when working with time-series or categorical data that may have gaps
in reporting or missing entries.

The class is designed for reuse in other Python scripts or Jupyter notebooks and can be imported like any other module.

What this file does:
---------------------
1. Loads a CSV file into memory.
2. Replaces all null or missing values with 0.
3. Stores the cleaned data in memory for use in other programs.
4. Provides a method to save the cleaned data to a new CSV file called `updated_nulls.csv`.
5. Prints a confirmation message so the user knows the cleaning process was completed.

Intended Users:
---------------
This script is built for users like financial analysts or operations staff who want to preprocess datasets before
analysis or visualization, without needing to write their own data-cleaning code.

How to use:
------------
Option 1: Run the script directly to clean a CSV and save the updated file.
Option 2: Import the `NullCleaner` class in another file to reuse the cleaning logic across multiple scripts without duplicating code.

Returns:
--------
- Cleaned DataFrame with nulls replaced by 0
- Saves a file named `updated_nulls.csv` containing the cleaned data

# ----------------------------------------------------------------------------------
# NOTE FOR REUSE:
# This file can be run directly to clean a CSV file. By default, it uses a file named
# "dummy_filter_format.csv", but you can change this to any CSV file you want to clean.
#
# When you run the cleaning process, the class will automatically:
#   - Replace all null values with 0
#   - Store the cleaned data as a DataFrame
#   - Save a new CSV file called "updated_nulls.csv" in the same folder
#
# To reuse this code in another Python script:
#
# 1. Import the class:
#       from cleaned_nulls import NullCleaner
#
# 2. Create an instance of the class with your own CSV file:
#       cleaner = NullCleaner("your_file_name.csv")
#
# 3. Clean the data (this will also automatically save to 'updated_nulls.csv'):
#       cleaner.clean_nulls()
#
# 4. Access the cleaned DataFrame for further use (e.g., plotting or analysis):
#       df = cleaner.cleaned_df
#
# The code at the bottom of this file will NOT run when the file is imported.
# It only runs if this file is opened and executed directly.
# ----------------------------------------------------------------------------------

"""

import pandas as pd


class NullCleaner:
    def __init__(self, file_path):
        """
        Initializes the NullCleaner with a path to the CSV file.

        Parameters:
        ------------
        file_path : str
            The file path to the CSV you want to clean.
        """
        self.file_path = file_path
        self.cleaned_df = None

    def clean_nulls(self):
        """
        Loads the CSV and replaces all null values with 0.
        Automatically saves the cleaned data to 'updated_nulls.csv'.

        After running this, the cleaned DataFrame is stored in `self.cleaned_df`.
        """
        try:
            df = pd.read_csv(self.file_path)
            self.cleaned_df = df.fillna(0)
            self.cleaned_df.to_csv("updated_nulls.csv", index=False)
            print("Null values successfully replaced with 0.")
            print("Cleaned data saved to 'updated_nulls.csv'.")
        except Exception as e:
            print(f"Error cleaning nulls: {e}")

    def save_cleaned_data(self, output_path="updated_nulls.csv"):
        """
        Saves the cleaned DataFrame to a new CSV file.

        Parameters:
        ------------
        output_path : str
            Optional. File path to save the cleaned data. Default is 'updated_nulls.csv'.
        """
        if self.cleaned_df is not None:
            try:
                self.cleaned_df.to_csv(output_path, index=False)
                print(f"Cleaned data saved to '{output_path}'.")
            except Exception as e:
                print(f"Error saving file: {e}")
        else:
            print("Please run clean_nulls() before saving.")


# The following code will only run if you open and run this file directly.
# If you import this file into another script or .py file, the code below will NOT run automatically.
if __name__ == "__main__":
    file_path = "dummy_filter_format.csv"  # Replace this with your actual file name
    cleaner = NullCleaner(file_path)
    cleaner.clean_nulls()
