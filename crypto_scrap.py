#import dependencies
import requests
from bs4 import BeautifulSoup
import pandas as pd


#Web Scraping CoinMarketCap with BeautifulSoup for the price of top 10 cryptocurrencies.
#request the page
page = requests.get('https://coinmarketcap.com/')
page
#Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

#Extract information from the page

##Extract the top 10 cryptocurrencies
cryptocurrencies = soup.find('table', class_='h7vnx2-2 juYUEZ cmc-table')
df = pd.read_html(str(cryptocurrencies))[0]

#using iloc to select the first 10 rows
df = df.iloc[0:10]

#Drop unwanted columns and rename the columns
df = df.drop(['Unnamed: 0'], axis=1)
df = df.drop(['Unnamed: 11'], axis=1)
df = df.drop(['Last 7 Days'], axis=1)
df = df.rename(columns={'Name': 'name', 'Price': 'price', 'Market Cap': 'market_cap', 'Circulating Supply': 'circulating_supply', 'Volume(24h)': 'volume_24h'})


# In the name column, remove the rank and the name of the cryptocurrency and keep only the name
x = 0
for name in df['name']:
    int = False
    for i in range(0, len(name)):
        if name[i].isdigit():
            int = True
            spot = i
            break
    if int == True:
        name = name[:i]
        df['name'][x] = name
        x += 1

# In the market_cap column, remove the dollar sign and the commas and all characters before the 'B'

df['market_cap'] = df['market_cap'].str.split('B').str[1]


df.to_csv('data/cryptocurrenies.csv', index=True)