import gazpacho
import requests
import re

## web scraping basics
url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"

html = requests.get(url)

imdb = gazpacho.Soup(html.text)
launched_year = imdb.find("h3",{"class": "lister-item-header"})
clean_launched_years = []

for i in launched_year:
    i = i.strip()
    year = re.search(r'\((\d{4})\)', i)
    if year:
        clean_launched_years.append(year.group(1))
    else:
        clean_launched_years.append('None')

import pandas as pd

# create dataframe
movie_database = pd.DataFrame( data = {
    "lauched_year":clean_launched_years,
})

# print first five rows
movie_database.head()
