# web-scraping
 HHA 507 Assignment 7
## Description
### Required Packages
- BeautifulSoup
- Pandas
- Requests

### Methodology 
- The script uses the requests package to get the HTML from the website
- The BeautifulSoup package is used to parse the HTML and extract the data
- The data is stored in a Pandas DataFrame and exported to a CSV file

### Extracting the data
- CoinMarketCap
    - This site had a table with data for the top cryptocurrencies. The data was extracted from the table using the BeautifulSoup find function. The tag class was inspected using a web browser. It was then stored in a DataFrame using the pandas read_html function. 
    - After the data was extracted, the DataFrame was filtered to only include the columns that were needed, the rows that were not needed were dropped, and only the top 10 cryptocurrencies were kept. It was also neccessary to clean up some of the data in the DataFrame to make it usable. (e.g. removing the redunadant 6.18B from the Market Cap column, or removing position and symbol from the name column)
    - The DataFrame was then exported to a CSV file using the to_csv function in pandas.

- NYT
    - For the NYT website, the data was extracted using the BeautifulSoup find_all function. The tag class was inspected using a web browser.
         - To do this I searched for the tag classes that contained the data I wanted to extract. I then used the find_all function to extract the data from the HTML.
    - 3 different tags were used to extract the data. The first tag was used to extract the title of the article, the second tag was used to extract the author of the article, and the third tag was used to extract the subheading of the article.
    - 3 lists were created to store the data from the tags. The lists were then combined into a DataFrame using the pandas DataFrame function.
    - The DataFrame was then exported to a CSV file using the to_csv function in pandas.