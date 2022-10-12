#import packages
import requests
from bs4 import BeautifulSoup
import pandas as pd


#Web Scraping the NYT Technology Section with BeautifulSoup.
#request the page   
page = requests.get('https://www.nytimes.com/section/technology')

#Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

#print prettified version of soup, using a web browser is easier to read
print(soup.prettify())

#Extract information from the page
##Extract the title of the article
Titles = soup.find_all('h2', class_='css-1kv6qi e15t083i0')
output_titles = [title.text for title in Titles]


##Extract the author(s) of the article
authors = soup.find_all('span', class_='css-1n7hynb')
output_authors = [author.text for author in authors]

##Extract the subheading of the article
subheadings = soup.find_all('p', class_='css-1pga48a e15t083i1')
output_subheadings = [subheading.text for subheading in subheadings]



df = pd.DataFrame({'title': output_titles, 'authors': output_authors, 'subheading': output_subheadings})
df.to_csv('data/NYT_Tech.csv', index=False)

