import pandas as pd

# Load the CSV
df = pd.read_csv('books.csv')

# Basic analysis
print("First 5 books:")
print(df.head())

print("\nTotal books scraped:", len(df))