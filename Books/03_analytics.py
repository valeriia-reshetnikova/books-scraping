import pandas as pd

try:
    df = pd.read_csv('books_cleaned.csv')
    print("Success: 'books_cleaned.csv' loaded successfully")
except FileNotFoundError:
    print("Error: 'books_cleaned.csv' not found. Please run '02_cleaning.py' first!")
    exit()

print("\n---GENERAL STATISTICS---")
print(df.describe())

print('\n---KEY INSIGHTS---')
total_books = len(df)
average_price = df['Price_USD'].mean().round(2)
print(f"Total books analyzed: {total_books}")
print(f"Average book price: ${average_price}")

cheapest_book_index = df['Price_USD'].idxmin()
expensive_book_index = df['Price_USD'].idxmax()

cheapest_title = df.loc[cheapest_book_index, 'Title']
cheapest_price = df.loc[cheapest_book_index, 'Price_USD']

expensive_title = df.loc[expensive_book_index, 'Title']
expensive_price = df.loc[expensive_book_index, 'Price_USD']

print(f"Cheapest book: '{cheapest_title}' (${cheapest_price})")
print(f"Most expensive book: '{expensive_title}' (${expensive_price})")

print("\n---PRICE BY RATING ANALYSIS---")
price_by_rating = df.groupby('Rating')['Price_USD'].mean().round(2)
print(price_by_rating)

print("\n---AVAILABILITY ANALYSIS---")
availability_count = df['Availability'].value_counts()
print(availability_count)
print("\nStep 3 completed! Analytics workflow finished successfully!")