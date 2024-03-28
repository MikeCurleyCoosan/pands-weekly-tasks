#Write a program called plottask.py the displays
# - a plot of a normal distribution of a 1000 values with a mean of 5 and a standard deviation of 2
# - and a plot of the function h(x) = x^3 in the range [0, 10].
# on the one set of axes

#Author: Michael Curley
#Date: 13/03/2024

#Import the required libraries
import numpy as np
import matplotlib.pyplot as plt

#Setting up the variables
mean = 5
std_dev = 2
number_of_values = 1000

#Create an array of 1000 values with a mean of 5 and a standard deviation of 2
normal_distribution = np.random.normal(loc=mean, scale=std_dev, size=number_of_values)

'''
print(normal_distribution) #Added for testing purposes
''' 

#Create an array of x values from 0 to 10
x_values = np.array(range(0, 11))

'''
print(x_values)#Added for testing purposes
''' 

#Create an array of y values which are the cube of the x values
y_values = x_values * x_values * x_values
'''
print(y_values) #Added for testing purposes
''' 

#Set the font styles
font1 = {'family': 'serif', 'color': 'blue' , 'size':20} #Set the font style, font family, font color and font size
font2 = {'family': 'serif', 'color': 'darkred' , 'size':15}


#Plot the normal distribution and the function h(x) = x^3 on the same set of axes
plt.hist(normal_distribution, label="Normal Distribution", edgecolor="black") #Plot the normal distribution, set the edge color to black
plt.plot(x_values, y_values, label="h(x) = x^3")
plt.legend() #Show the legend
plt.title('Normal Distribution and h(x) = x^3', fontdict=font1) #Title the plot, set the font style
plt.xlabel('x', fontdict=font2)
plt.ylabel('h(x)= x^3', fontdict=font2)
plt.grid(color = 'c', linestyle = '--', linewidth = 1) #Add a grid to the plot, set the color to cyan, the line style to dashed and the line width to 1
plt.savefig('../Images/normal_distribution_and_x_cubed.png') #Save the plot to a file
plt.show()

