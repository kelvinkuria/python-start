# Interpreter: Program that executes other programs.
# Python Shell: An interactive interpreter that can e accessed from the command line 
# Data Type: A specific kind of data 
# Exception: A type of error that can e predicted and handled without causing the program to crash 
# Code Block: Collection of code that is interpreted together
# Function: a named code lock that performs a sequence of actions when it is called.
# Scope: area in your program where a specific variale can e called.



# Data Types

# Strings

# "I'm a string"
# 'Me too'

# str('56')

# dog_name ="Deck"
# print(f"Say hello to my dog {dog_name}")

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

# price_1 = 3
# price_2 =2.5

# print(f"Item 1 costs ${price_1:.2f}")
# print(f"Item 2 costs ${price_2:.2f}")


# Variable Assignment:

# price_1 = 3 and price_2 = 2.5 assign numerical values to two variables named price_1 and price_2. These variables likely represent the prices of two items.
# f-Strings for Price Display:

# print(f"Item 1 costs ${price_1:.2f}") and print(f"Item 2 costs ${price_2:.2f}") are the lines that print formatted price information using f-strings. Here's a detailed explanation:
# f-string: The f before the opening quotation mark indicates that it's an f-string. F-strings are a powerful way to combine text and variables or expressions within strings.
# Text and Variable: The string includes fixed text like "Item 1 costs $" and "Item 2 costs $". The $ symbol is likely there for display purposes.
# Curly Braces ({}) and Variable: Inside the curly braces {}, you have the variable names price_1 and price_2 respectively. These placeholders will be replaced with the actual values stored in those variables.
# Formatting Specifier (:.2f): The part .2f after the variable name is a formatting specifier. It instructs Python on how to format the number inserted from the variable. In this case:
# : introduces the formatting options.
# .2 specifies that you want exactly 2 decimal places. So, even if a price has no decimal places (like 3 for price_1), it will be displayed with two zeros after the decimal point (e.g., "3.00").
# Output:

# When you run this code, it will produce the following output:

# Item 1 costs $3.00
# Item 2 costs $2.50
# The f-strings ensure that the prices are displayed with two decimal places for consistency and readability, even if one of the prices is a whole number.

# In Summary:

# F-strings provide a clean way to embed variables and expressions within strings for formatted output.
# Curly braces {} act as placeholders for variables.
# Formatting specifiers like .2f control how numbers are displayed (e.g., number of decimal places).


#  Strings as Objects:

# In Python, everything is treated as an object, even simple things like the text "hello". This means they have properties and methods associated with them.
# 2. String Methods:

# The code shows how to call various methods on the string "hello". Here's what each method does:
# upper(): Converts all characters in the string to uppercase.
# lower(): Converts all characters in the string to lowercase.
# capitalize(): Makes the first letter uppercase and the rest lowercase.
# +: Concatenates (joins) two strings together.
# *: Repeats a string a certain number of times.
# 3. Checking String Type:

# The type("hello") line uses the type() function to reveal that "hello" is a <class 'str'> object, confirming it's a string.
# 4. Exploring All String Methods:

# The dir("hello") line displays a long list of all the methods available for strings. You might recognize some methods from the previous examples, like upper and lower. This is just a small sampling of the many string methods in Python!
# Key Points:

# Strings in Python are versatile and offer various methods to manipulate text.
# These methods don't modify the original string but instead return a new string with the changes applied.


# Numbers

# Integers are whole numbers, like 7.

# Floats are decimal numbers, like 7.3.

# You can convert some other data types to integers or floats with the int() and float() class constructor functions:

# int("1")
# # => 1
# int(1.1)
# # => 1
# float("1.1")
# # => 1.1


# Sequence Types
# Python has a number of different data types that are useful for storing data. Each of these types can store any type of data inside; what differs between them are the rules for organizing and accessing the data.
# Lists
# There are a number of ways to create a list. Just like with creating strings, you can use the literal constructor or the class constructor.

# [1, 3, 400, 7] is a list of integers. Any set of comma separated data enclosed in brackets is a list. So, by simply writing something like the above, you can create a list:

# [1, 3, 400, 7]
# # => [1, 3, 400, 7]
# You can also create an list with the list() syntaxLinks to an external site.. Just typing list() will create an empty list ([]):

# list()
# # => []
# In order to access a specific element in a list, you will need to know its index, or the place it occupies in the list. Indices start at 0 and move up by 1 with each subsequent element. Once the index is known, the element can be accessed using square brackets and the index.

# list_abc = ['a','b','c']
# list_abc[0]
# # => 'a'
# list_abc[1]
# # => 'b'
# list_abc[2]
# # => 'c'
# There are many ways to operate on lists and on each individual item, or element, within an list. Later on in the course, we'll learn about methods for iterating over lists (as with the .forEach, .map, etc methods in JavaScript). For now, we'll preview a few list functions and methods, and you can check out more hereLinks to an external site..

# len([1, 3, 400, 7])
# # 4
# sorted([5, 100, 234, 7, 2])
# # [2, 5, 7, 100, 234]
# list_123 = [1, 2, 3]
# list_123.pop()
# # 3
# list_123.remove(1)
# print(list_123)
# # [2]

# list_abc = ['a','b','c']
# list_abc[0]

# len([1,2,3,4,5])

# sorted([]65,68,5,4,321,3)

# list_123.pop()


# Tuples
# Tuples are nearly identical to lists, with two key differences:

# First, tuples are created with open and close parentheses (in place of square brackets). The tuple() class constructor function can also be used to cast lists and other iterable data types to tuples.

# (1, 2, 3)
# # => (1, 2, 3)
# tuple([1, 2, 3])
# # => (1, 2, 3)
# Second, tuples are immutable. This means that once a tuple has been created, the tuple itself cannot be changed. Python functions that work on lists to create new data will still work on tuples, but tuples do not contain methods like .pop() and .insert() that would change their contents.

# While tuples are less flexible than lists, this can prove advantageous in certain situations. The most common situation where you will see tuples while at Flatiron will be in data retrieved from a database. Since you want to keep an accurate record of what is in the database while your application works with the data, a tuple will protect that information until it is no longer needed.

# NOTE: Parentheses can also be used for order of operations and grouping statements. To let Python know that it's looking at a tuple, there has to be at least one comma- even in tuples with only one element: (1,).
#  fruits_tuple = ('apple',"vinegar","cider")

# num_list = [1,2,3,4,5,6]
# nums_tuple=tuple(num_list)


# my_set = {1,2,3,4,4,4,4,5}
# print(my_set)


# num_list = [1,2,3,4,5,6,7,3,2,1,4,5,44,2,3,44,5,6,7]
# uniq_num = set(num_list)
# print(uniq_num)

# my_dict = {"name":"Kuria" , "Age": "24", "status":"married", "likes":["reading","coding"]}

# print(my_dict["Age"])

# no_value = ""
# print(no_value)

# def greet(name):
#     print("Hello,", name + "!")
# greet('Kuria')


# def add(s,y):
#     return s+y
# result = add(5,3)
# print(result)

# def multiply(l,w):
#     return l*w
# result = multiply(6,8)
# print (result)

# def is_even(num):
#     return num % 2 == 0
# print(is_even(9))



# age = int(input("Enter your age: "))

# if age >= 18:
#     if age <= 24:
#        print("You are eligile too vote.consider registering to vote")
#     else:
#        print("You can vote!")
# else:
#     print("You cant vote sucka#")



# grade = int(input("Enter your grade: "))

# if grade >= 90:
#     print("Grade: A   (Excellent!)")
# elif grade >= 80:
#     print("Grade B (Very Good)")
# elif grade >= 70:
#     print("Grade C (Good)")
# elif grade >= 60:
#     print("Grade D(Work harder!)")
# else:
#     print("FAIL")




# grade = input("Enter your grade A,B,C,D or F:  ").upper()

# if grade == 'A': 
#     print('Excellent')
# elif grade == 'B':
#     print ("Good")

# else:
#     if grade in("C","D"):
#         print('Improvement Needed')
#     else:
#         print("You may need to retake a course")


# age = 20

# is_adult = "Adult" if age >=18 else "Minor"

# print(is_adult)


# . Introduction to Exception Handling

# What are exceptions?
# Exceptions are events that disrupt the normal flow of program execution. They can occur due to various reasons like division by zero, accessing a non-existent index in a list, or network errors.
# Why handle exceptions?
# Unhandled exceptions can crash your program, leading to unexpected behavior and frustrating user experiences. Exception handling allows you to gracefully manage errors, provide informative messages, and continue program execution whenever possible.

try :
    num = int(input("Enter a num"))
    result= 10/num
except ZeroDivisionError:
    print("Cannot divide y zero")
except ValueError:
    print("Enter the correct values")