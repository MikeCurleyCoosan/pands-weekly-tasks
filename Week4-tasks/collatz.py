#Write a program called collatz.py, that asks the user to input any positive integer and outputs the successive values 
#of the following calculation. At each step calculate the next value by taking the current value and, if it is even,
#divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

number = int(input('Please enter a positive number: ')) #Ask user for positive number 
allNumbers = [] #Create a list to store the numbers

if number < 0: #If number given is not positive
    print('That is not a positive number, Please try again: ') #Tell the user the number entered is not positive
    number = int(input('Please enter a positive number: ')) # And ask again for positive number

print(number) #Print the first collatz series number

while number !=1: #The series ends when it reaches 1
    if (number % 2) == 0: #Check if number is even
        number = int(number/2) #If even divide by two and reassign to number
        allNumbers.append(number) #Add to the list
    else:
        number = (int(number *3)+1) #If number is not even, then its odd. Multiply it by 3 and add 1 to it.
        allNumbers.append(number) #Add number to the list

print(allNumbers) # print out the list

print('You have reached one, that is the end of the series. Thank you for playing')