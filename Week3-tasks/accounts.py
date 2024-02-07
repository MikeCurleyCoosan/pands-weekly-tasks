#Question: Write a python program called accounts.py that reads in a 10 character number and outputs
#the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs)

#Author: Michael Curley

#Read in the account number
accountNumber = input("Please enter a 10 digit account number: ")
#Check what type the input is
print(type(accountNumber))
#Convert input to String to find length
asString = str(accountNumber)
print(asString)

#Find the length of a string
lengthOfInput = len(asString)
print(lengthOfInput)

#While the string is less than 10 characters long, ask user for 10 digit number
while  lengthOfInput <10:
    print("That account number is less than 10 numbers")
    accountNumber = input("Please enter a 10 digit account number: ")
    asString = str(accountNumber)
    lengthOfInput = len(asString)
    break

#Get the last 4 characters of the string version of input
slicedString = asString[6:]

hideFront = "xxxxxx"
result = hideFront + slicedString
print(result)

