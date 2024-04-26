#Write a program called collatz.py, that asks the user to input any positive integer and outputs the successive values 
#of the following calculation. At each step calculate the next value by taking the current value and, if it is even,
#divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

#Modification: After looking into lists on the RealPython website and the DataCamp website, I have modified this program
#to include a list.

#Create a list to store the numbers
allNumbers = [] 

number = input('Please enter a positive number: ')#Ask user for positive number

#Run the program until the user enters a positive number
while True:
    #Check if the input is an integer
    try: 
        #If the input is an integer,  
        number = int(number) #Ask user for positive number 
        #Check if the number is positive
        if number < 0:
            #If the number is not positive, ask the user for a positive number
            print('That is not a positive number, Please try again: ') 
            #Aske the user again for a positive number
            number = input('Please enter a positive number: ')
            continue
    #If the input is not an integer
    except ValueError:
        #Check if the value entered is a float
        try: 
            #If the input is a float, inform the user that only positive integers are accepted  
            val = float(number)
            print("Input is an float number, only positive integers are accepted.")
            #Ask the user for a valid number
            number = input('Please enter a positive number: ')
            continue
        #If the input is a string
        except ValueError:
            #If the input is a string, inform the user that only positive integers are accepted
            print("This is not a number, its a string. Only positive integers are accepted")
            number = input('Please enter a positive number: ')
            continue
    break
        
#Add the number to the list
allNumbers.append(number) #This is the first number in the collatz series

#Run the program until the number reaches 1
while number !=1: #The series ends when it reaches 1
    if (number % 2) == 0: #Check if number is even
        number = int(number/2) #If even divide by two and reassign to number
        allNumbers.append(number) #Add to the list
    else:
        number = (int(number *3)+1) #If number is not even, then its odd. Multiply it by 3 and add 1 to it.
        allNumbers.append(number) #Add number to the list

print(allNumbers) # print out the list

print('You have reached one, that is the end of the series. Thank you for playing')