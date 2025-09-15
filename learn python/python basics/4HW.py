
#  Homework
# 1. Write a Python program that takes two numbers as input from the user and checks if:

#a. Both numbers are greater than 10 (using and).

a = int(input ( "enter first number: "))
b = int(input  ("enter second number: "))

print (a>10 and b>10)

#b. At least one of the numbers is less than 5 (using or).

c = int(input("1st number:- "))
d = int(input("2nd number:- "))

print (c<5 or d<5)

#c. The first number is not greater than the second (using not).

e = int(input("1st no.- "))
f = int(input("2nd no.- "))

print (not(e>f))

# 2. Comparison Operator Challenge: Create a Python program that asks the user for their age and prints:

#a. "You are an adult" if the age is greater than or equal to 18.

x = int(input("Enter youur age : "))
y = 18

if x >= y:

    print ("You are an adult")
    
    #b. "You are a minor" if the age is less than 18.
    
elif x < y :
    print("You are a child") 
    
# 3. Membership Operator Exercise: Write a Python program that:

#a. Takes a string as input from the user.

a = input ("enter your words : ")

#b. Checks if the letter 'a' is in the string (using in).

if "a" in a :
    print ("letter 'a' is in the string")
    
else:
    print("string doesn't contain letter 'a'")

#c.Checks if the string doesn't contain the word "Python" (using not in).
if "python" not in a :

    print ("string doesn't contain the world")
    
else:
    print ("string doesn't contain the world 'python'.")
    
    # 4. Bitwise Operator Task: Given two integers, write a Python program that:
    
m = 7      # in binary: (111)
n = 5     # in binary: (101)
    
#bitwise and 
print (m & n)   # out put : 5 (binery : 101)

#bitwise or
print (m | n)   # out put : 7 (binery : 111)

#bitwise Ex-or
print (m ^ n)   # out put : 5 (binery : 101)

#bitwise not 
print (~m)      # out put : -8(binery : invert of 1000)

#bitwise left shift
print (m << 1)  # out put : 5 (binery : 1110)

#bitwise right shift
print (m >> 1)  # out put : 5 (binery : 011)



lst = ["a",12,"teja",999]

lst.append("NOOb")
lst.insert(1,"added")
print(lst)
lst.remove(lst[2])
print(lst)