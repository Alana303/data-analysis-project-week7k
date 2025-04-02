import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Dataset Loaded Successfully!\n")
        print("First Few Rows:\n", df.head())
        print("\nDataset Info:")
        print(df.info())
        print("\nMissing Values:\n", df.isnull().sum())
        
        # Handle missing values
        df = df.dropna()  # Drop missing values (or use df.fillna(value))
        return df
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as e:
        print("An error occurred:", e)

# Task 2: Basic Data Analysis
def analyze_data(df):
    print("\nBasic Statistics:\n", df.describe())
    
    # Example grouping: Assume 'Category' is a categorical column
    if 'Category' in df.columns:
        grouped = df.groupby('Category').mean()
        print("\nGrouped Data by Category:\n", grouped)
    
# Task 3: Data Visualization
def visualize_data(df):
    plt.figure(figsize=(12, 6))
    
    # Line Chart (Example: Date vs Sales)
    if 'Date' in df.columns and 'Sales' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])  # Convert Date column
        df.set_index('Date')['Sales'].plot(title='Sales Over Time', ylabel='Sales', xlabel='Date')
        plt.show()
    
    # Bar Chart (Example: Category vs Sales)
    if 'Category' in df.columns and 'Sales' in df.columns:
        df.groupby('Category')['Sales'].mean().plot(kind='bar', title='Average Sales per Category')
        plt.show()
    
    # Histogram (Example: Sales Distribution)
    if 'Sales' in df.columns:
        df['Sales'].plot(kind='hist', title='Sales Distribution', bins=20)
        plt.show()
    
    # Scatter Plot (Example: Two numerical columns)
    if 'Feature1' in df.columns and 'Feature2' in df.columns:
        sns.scatterplot(x=df['Feature1'], y=df['Feature2'])
        plt.title('Feature1 vs Feature2')
        plt.show()

if __name__ == "__main__":
    file_path = "your_dataset.csv"  # Update this with your actual dataset path
    df = load_dataset(file_path)
    
    if df is not None:
        analyze_data(df)
        visualize_data(df)
