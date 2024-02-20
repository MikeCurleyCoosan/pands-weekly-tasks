#Write a program that outputs whether or not today is a weekday. The program should be called weekday.py
#Authon: Michael Curley

import datetime

#Get the current date
currentDate = datetime.datetime.now()

#Get the current day of the week
day = currentDate.strftime("%A")
print(day)

#If the day is a weekday, print that it is a weekday
if day == "Saturday" or day == "Sunday":
    print("Its a weekend, yah")
    
else:
    print("yes, unfortunately today is a weekday.")

#References:
    
#https://www.w3resource.com/python-exercises/python-basic-exercise-3.php
    
