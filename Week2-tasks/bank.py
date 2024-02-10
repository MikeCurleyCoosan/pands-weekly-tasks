# bank.py
# Week two weekly task
# Author: Michael Curley

#Question When Banks are storing currency figures, they store them as integers (usually in cent).This is to avoid rounding errors. 

#Write a program called bank.py 

#The program should:

'''Prompt the user and read in two money amounts (in cent)
Add the two amounts
Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
$ python bank.py
Enter amount1(in cent): 65
Enter amount2(in cent): 180
The sum of these is €2.45'''

#First attempt using a float value after reading in two amounts in cents as integers.

a = int(input("Please enter amount in cents: "))
b = int(input("Please enter amoutn in cents: "))
#If we add these values and divide by 100 we get a float result therefore we need to declare our result as a float
result = float((a + b)/100)
#Format our answer to two decimal places.
answer = format(result,".2f")

'''
print(result) # Just for test purposes
'''

print(f"The sum of these is €{answer}")

#A second solution not using floats which are prone to inaccuracy. Solution taken from The python tutorial.

#Disgard the fractional part using floor division
c = ((a + b) // 100)

#Use the % operator to the the remainder of the division
d = ((a+b) % 100)

answer2 = print('The sum of these is €{}.{}'.format(c,d))