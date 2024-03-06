#Write a program that outputs whether or not today is a weekday. The program should be called weekday.py
#Authon: Michael Curley

import datetime #The module datetime provides classed for manipulating dates and times

#Get the current date
currentDate = datetime.datetime.now() #datetime.datetime.now() returns the current date and time

#Get the current day of the week strftime() method returns a string representing using date, time or datetime object
day = currentDate.strftime("%A") #%a Abbreviated weekday name, %A Full weekday name, %w Weekday as a decimal number, 
print(day)

#If the day is a weekday, print that it is a weekday
if day == "Saturday" or day == "Sunday":
    print("Its a weekend, yah")
    
else:
    print("yes, unfortunately today is a weekday.")

#References:
    
#https://www.w3resource.com/python-exercises/python-basic-exercise-3.php
    
