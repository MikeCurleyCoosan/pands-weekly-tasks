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
print(normal_distribution)

#Create an array of x values from 0 to 10
x_values = np.array(range(0, 11))
print(x_values)

#Create an array of y values which are the cube of the x values
y_values = x_values * x_values * x_values
print(y_values)

#Set the font styles
font1 = {'family': 'serif', 'color': 'blue' , 'size':20}
font2 = {'family': 'serif', 'color': 'darkred' , 'size':15}


#Plot the normal distribution and the function h(x) = x^3 on the same set of axes
plt.hist(normal_distribution, label="Normal Distribution", edgecolor="black")
plt.plot(x_values, y_values, label="h(x) = x^3")
plt.legend()
plt.title('Normal Distribution and h(x) = x^3', fontdict=font1)
plt.xlabel('x', fontdict=font2)
plt.ylabel('h(x)= x^3', fontdict=font2)
plt.grid(color = 'c', linestyle = '--', linewidth = 1)
plt.savefig('normal_distribution_and_x_cubed.png')
plt.show()

