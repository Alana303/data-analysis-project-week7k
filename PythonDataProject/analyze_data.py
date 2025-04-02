import pandas as pd
import matplotlib.pyplot as plt # type: ignore

# Load the dataset
df = pd.read_csv("sales_data.csv")

# Display first few rows
print(df.head())

# Basic Statistics
print(df.describe())

# Visualization - Bar Chart (Sales per Category)
df.groupby("Category")["Sales"].mean().plot(kind="bar", title="Average Sales per Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()
