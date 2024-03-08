# pands-weekly-tasks 2023

![ATU Image](https://www.atu.ie/sites/default/files/styles/homepage_hero/public/2022-03/GMIT-Galway-Campus.jpg?itok=JshYufwh)

## Table of Contents.

* [Week 01 - Hello World](#week-01---hello-world)
* [Week 02 - Bank](#week-02---bank)
* [Week 03 - Accounts](#week-03---accounts)
* [Week 04 - Collats](#week-04---collatz)
* [Week 05 - Weekday](#week-05---weekday)
* [Week 06 - Square root](#week-06---squareroot)


### ***Week 01 - Hello World***

The Hello World program is a traditional first step when learing a new programming language. It allows us to confirm that we have downloaded and setup the tools that we will require over the duration of the course of study, such as cmder and VScode. We created a simple program called helloWorld.py, which basically output the words "Hello World" in the terminal window once the program was run.

- - - -
### ***Week 02 - Bank***

>When Banks are storing currency figures, they store them as integers (usually in cent).This is to avoid rounding errors. 
>Write a program called bank.py
>The program should
>1. Prompt the user and read in two money amounts (in cent).
>2. Add the two amounts.
>3. Print out the amount in a human readable format with a euro sign and decimal point between the euro and cent of the amount.

```
$ python bank.py
```
User Input:
```
Enter amount1(in cent): 65
Enter amount2(in cent): 180
```
Terminal Output:
```
The sum of these is €2.45
```

- - - - 
### ***Week 03 - Accounts***

>Bank account numbers can be stored as 10 character strings, for security reasons some applications only display 
>the last 4 characters (with the other other characters replaced with Xs).
>Write a python program called accounts.py that reads in a 10 character account number and outputs the
>account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

```
$ python accounts.py
```
User Input:
```
Please enter a 10 digit account number: 1234567890
```
Terminal Output:
```
xxxxxx7890
```

- - - - 

### ***Week 04 - Collatz***

>Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
>tAt each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
>Have the program end if the current value is one.

```
$ python collatz.py
```
User Input:
```
Please enter a positive integer: 10
```
Terminal Output:
```
10 5 16 8 4 2 1
```

![Week4-tasks](Week4-tasks.PNG)

- - - - 

### ***Week 05 - Weekday***

>Write a program that outputs whether or not today is a weekday. The program should be called weekday.py
>Search the web to find out how you work out what day it is in python


Example of program running on a Thursday is given below

```
$ python weekday.py
```
```
Yes, unfortunately today is a Weekday
```
Example of program running on a Saturday is as follows
```
$ python weekday.py
```
```
It is the Weekend, yah!
```

![Week5-tasks](Week5-tasks.PNG)

- - - - 


### ***Week 06 - Squareroot***

>Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
>You should create a function called sqrt() that does this.

```
$ python squareroot.py
```
User Input:
```
Please enter a positive number: 14.5
```
Terminal Output:
```
The square root of 14.5 is approx. 3.8
```
<details>
            <summary> Running the program</summary>
<p>
            ![Week6-tasks](Week6-tasks.PNG)
            <img>Week6-tasks.PNG</img>
</p>

</details>

- - - - 
