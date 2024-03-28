#Question: Write a python program called accounts.py that reads in a 10 character number and outputs
#the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs)

#Modify the program to deal with account numbers of any length (comment your assumptions)
#Assumptions: I have assumed that the account number is at least 10 digits long and the last 4 digits are alwasys shown
#Futher changes to follow.....

#Author: Michael Curley

length_of_input = 0

#Run the program until the user enters a 10 digit account number
while True and length_of_input < 10:
    #Ask the user for a 10 digit account number
    account_number = input("Please enter a 10 digit accound number ")
    #Check if the input is an integer
    try:
        #If the input is an integer, convert it to a string and get the length of the string
        number_as_int = int(account_number)
        number_as_str = str(account_number)
        length_of_input = len(number_as_str)
        #If the length of the input is less than 10, ask the user for a 10 digit account number
        if length_of_input < 10:
            print("The account number is less than 10 digits long, please enter a valid 10 digit account number")
            continue

        else:
            #Get the last 4 characters of the string version of input
            sliced_string = number_as_str[length_of_input-4:]
            #Put an x for all charactes apart from the last 4 charactes
            hide_front = "x" * (length_of_input-4)
            #Combine the x's and the last 4 characters
            result = hide_front + sliced_string
            #Print the result
            print(result)
        break;
    #If the input is not an integer, ask the user for a valid number
    except ValueError:
        try:
            #If the input is a float, ask the user for a valid number
            val = float(account_number)
            print("Input is an float number, account numbers should contain integers only.")
            continue
        except ValueError:
            #If the input is a string, ask the user for a valid number
            print("This is not a number, its a string. Please enter a valid 10 digit account number")
            continue

#Problems encountered while writing the code:
        # Leading zeros were being removed from the account number when the user entered a number with leading zeros
        # The program was not checking if the input was a float or a string
        # The program was not checking if the input was less than 10 digits long