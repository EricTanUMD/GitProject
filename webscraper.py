# Required Imports, everything is installed via pip
from bs4 import BeautifulSoup
import requests

#Use Beautiful soup to specificly scrape the first chart for its information
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
print("This is our url to make the soup: " , url)
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

print(soup)