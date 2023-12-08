# This module makes use webscraper.py to give the user ways to access the information of the top companies by revenue in the USA
# The program gives a series of prompts that the user can chose to select to access this information. A log of what was done will be printed out
# to show the user their history.
import webscraper as ws
import numpy as np

data_frame = ws.pd.read_csv('df.csv') #bring in the csv data exported from webscraper
############################################################################################################]
# Functions. All Returning tuples of results and the number of places searched
def find_ranks(lower, upper):
    """ Finds the names of the companies with ranks between the specified lower and upper values. """
    if(lower <= 0):
        raise Exception("Sorry no lower limit below 1 or upper limit above 100")
    if(lower >= upper): # also an invalid range, in this case, we will simply adjust the range to only encompass the upper rank
        lower = upper - 1
        print("Invalid range, adjusting lower limit.")
    
    names = []
    counter = 0
    for company_name in ws.Companies["name"][lower - 1: upper]: #We have 100 companies so indexed from 0 to 99
        names.append(company_name)
        counter += 1
    return names, counter
# Searches through the revenues dictionary value for a user specified range. Though the tuple is 0 indexed, it accounts for it.
def find_revenue(lower, upper):
    """ Find the revenues within the range of the ranks specified"""
    if(lower <= 0 or upper > 100):
        raise Exception("Sorry no lower limit below 1 or upper limit above 100")
    if(lower >= upper): # also an invalid range, in this case, we will simply adjust the range to only encompass the upper rank
        lower = upper - 1
        print("Invalid range, adjusting lower limit.")
    
    revenue = []
    counter = 0
    for rev in ws.Companies["revenue"][lower - 1: upper]:
        revenue.append(rev)
        counter += 1
    return revenue, counter
# Search through the employees dictionary value within a user specified rank range. Returns the list of employee numbers within this range.
def find_employees(lower, upper):
    """ Find the revenues within the range of the ranks specified"""
    if(lower <= 0 or upper > 100):
        raise Exception("Sorry no lower limit below 1 or upper limit above 100")
    if(lower >= upper): # also an invalid range, in this case, we will simply adjust the range to only encompass the upper rank
        lower = upper - 1
        print("Invalid range, adjusting lower limit.")
    employees = []
    counter = 0
    for emp in ws.Companies["employees"][lower - 1: upper]:
        employees.append(emp)
        counter += 1
    return employees, counter
# Search through the revenue growth dictionary value within a user specified rank range. Returns the list of revenue growth rates within this range.
def find_revenue_growth(lower, upper):
    """ Find the revenue growths within the range of the ranks specified"""
    if(lower <= 0 or upper > 100):
        raise Exception("Sorry no lower limit below 1 or upper limit above 100")
    if(lower >= upper): # also an invalid range, in this case, we will simply adjust the range to only encompass the upper rank
        lower = upper - 1
        print("Invalid range, adjusting lower limit.")
    
    rev_growth = []
    counter = 0
    for growth in ws.Companies["revenue_growth"][lower - 1: upper]:
        rev_growth.append(growth)
        counter += 1
    return rev_growth, counter

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
           "Average revenue") #The user can only pick from these choices

print("Welcome to the Company Ranking DataBase")
result_log = []
result_num = 0
counter = 0
while (loop == True):
    print("Here are your options, ", options)
    choice = input("What do you wish to do?: ")
    # Handle each function depending on
    if(choice.casefold() == options[0].casefold()): # Find Ranks
        lower_limit = int(input("Enter the lowest rank you want to find: "))
        upper_limit = int(input("Enter the highest rank you want to find: "))
        result_log, result_num = find_ranks(lower_limit, upper_limit)
        print("Here are the ranks in order: {}. You searched through {} companies.".format(result_log, result_num))
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
    elif(choice.casefold() == options[3].casefold()): # Revenue Growth
        lower_limit = int(input("Enter the lowest rank you want to find revenue growth: "))
        upper_limit = int(input("Enter the highest rank you want to find revenue growth: "))
        result_log, result_num = find_revenue_growth(lower_limit, upper_limit)
        print("Here are the revenue growth numbers within this range {}. You searched through {} companies".format(result_log, result_num))
    elif(choice.casefold() == options[4].casefold()): # Average revenue finder
        lower_limit = int(input("Enter the lowest rank you want to use for calculating the average: "))
        upper_limit = int(input("Enter the highest rank you want to use for calculating the average: "))
        revenue_array = np.asarray(ws.Companies["revenue"][lower_limit - 1: upper_limit])

        minimum = 0
    
        if(input("Do you wish to set a minimum? ").casefold() == "yes".casefold()):
            minimum = float(input("Enter your minimum: "))

        revenue_array = revenue_array[revenue_array > minimum]
        # print(revenue_array)
        result_log = revenue_array
        result_num = revenue_array.sum()/(len(revenue_array))
        print("Here is your list of revenues {} and your average revenue {}".format(result_log, result_num))
    else: # If the user fails to input anything or a valid option, they will have up to 3 chances input a valid input
        counter += 1
        print("Invalid Input you have failed {} times. Program exits after 3 fails.".format(counter))

    # If the user fails 3 times, the program will close and prompt for a rerun.
    if (counter == 3):
        print("Too many invalid inputs rerun the program and try again. ")
        break

    #Note to self, you can convert a df column into an array
    if (input("Do you want to do another function?: ") == "no".casefold()):
        loop = False
        print("Thanks for using this program, exiting now. ")




##################################################################################################################
# Tests
#ranks, number = find_ranks(1, 10)
#print(ranks)