# Required Imports, everything is installed via pip
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

#Use Beautiful soup to specificly scrape the first chart for its information
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
print("This is our url to make the soup: " , url)
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)


#Finding the correct table
print()
table = soup.find_all('table')[1] #We found the table we want here
base_titles = table.find_all('th') # we extract the tiles marked by </th>
titles = [title.text.strip() for title in base_titles] # remove </th> and new lines, only a list of base strings remain

# Pandas functionalities
df = pd.DataFrame(columns = titles) #create our dataframe with columns
column_data = table.find_all('tr')

#Extract the row data from each column, but these are still individual lists
for row in column_data[1:]: #skip first blank row
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    # print(individual_row_data)
    df_length = len(df) 
    df.loc[df_length] = individual_row_data # check for the length of the dataframe and we just append each row onto it, pretty cool

print(df)
df.to_csv(os.getcwd() + '/df.csv', index = False) #import the constructed dataframe as a csv file!