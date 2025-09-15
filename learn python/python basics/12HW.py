#  Greet Function: Write a function greet() that takes no arguments and prints a greeting message.


def greet():
    print("Hello! Welcome to the world of Python.")


#  Parameterized Greet: Write a function greet_user() that takes a name as input and prints a custom greeting.


def greet_user(name):
    print(f"Hello, {name}! Welcome to the world of Python.")


# Sum Function: Write a function add_numbers(a, b) that returns the sum of two numbers. Call this function with different values.


def add_numbers(a, b):
    return a + b


# Test the functions
greet()  # Output: Hello! Welcome to the world of Python.
greet_user("TEJAS")  # Output: Hello, Alice! Welcome to the world of Python.
print(add_numbers(5, 3))  # Output: 8
print(add_numbers(10, 7))  # Output: 17



















#  Factorial Function: Write a function factorial(n) that calculates the factorial of a given number n. Call this function with different values.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    # Test the factorial function
print(factorial(5))  # Output: 120
print(factorial(3))  # Output: 6
print(factorial(0))  # Output: 1

    #  Fibonacci Function: Write a function fibonacci(n) that returns the nth Fibonacci number. Call this function with different values.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
            # Test the fibonacci function
print(fibonacci(6))  # Output: 8
print(fibonacci(10))  # Output: 55
print(fibonacci(1))  # Output: 1
