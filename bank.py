# bank.py
# Week two weekly task
# Author: Michael Curley

#Question When Banks are storing currency figures, they store them as integers (usually in cent).This is to avoid rounding errors. 

#Write a program called bank.py 

#The program should:

'''
Prompt the user and read in two money amounts (in cent)
Add the two amounts
Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
$ python bank.py
Enter amount1(in cent): 65
Enter amount2(in cent): 180
The sum of these is €2.45
'''

#Run the program until the user enters two integer values for the amounts of money in cents
while True:
    #Ask the user to enter two amounts of money in cents
    a = input("Enter amount1(in cent): ")
    b = input("Enter amount2(in cent): ")
    #Check if the inputs that the user entered are integer
    try:
        #If the inputs is integers, 
        number_as_int = int(a)
        number_as_int2 = int(b)
        #Check if they are less than zero.....ie negative
        if number_as_int < 0 or number_as_int2 < 0:
            #If they are less than zero, ask the user for a valid number
            print("At lease one of those number is less than 0, please enter a valid numbers")
            continue
        #If the inputs are integers and greater than zero
        else:
            #Add the two numbers
            result = (number_as_int + number_as_int2)/100 # Not the recommended way to do this but we have ensured that the input is an integer
                                                            #Before adding the try catch block I used the recommended method which is commented out below
            
            answer = format(result,".2f") #Format the result to two decimal places              
            #Print the result
            print(f"The sum of these is €{answer}")

        break;
    #If the input is not an integer the following code will run
    except ValueError:
        #Check if the value entered is a float
        try:
            #If the input is a float, ask the user for a valid number
            val = float(a)
            val2 = float(b)
            #If the input is a float, ask the user for a valid number
            print("At least one of those numbers is a float, please enter a valid number")
            continue
        #Otherwise the input is a string, and the following block of code will run
        except ValueError:
            #If the input is a string, ask the user for a valid number
            print("At least one of those numbers is a string, please enter a valid number")
            continue


#A second solution not using floats which are prone to inaccuracy. Solution taken from The python tutorial.

#Disgard the fractional part using floor division
#c = ((a + b) // 100)

#Use the % operator to the the remainder of the division
#d = ((a+b) % 100)

#answer2 = print('The sum of these is €{}.{}'.format(c,d))