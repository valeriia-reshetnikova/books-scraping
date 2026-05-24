import pandas as pd

try:
    df = pd.read_csv('books_data.csv')
    print("Success: 'books_data.csv' loaded successfully!")
except FileNotFoundError:
    print("Error: 'books_data.csv' not found. Please run '01_scraping.py' first!")
    exit()

print("\nData types BEFORE cleaning:")
print(df.dtypes)

df['Price_GBP'] = df['Price_GBP'].str[1:].astype('float')

exchange_rate_gbp_to_usd = 1.34  #Exchange rate fixed as of May 2026
df['Price_USD'] = (df['Price_GBP'] * exchange_rate_gbp_to_usd).round(2)
df = df.drop(columns=['Price_GBP'])

rating_mapping = {
    'One' : 1,
    'Two' : 2,
    'Three' : 3,
    'Four' : 4,
    'Five' : 5
}
df['Rating'] = df['Rating'].map(lambda x: rating_mapping[x])

print('\nData types AFTER cleaning:')
print(df.dtypes)

df.to_csv('books_cleaned.csv', index = False, encoding = 'utf-8')
print("\nStep 2 (Cleaning data) completed successfully!")
