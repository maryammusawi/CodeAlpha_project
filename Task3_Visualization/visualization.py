import pandas as pd
import matplotlib.pyplot as plt

# Load data
try:
    df = pd.read_csv('books.csv')
    print("Data loaded successfully! First 5 rows:")
    print(df.head())
except FileNotFoundError:
    print("Error: books.csv not found in:", os.getcwd())
    exit()

# Create visualization
df['Title Length'] = df['Title'].apply(len)
plt.hist(df['Title Length'], bins=10, color='skyblue')
plt.title('Book Title Length Distribution')
plt.xlabel('Characters')
plt.ylabel('Number of Books')

# Save and show
plt.savefig('my_chart.png')
print("Chart saved as my_chart.png")
plt.show()
