import requests
from bs4 import BeautifulSoup

# specify the URL to scrape
url = 'https://dailytrust.com/87-days-to-go-buhari-races-to-complete-legacy-projects/'

# send a GET request to the URL and retrieve the HTML content
response = requests.get(url)

# check the response status code
status = response.status_code
print(status)

# parse the HTML content using BeautifulSoup
content = response.content
soup = BeautifulSoup(content, 'html.parser')

# extract the page title and print it
title = soup.title
print(title)

# extract all paragraphs and print their text
paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.get_text())
