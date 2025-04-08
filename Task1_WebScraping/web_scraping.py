import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL (a practice scraping site)
url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract book titles
books = []
for book in soup.find_all('h3'):
    books.append({'Title': book.a['title']})

# Save to CSV
pd.DataFrame(books).to_csv('books.csv', index=False)
print("Done! Check 'books.csv' on your computer.")
