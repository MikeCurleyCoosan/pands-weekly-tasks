#Write a program called collatz.py, that asks the user to input any positive integer and outputs the successive values 
#of the following calculation. At each step calculate the next value by taking the current value and, if it is even,
#divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

number = int(input('Please enter a positive number: '))

if number < 0:
    print('That is not a positive number, Please try again: ')
    number = int(input('Please enter a positive number: '))

print(number)

while number !=1:
    if (number % 2) == 0:
        number = int(number/2)
        print(number)
    else:
        number = (int(number *3)+1)
        print(number)

print('You have reached one, that is the end of the series. Thank you for playing')