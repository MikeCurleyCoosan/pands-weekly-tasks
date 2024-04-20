#Write a program that reads in a text file and outputs the number of e's it contains. The program should take in the filename
#from an argument on the command line.

#Author: Michael Curley
#Date: 06/03/2024

#https://www.tutorialspoint.com/python/python_command_line_arguments.htm

import sys #import sys module. This module provides access to some variables used or maintained by the interpreter
            #and to some other functions that interact strongly with the interpreter

try: #try to get the filename from the command line, if it is not there, print an error message and exit the program
    FILENAME = sys.argv[1] #sys.argv is a list in Python, which contains the command-line arguments passed to the script.
                            #argv[1] is the argument passed to the script. In this case, it is the filename of the text file
except: #if the filename is not passed as an argument, print an error message and exit the program
    print("Please run the program with a filename as an argument")
    sys.exit()

try:
    with open(FILENAME, "r") as f: #open the file in read mode
        text = f.read() #read the file and store the contents in the variable text
        count = text.count("e") + text.count("E")  #count the number of 'e's in the text file
        print(f"The file {FILENAME} contains {count} 'e's") #print the number of 'e's in the file
except FileNotFoundError:   #catch the FileNotFoundError exception which occurs when the file is not found
    print(f"The file {FILENAME} was not found")
    sys.exit()
except:
    print("An error occurred while reading the file") #catch any other errors that may occur
    sys.exit()

