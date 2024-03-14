#Write a program called plottask.py the displays
# - a plot of a normal distribution of a 1000 values with a mean of 5 and a standard deviation of 2
# - and a plot of the function h(x) = x^3 in the range [0, 10].
# on the one set of axes
#Author: Michael Curley
#Date: 13/03/2024

#Import the required libraries
import numpy as np
import matplotlib.pyplot as plt

#Create an array of 1000 values with a mean of 5 and a standard deviation of 2
normal_distribution = np.random.normal(5, 2, 1000)
print(normal_distribution)

#Create an array of x values from 0 to 10
x_values = np.array(range(0, 11))
print(x_values)

#Create an array of y values which are the cube of the x values
y_values = x_values * x_values * x_values
print(y_values)


#Plot the normal distribution and the function h(x) = x^3 on the same set of axes
plt.hist(normal_distribution, label="Normal Distribution", edgecolor="black")
plt.plot(x_values, y_values, label="h(x) = x^3")
plt.legend()
plt.show()

