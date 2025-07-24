def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k: "))

print(f"The binomial coefficient of {n} and {k} is {binomial_coefficient(n, k)}")