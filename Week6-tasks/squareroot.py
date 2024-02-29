#Date: 29-Feb-2024
#Author: Michael Curley

#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root. 
#You should create a function called sqrt that does this.

#you must create your own function and cannot use the built in functions x** .5 or math.sqrt(x).

#You should use Newton's method to find the square root.


#To start we can use the following formula x_new = 0.5 * (x + n / x) where x is starting point, and n is the number we are taking the square root of.

#This approximation is good for positive whole numbers, but not for floating point numbers. This method is explained here:
# https://www.youtube.com/watch?v=gNb-H50zmRY

#The following is a snippet from the video:
# The idea is to start with an initial guess which is not very far from the actual square root.
# Then we use this initial guess to find an even better guess.
# We keep doing this until we are as close as we want to be."

def sqrt(n,i):

    #Initial guess for the square root
    x = n/2 #An approximate guess would be half of the number
    #The formula to find the square root
    while i > 0:
        x = 0.5 * (x + n / x)
        i -= 1
    return x

#Main program
n = float(input("Please enter a positive number: "))
i = int(input("Please enter the number of iterations: "))
print(f"The square root of {n} with {i} iterations is approximately {sqrt(n, i)}")


