def factorial():
    n = int(input("Enter a number: "))
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
print(factorial())

# def factorial(n):
#     return 1 if n <= 1 else n * factorial(n - 1)
# print(factorial(2))