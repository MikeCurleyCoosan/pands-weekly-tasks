#Question: Write a python program called accounts.py that reads in a 10 character number and outputs
#the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs)

#Modify the program to deal with account numbers of any length (comment your assumptions)
#Assumptions: I have assumed that the account number is at least 10 digits long and the last 4 digits are alwasys shown

#Author: Michael Curley

#Read in the account number
accountNumber = input("Please enter your account number: ")
#Check what type the input is
isInt = type(accountNumber)

#As long as an integer is entered
if isInt == int:
    asString = str(accountNumber) #Convert the integer to a string
    lengthOfInput = len(asString) #And get the length of the string
    """print(lengthOfInput)""" #testing 
elif isInt != int: #If it isnt an integer, ask again for a 10 digit number
    accountNumber = input("Please enter your account number: ")
    isInt = type(accountNumber)

#While the string is less than 10 digits long, ask user for 10 digit number
while lengthOfInput <10:
    print("That account number is less than 10 numbers")
    accountNumber = input("Please enter your account number: ")
    asString = str(accountNumber)
    lengthOfInput = len(asString)
    

#Get the last 4 characters of the string version of input
slicedString = asString[lengthOfInput-4:]

#Put an x for all charactes apart from the last 4 charactes
hideFront = "x" * (lengthOfInput-4)
result = hideFront + slicedString
print(result)

