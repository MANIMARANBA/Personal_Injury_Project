import pandas as pd

from datetime import datetime

dataset_path = "D:/BA_Project_Portfolio/personal_injury_cases.csv"
df = pd.read_csv(dataset_path)

# View the first few rows of the dataset
print(df.head())

# Get summary statistics of the dataset
print(df.describe())

# Check the data types and column information
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Remove duplicate records
df.drop_duplicates(inplace=True)

# Perform data transformations or preprocessing as needed
# For example, convert date columns to datetime type, handle categorical variables, etc.

# Example: Calculate the count of cases by case type
case_type_counts = df["Case Type"].value_counts()
print(case_type_counts)

# Example: Create a bar plot of case status distribution
import matplotlib.pyplot as plt

case_status_counts = df["Case Status"].value_counts()
plt.bar(case_status_counts.index, case_status_counts.values)
plt.xlabel("Case Status")
plt.ylabel("Count")
plt.title("Distribution of Case Status")
plt.show()

import numpy as np

# Example: Calculate the average case duration
df["Case Start Date"] = pd.to_datetime(df["Case Start Date"])
df["Case Close Date"] = pd.to_datetime(df["Case Close Date"])
df["Case Duration"] = (df["Case Close Date"] - df["Case Start Date"]).dt.days
average_duration = np.mean(df["Case Duration"])
print("Average Case Duration: ", average_duration)


