n = int(input("How many no. do you want to add? "))
total= 0

for a in range(n):
    no = int(input(f"Enter the number {a+1} : "))
    total += no

print(f"The sum of {n} Number is {total}")