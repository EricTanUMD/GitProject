# This module makes use webscraper.py to give the user ways to access the information of the top companies by revenue in the USA
# The program gives a series of prompts that the user can chose to select to access this information. A log of what was done will be printed out
# to show the user their history.
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

def find_employees(lower, upper):
    """ Find the revenues within the range of the ranks specified"""
    if(lower <= 0 or upper > 100):
        raise Exception("Sorry no lower limit below 1 or upper limit above 100")
    
    employees = []
    counter = 0
    for emp in ws.Companies["employees"][lower - 1: upper]:
        employees.append(emp)
        counter += 1
    return employees, counter

def remove_from_list(lower, upper, list): #try to iteratively remove from the list
    """ Removes everything from a list within the specified range of the list"""
    
    return 
################################################################################################################
# Main Code
loop = True
options = ("Find ranks", 
           "Find revenue", 
           "Find employee number",
           "Find revenue growth", 
           "Average revenue", 
           "Revenue per employee") #The user can only pick from these choices

print("Welcome to the Company Ranking DataBase")
result_log = []
result_num = 0
counter = 0
while (loop == True):
    print("Here are your options, ", options)
    choice = input("What do you wish to do?: ")
    print(choice)
    print(options[0].casefold())
    # Handle each function depending on
    if(choice.casefold() == options[0].casefold()): # Find Ranks
        lower_limit = int(input("Enter the lowest rank you want to find: "))
        upper_limit = int(input("Enter the highest rank you want to find: "))
        result_log, result_num = find_ranks(lower_limit, upper_limit)
        print("Here are the ranks in order: {}. You searched through {} companies.", result_log, result_num)
    elif(choice.casefold() == options[1].casefold()): # Find Revenue
        lower_limit = int(input("Enter the lowest rank you want to find revenue: "))
        upper_limit = int(input("Enter the highest rank you want to find revenue: "))
        result_log, result_num = find_revenue(lower_limit, upper_limit)
        print("Here are the revenues in millions USD in order from largest to smallest {}. You searched through {} companies.".format(result_log, result_num))
    elif(choice.casefold() == options[2].casefold()): # Employee Numbers
        lower_limit = int(input("Enter the lowest rank you want to find employee numbers: "))
        upper_limit = int(input("Enter the highest rank you want to find employee number: "))
        result_log, result_num = find_employees(lower_limit, upper_limit)
        print("Here are the employee numbers for the companies you specified {}. You searched through {} companies".format(result_log, result_num))
    elif(): # Revenue Growth
        lower_limit = int(input("Enter the lowest rank you want to find revenue growth: "))
        upper_limit = int(input("Enter the highest rank you want to find revenue growth: "))
        print("placeholder")
    elif(): # Average revenue find
        print("placeholder")
    else: # If the user fails to input anything, they will have up to 3 chances input a valid input
        counter += 1
        print("Invalid Input you have failed {} times. Program exits after 3 fails.".format(counter))


    if (counter == 3):
        print("Too many invalid inputs rerun the program")
        break

    #Note to self, you can convert a df column into an array
    if (input("Do you wish to continue?") == "no".casefold()):
        loop = False
        print("Thanks for using the program, exiting now")




##################################################################################################################
# Tests
#ranks, number = find_ranks(1, 10)
#print(ranks)