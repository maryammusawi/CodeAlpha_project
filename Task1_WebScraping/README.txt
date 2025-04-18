TASK 1: WEB SCRAPING
---------------------
**Project Description**:
Scraped book titles and ratings from books.toscrape.com using Python.

**Libraries Used**:
- requests
- BeautifulSoup
- pandas

**How to Run**:
1. Install dependencies:
   pip install requests beautifulsoup4 pandas
2. Run the script:
   python web_scraping.py

**Output**:
- Generates a CSV file: `books.csv`

**Notes**:
- Target website: http://books.toscrape.com/
- Script handles basic HTTP requests and saves data in structured format.

## Datasets Scraped
1. **`books.csv`**:  
   - Source: [books.toscrape.com](http://books.toscrape.com)  
   - Contents: 10 book titles.

2. **`amazon_reviews.csv`**:  
   - Source: Amazon product reviews (provide URL if possible)  
   - Contents: Review text and ratings.  
   - Example row:  
     ```csv
     "Great product!",5
     "Not worth the price.",2
     ``` 
