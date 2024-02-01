# bank.py
# Week two weekly task
# Author: Michael Curley

a = int(input("Please enter amount in cents: "))
b = int(input("Please enter amoutn in cents: "))
result = float((a + b)/100)
answer = format(result,".2f")

'''
print(result)
'''

print(f"The sum of these is £{answer}")