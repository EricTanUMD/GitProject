# This file serves to scrape informations of the wikipedia page that documents the largest companies in the United states by revenue.
# This information will then be sequentially fed into a series of lists, a dictionary, and then be converted into a dataframe. The User may also
# Peak into the dictionary if they so choice once the program is running.
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import re

#Use Beautiful soup to specificly scrape the first chart for its information
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
print("This is our url to make the soup: " , url)
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)


#Finding the correct table
table = soup.find_all('table')[1] #We found the table we want here
base_titles = table.find_all('th') # we extract the tiles marked by </th>
titles = [title.text.strip() for title in base_titles] # remove </th> and new lines, only a list of base strings remain

# Pandas functionalities
df = pd.DataFrame(columns = titles) #create our dataframe with columns
column_data = table.find_all('tr')

# Extract the information of each row into a list of its own, We will eventually turn this information into a dictionary and dataframe
Companies = {
    "rank": "",
    "name": "",
    "industry": "",
    "revenue": "",
    "revenue_growth": "",
    "employees": "",
    "headquarters": "" 
}

rank = []
name = []
industry = []
revenue = []
revenue_growth = []
employees = []
headquarters = []

counter = 1
for row in column_data[1:]: #skip first blank row
    row_data = row.find_all('td')
    #print(row_data)
    for data in row_data:
        if(counter == 1):
            rank.append(int(data.text.strip()))
            counter += 1
        elif(counter == 2):
            name.append(data.text.strip())
            counter += 1
        elif (counter == 3):
            industry.append(data.text.strip())
            counter += 1
        elif (counter == 4):
            revenue.append(float(re.sub("[,]", "", data.text.strip())))
            counter += 1
        elif (counter == 5):
            revenue_growth.append(float(re.sub("[\%]", "", data.text.strip()))) #this is a percent, convert for specific calculations
            counter += 1
        elif (counter == 6):
            employees.append(float(re.sub("[,]", "", data.text.strip()))) #convert into a float
            counter += 1
        elif (counter == 7):
            headquarters.append(data.text.strip())
            counter = 1

#print(headquarters)
#print(len(rank) + len(name) + len(industry) + len(revenue) + len(revenue_growth) + len(employees) + len(headquarters))

# Update the values of the dictionary using update()
Companies.update({"rank": tuple(rank),
    "name": tuple(name),
    "industry": tuple(industry),
    "revenue": tuple(revenue),
    "revenue_growth": tuple(revenue_growth),
    "employees": tuple(employees),
    "headquarters": tuple(headquarters)})

data_frame = pd.DataFrame.from_dict(Companies)
#print(data_frame)
data_frame.to_csv(os.getcwd() + '/df.csv', index = False) #import the constructed dataframe as a csv file!

# If the User wants to see the dictionary, they can. Access both key and value in the dict to do so
see_dict = input("View Company information?")
if(see_dict == "yes".casefold()):
    for key, value in Companies.items():
        print(key, " ", value)
else:
    print("Ok, no issue")