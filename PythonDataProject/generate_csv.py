import pandas as pd

# Create sample data
data = {
    "Date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
    "Category": ["Electronics", "Clothing", "Groceries", "Electronics", "Clothing"],
    "Sales": [500, 300, 150, 700, 250],
    "Feature1": [10, 15, 8, 12, 14],
    "Feature2": [20, 25, 18, 22, 30],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("sales_data.csv", index=False)

print("✅ CSV file 'sales_data.csv' created successfully!")
