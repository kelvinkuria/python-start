# Interpreter: Program that executes other programs.
# Python Shell: An interactive interpreter that can e accessed from the command line 
# Data Type: A specific kind of data 
# Exception: A type of error that can e predicted and handled without causing the program to crash 
# Code Block: Collection of code that is interpreted together
# Function: a named code lock that performs a sequence of actions when it is called.
# Scope: area in your program where a specific variale can e called.



# Data Types

# Strings

"I'm a string"
'Me too'

str('56')

dog_name ="Deck"
print(f"Say hello to my dog {dog_name}")

# created a variale called dog name and assigned a string value Deck to it.
# this stores the dogs name for later use
# print(f'say hello to my {dog_name}')  is used to print the message.
# The f indicates its an f string a special type of string in python that allows for formatted output
# it is used in sring interpolation otherwise youd need to use string concatenation.
# something like print("say hello to  y dog" + dog_name) 
# this method is cumersome and error prone especially in insertion of multiple values or expressions.
# f strings offers a more cleaner and more readale way to emed variales directly into the string.
# Key Points:

# F-strings make string formatting more concise and less error-prone.
# They are especially useful when you need to dynamically insert variables or expressions into strings.
# The f before the quotation mark is essential to tell Python you're using an f-string.

price_1 = 3
price_2 =2.5

print(f"Item 1 costs ${price_1:.2f}")
print(f"Item 2 costs ${price_2:.2f}")