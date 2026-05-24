import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
all_books_data = []

for page in range(1, 51):
    print(f'Scraping page {page}/50...')
    url = base_url.format(page)

    try:
        response = requests.get(url, timeout = 10)
        response.encoding = 'utf-8'
    except requests.RequestException as e:
        print(f'Warning: Skipped page {page} due to {e}')
        continue

    if response.status_code != 200:
        print(f'Warning: Skipped page {page} due to connection error')
        continue

    soup = BeautifulSoup(response.text, 'html.parser')
    book_cards = soup.find_all('article', class_ = 'product_pod')

    for book in book_cards:

        book_title = book.h3.a['title']
        book_price = book.find('p', class_ = 'price_color').text
        book_rating_classes = book.p['class']
        book_rating = book_rating_classes[1] if len(book_rating_classes) > 1 else None
        book_availability = book.find('p', class_ = 'instock availability').text.strip()

        book_info = {
            'Title' : book_title,
            'Price_GBP' : book_price,
            'Rating' : book_rating,
            'Availability' : book_availability
            }
        all_books_data.append(book_info)
    time.sleep(1)

df = pd.DataFrame(all_books_data)
df.to_csv('books_data.csv', index = False, encoding = 'utf-8')
print("Step 1 (Scraping all pages) completed successfully!")
