#Date: 29-Feb-2024
#Author: Michael Curley

#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. 
#You should create a function called sqrt that does this.

#you must create your own function and cannot use the built in functions x** .5 or math.sqrt(x).

#You should use Newton's method to find the square root.


#To start we can use the following formula x_new = 0.5 * (x + n / x) where x is starting point, and n is the number we are taking the square root of.

#This approximation is good for positive whole numbers, but not for floating point numbers. This method is explained here:
#https://www.youtube.com/watch?v=gNb-H50zmRY

#The following is a snippet from the video:
# The idea is to start with an initial guess which is not very far from the actual square root.
# Then we use this initial guess to find an even better guess.
# We keep doing this until we are as close as we want to be."

def sqrt(n,i):

    #Initial guess for the square root
    x = n/2 #An approximate guess would be half of the number
    #The formula to find the square root
    while i > 0:    #Keep iterating until the number of iterations is 0
        x = 0.5 * (x + n / x)   #The formula to find the square root using Newton's method
        i -= 1  #Decrement the number of iterations
    return x    #Return the square root

#The following is another example using the above formula to find the square root using Newton's method
#This method is used on Stack Overflow: https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm
#The difference is that the following method defines the variable differently and keeps iterating until the new guess is the same as the old guess

def my_sqrt(n):
    approx = n/2 #An approximate guess would be half the number as before
    closer = (approx + n/approx)/2 #The formula to find the square root using Newton's method
    while closer != approx: #Keep iterating until the new guess is the same as the old guess
        approx = closer #The new guess becomes the old guess
        closer = (approx + n/approx)/2  #The formula to find the square root using Newton's method
    return approx   #Return the square root



#Main program
n = float(input("Please enter a positive number: "))
while n < 1:    #Keep asking for a number until a positive number is entered
        print("That was not a positive number. Please try again.")
        n = float(input("Please enter a positive number: "))

i = int(input("Please enter the number of iterations you would like the program to undertake: "))
while i is not int:
    print("That was not a number. Please try again.")
    i = int(input("Please enter the number of iterations you would like the program to undertake: "))
    
print(f"The square root of {n} with {i} iterations is approximately {sqrt(n, i)}")
print(f"The square root of {n} using the second method is {my_sqrt(n)}")
