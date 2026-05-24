import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv('books_cleaned.csv')
    print("Success: 'books_cleaned.csv' loaded successfully!")
except FileNotFoundError:
    print("Error: 'books_cleaned.csv' not found. Please run '02_cleaning.py' first!")
    exit()

sns.set_theme(style="whitegrid")
PALETTE = "Blues_d"

plt.rcParams.update({
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'figure.figsize': (10, 6)
})

print('\n---Price by Rating---')
avg_price_data = df.groupby('Rating')['Price_USD'].mean().reset_index()
ax = sns.barplot(data = avg_price_data, x = 'Rating', y = 'Price_USD', hue = 'Rating', palette = PALETTE, legend = False)
for container in ax.containers:
    ax.bar_label(container, fmt='%.2f', padding = 3, fontsize = 11, fontweight = 'bold')
plt.title('Average book price by Rating')
plt.xlabel('Rating (Stars)')
plt.ylabel('Average Price USD')
plt.savefig('01_price_by_rating.png')
print("Saved: '01_price_by_rating.png'")
plt.close()

print('\n---Price Distribution---')
sns.histplot(df['Price_USD'], bins = 15, kde = True, color = 'steelblue')
plt.title('Distribution of Book Prices')
plt.xlabel('Price USD')
plt.ylabel('Count')
plt.savefig('02_price_distribution.png')
print("Saved: '02_price_distribution.png'")
plt.close()


print('\n---Books count by Rating---')
ax = sns.countplot(data = df, x = 'Rating', hue = 'Rating', palette = PALETTE, legend = False)
for container in ax.containers:
    ax.bar_label(container, padding = 3, fontsize = 11, fontweight = 'bold')
plt.title('Number of Books by Rating')
plt.xlabel('Rating (Stars)')
plt.ylabel('Total Books')
plt.savefig('03_books_count_by_rating.png')
print("Saved: '03_books_count_by_rating.png'")
plt.close()

print('\n---Price Boxplot---')
sns.boxplot(data = df, x = 'Rating', y = 'Price_USD', hue = 'Rating', palette = PALETTE, legend = False)
plt.title('Price Distribution Across Ratings (Boxplot)')
plt.xlabel('Rating (Stars)')
plt.ylabel('Price USD')
plt.savefig('04_price_boxplot.png')
print("Saved: '04_price_boxplot.png'")
plt.close()

print('\n---Top 10 Most Expensive Books')
top_10_expensive = df.nlargest(10, 'Price_USD')
ax = sns.barplot(data = top_10_expensive, x = 'Price_USD', y = 'Title', hue = 'Title', palette = PALETTE, legend = False)
for container in ax.containers:
    ax.bar_label(container, fmt='%.2f', padding = 3, fontsize = 11, fontweight = 'bold')
plt.title('Top 10 Most Expensive Books on the Website')
plt.xlabel('Price USD')
plt.ylabel('', fontsize = 11)
plt.savefig('05_top_10_expensive.png', dpi = 300, bbox_inches = 'tight')

print("Saved: '05_top_10_expensive.png'")
plt.close()