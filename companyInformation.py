# This module makes use webscraper.py to give the user ways to access the information of the top companies by revenue in the USA
# The program gives a series of prompts that the user can chose to select to access this information.
import webscraper as ws

data_frame = ws.pd.read_csv('df.csv') #bring in the csv data exported from webscraper
############################################################################################################]
# Functions
def find_ranks(lower, upper):
    """ Finds the names of the companies with ranks between the specified lower and upper values. """
    if(lower <= 0):
        raise Exception("Sorry no lower limit below 1 or upper limit above 100")
    
    names = []
    counter = 0
    for company_name in ws.Companies["name"][lower - 1: upper]: #We have 100 companies so indexed from 0 to 99
        names.append(company_name)
        counter += 1
    return names, counter

def find_revenue(lower, upper):
    """ Find the revenues within the range of the ranks specified"""
    if(lower <= 0 or upper > 100):
        raise Exception("Sorry no lower limit below 1 or upper limit above 100")
    
    revenue = []
    counter = 0
    for rev in ws.Companies["revenue"][lower - 1: upper]:
        revenue.append(rev)
        counter += 1
    return revenue, counter

def remove_from_list(lower, upper, list): #try to iteratively remove from the list
    """ Removes everything from a list within the specified range of the list"""
    
    return 
################################################################################################################
# Main Code
loop = True
options = {"Find ranks ", 
           "Find revenue", 
           "Find employee number ",
           "Find revenue growth", 
           "Average revenue ", 
           "Revenue per employee "} #The user can only pick from these choices

print("Welcome to the Company Ranking DataBase")
while (loop == True):
    print("Here are your options, ", options)
    choice = input("What do you wish to do?:\n")
    # Handle each function depending on
    if(choice.casefold() == options[0].casefold()): # consider adding a string to store the tuple results using variables.
        lower_limit = input("Enter the lowest rank you want to find: ")
        upper_limit = input("Enter the highest rank you want to find: ")
        print()

    #Note to self, you can convert a df column into an array
    if (input("Do you wish to continue?") == "yes".casefold()):
        loop = False
        break




##################################################################################################################
# Tests
#ranks, number = find_ranks(1, 10)
#print(ranks)