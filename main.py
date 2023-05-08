import requests
from bs4 import BeautifulSoup
import pandas as pd

# Set headers and cookies
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
cookies = {
    'session-id': '',
    'session-id-time': '',
    'i18n-prefs': '',
    'lc-acbin': '',
    'sp-cdn': '',
    'x-main': '',
    'at-main': '',
    'ubid-main': '',
    'session-token': ''
}

# Send request
url = 'https://www.amazon.in/s?k=tv&crid=2DRPO916WT546&sprefix=%2Caps%2C255&ref=nb_sb_noss_2'
response = requests.get(url, headers=headers, cookies=cookies)

# Parse content
soup = BeautifulSoup(response.content, 'html.parser')

# Find products
products = soup.find_all('div', {'data-component-type': 's-search-result'})

# Extract titles and links
titles = []
links = []
for product in products:
    title = product.find('span', {'class': 'a-size-medium a-color-base a-text-normal'}).text.strip()
    link = 'https://www.amazon.in' + product.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})['href']
    titles.append(title)
    links.append(link)

# Convert to DataFrame and save as CSV
df = pd.DataFrame({'Title': titles, 'Link': links})
df.to_csv('Amazon_Product_List.csv', index=False)
