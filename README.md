
![Banner Image](./Images/Pands_Weekly_Tasks.png)

## Student Name: Michael Curley

![ATU Image](https://www.atu.ie/sites/default/files/styles/homepage_hero/public/2022-03/GMIT-Galway-Campus.jpg?itok=JshYufwh)

<a target="_blank" href="https://docs.python.org/3/tutorial/index.html">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"/>
</a>
<a target="_blank" href="https://www.anaconda.com/">
  <img src="https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white" alt="Anaconda"/>
</a>
<a target="_blank" href="https://numpy.org/devdocs/index.html">
  <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
</a>
<a target="_blank" href="https://pypi.org/project/pandas/">
  <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
</a>
<a target="_blank" href="https://matplotlib.org/">
  <img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" alt="Matplotlib"/>
</a>
<a target="_blank" href="https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax">
  <img src="https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white" alt="Markdown"/>
</a>
<a target="_blank" href="https://www.latex-project.org/">
  <img src="https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white" alt="LaTeX"/>
</a>
<a target="_blank" href="https://code.visualstudio.com/">
  <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="Visual Studio Code"/>
</a>
<a target="_blank" href="https://jupyter.org/">
  <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter Notebook"/>
</a>

-----

_This README has being written with [GitHub's Documentation on README's](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) in mind. You should refer to that documentation for more information on writing an appropriate README for visitors to your 
repository._

_You can find out more about writing in MarkDown in [GitHub Documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)_

-----


## Table of Contents.

* [About this project](#about-this-project)
* [Get Started](#get-started)
* [Week 01 - Hello World](#week-01---hello-world)
* [Week 02 - Bank](#week-02---bank)
* [Week 03 - Accounts](#week-03---accounts)
* [Week 04 - Collats](#week-04---collatz)
* [Week 05 - Weekday](#week-05---weekday)
* [Week 06 - Square root](#week-06---squareroot)
* [Week 07 - Es](#week-07---es)
* [Week 08 - Plottask](#week-08---plottask)
* [References](#references)

## ***About this project***

This repository contains the weekly tasks that were undertaken as part of the 'Programming and Scripting' Module in the Higher Diploma in Data Analytics course at ATU Galway in the year 2024.

### Get Started


1. Clone the repository to your local machine. 

```sh
git https://github.com/MikeCurleyCoosan/pands-weekly-tasks.git

```
2. Download and install [Anaconda](https://www.anaconda.com/). Anaconda comes with its own set of pre-installed data science packages and tools, making it convenient for
beginners to set up their environment quickly. The pre-installed packages that are required to work with the project are [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/) and [Matplotlib](https://matplotlib.org/).

3. Download and install [Visual Studio Code](https://code.visualstudio.com/). Visual Studio Code is a code editor with support for development operations like debugging,
task running, and version control.

4. Download and install the latest version of [Git](https://git-scm.com/). Git is a free and open source version control system designed to handle everything from small 
very large projects with speed and efficiency.

5. Navigate to the project directory in VS Code

6. Navigate to the folder of the weekly task you would like to run.

7. Copy the script in the "Running the program" section on this page and paste into the terminal window in VS Code. The program should now run.


### ***Week 01 - [Hello World](https://github.com/MikeCurleyCoosan/pands-weekly-tasks/blob/main/helloWorld.py)***

The Hello World program is a traditional first step when learing a new programming language. It allows us to confirm that we have downloaded and setup the tools that we will require over the duration of the course of study, such as [cmder](https://cmder.app/) and [Visual Studio Code](https://code.visualstudio.com/). We created a simple program called helloWorld.py, which basically output the words "Hello World" in the terminal window once the program was run.

![Week1-tasks](Images/Week1-tasks.PNG)

- - - -
### ***Week 02 - [Bank](https://github.com/MikeCurleyCoosan/pands-weekly-tasks/blob/main/bank.py)***

>When Banks are storing currency figures, they store them as integers (usually in cent).This is to avoid rounding errors. 
>Write a program called bank.py
>The program should
>1. Prompt the user and read in two money amounts (in cent).
>2. Add the two amounts.
>3. Print out the amount in a human readable format with a euro sign and decimal point between the euro and cent of the amount.

The user is asked "Enter amount1(in cent)", and then to "Enter amount 2(in cent). To ensure we are not recieving string inputs or floating point inputs the code has being refactored to inclued a try/except block. This block will inform the user if he has entered a string or a float for either amounts, and will advise if a negative number has being entered for either amount also.. The two inputs are then added together to find the total amount in cents, which will be converted to euros by either of two methods. The first method is not recommended as dealing with floats in python can produce some undesirable results.  

Method 2 is the recommended way of dealing with this type of problem in python. Here we are using [floor division](https://stackoverflow.com/questions/183853/what-is-the-difference-between-and-when-used-for-division), and the [modulus operator](https://realpython.com/python-modulo-operator/). The floor division divides the first amount by the second amount and rounds the result down to the nearest whole number. This will give us our euro part of the solution. The modulus operator will return the remainder of dividing the first amount by the second amount, and will therefore compute the cent equivalent. 

![Week2-tasks](Images/Week2-tasks.PNG)

<details>
            <summary>Running the program</summary>

<p>

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

</p>

</details>

- - - - 
### ***Week 03 - [Accounts](https://github.com/MikeCurleyCoosan/pands-weekly-tasks/blob/main/accounts.py)***

>Bank account numbers can be stored as 10 character strings, for security reasons some applications only display 
>the last 4 characters (with the other other characters replaced with Xs).
>Write a python program called accounts.py that reads in a 10 character account number and outputs the
>account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

This program was re-written multiple times to give the final program presented here. A number of issues were encountered while writting this program. Firstly, if the bank account number contained leading zeros, such as 000******, these leading zeros were being removed by python, so this meant that even if you entered a 10 digit account number as above, it was being recognised as a 7 digit number and you were being prompted "The account number is less than 10 digits long, please enter a valid 10 digit account number". This problem was overcome by casting the account number entered to a string value, and getting the length of this string, after firstly checking that the number entered was in fact an integer value.

A second problem encountered when creating this program was that the program was not checking if floating point numbers or strings were being entered at the command prompt by the user. A try/except statement was added to the program later to ensure that only integers would be accepted by the program. If the user enters a floating point number, they are prompted "Input is a float number, account numbers should contain integers only". If a string value was entered they were prompted "This is not a number, its a string. Please enter a valid 10 digit account number.

An if statement was used to ensure that the account number entered was at least 10 numbers in length. This can be changed to accept numbers of any length at the users disgression.

![Week3-tasks](Images/Week3-tasks.PNG)

<details>
            <summary>Running the program</summary>

<p>

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

</p>

</details>

- - - - 

### ***Week 04 - [Collatz](https://github.com/MikeCurleyCoosan/pands-weekly-tasks/blob/main/collatz.py)***

>Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
>At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
>Have the program end if the current value is one.

The above problem is known as the [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture), one of the most famous unsolved problems in mathematics. The conjecture asks whether repeating two simple arithmetic operations will eventually transfrom every positive integer into 1.

The user is asked "Please enter a positive integer" to start, which will be stored in the variable number. A if statement is used to confirm that the user has actually entered a positive number. If the user has not entered a positive integer, the program will prompt the user "That is not a positive number, Please try again", and ask the user to "Please enter a positive number" again. 

Once a positive integer has being entered this will be appended to our list allNumber, as the start of our collatz series. 

A while statement is then used to complete either of the two mathematical calculations on the current number while the number is not equal to 1, and apend the new result to our list. The result will be stored in our variable number, and the program will continue until the result of the calculations in the if/else loop result in 1.

When we reach 1 all the numbers in the list which make up our collatz conjecture for the number the user entered, will be printed to the screen, along with the message "You have reached one, that is the end of the series. Thank you for playing".

![Week4-tasks](Images/Week4-tasks.PNG)

<details>
            <summary>Running the program</summary>

<p>

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
</p>

</details>



- - - - 

### ***Week 05 - [Weekday](https://github.com/MikeCurleyCoosan/pands-weekly-tasks/blob/main/Weekday.py)***

>Write a program that outputs whether or not today is a weekday. The program should be called weekday.py
>Search the web to find out how you work out what day it is in python

The [datetime module](https://docs.python.org/3/library/datetime.html#module-datetime) was used in order to manipulate the date and time in this programme. A good reference on using the module to manipulate the date and time can be found on the [note.nkmk.me](https://note.nkmk.me/en/python-datetime-now-today/) website. The program does not require any input from the user, it determines the current date, and then determines what day of the week it is from this. The module can return the current day in various forms, but I have chosen to return the day using its full Weekday name. An if statement then determines whether the day is a weekday or a day of the weekend. The program has been tested on a weekday and during the weekend to ensure that it works in both cases.

![Week5-tasks](Images/Week5-tasks.PNG)

![Week5-tasks2](Images/Week5-task2.PNG)


<details>
            <summary>Running the program</summary>

<p>
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

</p>

</details>



- - - - 

### ***Week 06 - [Squareroot](https://github.com/MikeCurleyCoosan/pands-weekly-tasks/blob/main/squareroot.py)***

>Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
>You should create a function called sqrt() that does this.

In order to be able to complete this program, we had to become familiar with the [Newton Method](https://en.wikipedia.org/wiki/Newton%27s_method). This in itself was a very time consuming task, and required a lot of research. Along with the above link, I found the following [YouTube Video](https://www.youtube.com/watch?v=gNb-H50zmRY) a great source of information to fully understand this method. [Stack overflow](https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm) also gives an excellent overview from a progmamming point of view of implementing the newton method in the Python programming language.

Ultimately, to find the square root of a positive floating point number required implementing the mathematical formula which has being derived to approximate the square root of any positive number.

A while loop has being used to ensure that a positive number(n) is entered, and a try/catch block is used to ensure that the program can deal with negitive numbers and strings. The program is designed to ask the user for the number of iterations(i) that they would like to approximate the square root to. You can enter as many iterations as you would like. Perhaps, another approach that could have being taken would have being to keep approximating the root until the new approximation is equal to the last approximation within a number of decimal places. 

![Week6-tasks](Images/Week6-tasks.PNG)

<details>
            <summary> Running the program</summary>
<p>
           
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

</p>

</details>

- - - - 


### ***Week 07 - [Es](https://github.com/MikeCurleyCoosan/pands-weekly-tasks/blob/main/es.py)***

>Write a program that reads in a text file and outputs the number of e's it contains.
>The program should take the filename from an argument on the command line.

This program has been designed to read a text file called by the user from the command line. In order to do this we have made the assumption that the file will be in the same directory as the program that is reaing the number of 'e's it contains. I have downloaded a copy of Dante's Divine Comedy and added this to the same diretory as the program for testing purposes. This file is saved as DivineComedy-Dante.txt. The [sys module](https://docs.python.org/3/library/sys.html) module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available. The submodule sys.argv deals with command line arguments passed to a Python script. The sys.argv[0] contains the python script name, and therefore the text filename needs to be held in the second argument sys.argv[1]. I found the [Tutorials Point](https://www.tutorialspoint.com/python/python_command_line_arguments.htm) website an invaluable resourse when completing this task. The website describe the sys module in great details.

We need to import the sys module into our program in order to use its functionality. 



![Week7-tasks](Images/Week7-tasks.png)

<details>
            <summary> Running the program</summary>
<p>
           
```
$ python es.py DivineComedy-Dante.txt
```

Terminal Output:
```
The file DivineComedy-Dante.txt contains 8334 'e's
```

</p>

</details>

- - - - 

### ***Week 08 - [Plottask](https://github.com/MikeCurleyCoosan/pands-weekly-tasks/blob/main/plottask.py)***

>Write a program called plottask.py that displays:
>
> - a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
> - and a plot of the function  h(x)=x3 in the range 0 to 10, 
>
>on the one set of axes.

This task was assigned as an introduction to [matplotlib](https://matplotlib.org/), which is a plotting library for the Python programming language, and is usually used in conjunction with its numerical mathematics extension [NumPy](https://numpy.org/). Numpy is a library for the Python programming language, which allows us to work with large multi-dimensional arrays and matrices. It also supplies a large collection of high-level mathematical functions to operate on these arrays. [NumPy Wikipedia](https://en.wikipedia.org/wiki/NumPy)

Both these libraries were imported so that we could use them for our purposes. To calculated 1000 values with a normal distribution with a mean of 5 and a standard deviation of 2, the Numpy [random.normal()](https://numpy.org/devdocs/reference/random/generated/numpy.random.normal.html) function was called upon. This function allows us to draw random samples from a normal (Gaussian) distribution where three parameters are passed into the function. These three parameters are loc, scale and size, where loc=mean and the scale=standard deviation and size=number of samples required. If no size attribute is pased into the function just one value is returned to the user. The mean is the 'centre' of our distribution and the standard deviation is the 'spread' or 'width' of the distribution.

The matplotlib.pyplot library was then used to plot this distribution as a histogram, with the default number of bins being used (default for Matplotlib is 10). We used the object orientated approach here, to create an instance of the subplots class. We applied variable names fig, ax to the figure and axes instances created when an instance of the subplots class is called. Various functions are then availabe to us and for our purposes we used the ax.set_xlabel, ax.set_ylabel, and ax.grid functions to improve the appearance of our plots.

To create an array of values for h(x) = x^3 in the range 0-10, the Python range function range(0,11) was used to create x_values between 0 and 10. These values were passed to the Numpy array function np.array() to create a Numpy Array of values between 0 and 10. We then created the x^3 array by creating another variable y_values and storing the values y_values = x_values * x_values * x_values in this array. We simply plotted this using the Matplotlib plot() function. 

As both plots had to be plotted on the one axis when the h(x) = x^3 function was plotted it skewed the histogram plot. I decided therefore to use the ax2 = ax1.twinx() function available to us in Matplotlib which creates a second y-axis and allows us to view both plots on the one Axis in a much nicer way.

![Week8-tasks](Images/normal_distribution_and_x_cubed.png)


<details>
            <summary> Running the program</summary>
<p>
           
```
$ python plottask.py
```
</p>

</details>

- - - -

### References

- Reference #1: https://www.w3schools.com/python/python_casting.asp
- Reference #2: https://stackoverflow.com/questions/183853/what-is-the-difference-between-and-when-used-for-division
- Reference #3: https://realpython.com/python-modulo-operator/
- Reference #4: https://realpython.com/python-strings/#string-operators
- Reference #5: https://en.wikipedia.org/wiki/Collatz_conjecture
- Reference #6: https://www.educative.io/answers/how-to-generate-the-collatz-sequence-in-python
- Reference #7: https://medium.com/@chakshugupta774/exploring-the-collatz-conjecture-with-python-7c5d9f31d233
- Reference #8: https://docs.python.org/3/library/datetime.html#module-datetime
- Reference #9: https://note.nkmk.me/en/python-datetime-now-today/
- Reference #10: https://www.shecodes.io/athena/10185-how-to-check-what-day-of-the-week-it-is-in-python#:~:text=date%20using%20datetime.-,datetime.,
- Reference #11: https://ioflood.com/blog/python-get-current-date/#:~:text=To%20get%20the%20current%20date%20in%20Python%2C%20you%20can%20use,function%20from%20the%20datetime%20module.
- Reference #12: https://en.wikipedia.org/wiki/Newton%27s_method
- Reference #13: https://www.youtube.com/watch?v=gNb-H50zmRY
- Reference #14: https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm
- Reference #15: https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
- Reference #16: https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html#newton-s-method
- Reference #17: https://docs.python.org/3/library/sys.html
- Reference #18: #https://www.tutorialspoint.com/python/python_command_line_arguments.htm
- Reference #19: https://realpython.com/working-with-files-in-python/
- Reference #20: https://www.youtube.com/watch?v=rJCl7t3IIbA
- Reference #21: https://www.w3schools.com/python/numpy/numpy_random_normal.asp
- Reference #22: https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/
- Reference #23: https://realpython.com/how-to-use-numpy-arange/


