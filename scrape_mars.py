#import dependencies
import pandas as pd
import time
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.mars_db
collection = db.articles

# URL of page to be scraped
nasa_url = 'https://mars.nasa.gov/news/'
jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
twitter_url = 'https://twitter.com/marswxreport?lang=en'
# Retrieve page with the requests module
response = requests.get(nasa_url)
# Create BeautifulSoup object; parse with 'lxml'
soup = BeautifulSoup(response.text, 'lxml')
#print(soup)

news_title = soup.find_all("div",class_="content_title")
#print(news_title)

news_p = soup.find_all("div", class_="rollover_description_inner")
#print(news_p)

featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA17832_hires.jpg'
#print(featured_image_url)

twitter_url = 'https://twitter.com/marswxreport?lang=en'
response = requests.get(twitter_url)
soup = BeautifulSoup(response.text, 'lxml')
twitter = soup.find('div', class_='js-tweet-text-container').text
#weathertweet = twitter.find_all('')
#print(twitter)


facts_url = 'https://space-facts.com/mars'
response = requests.get(facts_url)
facts_soup = BeautifulSoup(response.text, 'lxml')
facts = facts_soup.find('table', class_= 'tablepress tablepress-id-mars').text

column1 = facts_soup.find_all('td', class_='column-1')
column2 = facts_soup.find_all('td', class_='column-2')
facets = []
values = []

for row in column1:
    facet = row.text.strip()
    facets.append(facet)
    
for row in column2:
    value = row.text.strip()
    values.append(value)
    
mars_facts = pd.DataFrame({
    "Facet":facets,
    "Value":values
    })

mars_facts_html = mars_facts.to_html(header=False, index=False)
mars_facts

c_image_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
#print(c_image_url)

s_image_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
#print(s_image_url)

sy_image_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
#print(sy_image_url)

v_image_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'
#print(v_image_url)