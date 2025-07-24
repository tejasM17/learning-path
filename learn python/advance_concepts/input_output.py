# a) Taking Multiple Inputs

a,b,c = map(int,input().split())
print(a,b,c)

# input("Enter three numbers: ") → This function asks the user to enter some text. The text inside "" is a prompt message.

# .split() → This function splits the input based on spaces and creates a list of values.

# map(int, ...) → The map() function converts each value in the list to an integer.

# a, b, c = ... → The converted integers are assigned to the variables a, b, and c.

# print(a, b, c) → This function prints the three values.



# b) reading a input as a list

numbers = list(map(int,input("enter numbers: ").split()))
print(numbers)
print(type(numbers)) # <class 'list'>


# c) using sys.stdin for fast input

import sys
data = sys.stdin.read()
print(data)

# import sys → Imports the sys module (used for system-related operations).

# sys.stdin.read() → Reads all input as a single string.

# print(data) → Prints the collected input.

# Why use this? This is faster than input() when handling large inputs (e.g., competitive programming).




# d) Taking Input as a Dictionary


key = input("Enter key: ").split()
valu = input("Enter valu: ").split()

dictionary = dict(zip(key,valu))

print(dictionary)





#  Advanced Output in Python

# a)


name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# f-string is a string literal that allows you to embed expressions inside curly braces {}.

# b) Using sep and end Parameters

print("python", 'is', "syke", sep='-', end='!!!\n')