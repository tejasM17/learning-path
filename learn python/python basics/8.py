#                                                     Conditional Statements in Python: if, elif, and else

#  Indentation in Python

# 1. The if Statement

#  The if statement is used to test a condition. If the condition is True, the block of code under the if statement is executed

time = 20  # 20 represents 8 PM in 24-hour format
if time == 20:
    print("It's time for dinner!")
    
    
# 2. The else Statement

time = 18  # 6 PM
if time == 20:
    print("It's time for dinner!")
else:
    print("It's not dinner time yet.")
    
    
#  3. The elif Statement

#  Let’s create a system to check meal times based on the time of the day:

a = 33
b = 33
if b > a:
	print("b is greater than a")
elif a != b:
	print("a and b are not equal")
else :
	print ('none')
    
#    4. Comparison Operators in if Statements
    
    
# ==: Equal to
# !=: Not equal to
#  <: Less than
#  >: Greater than
#  <=: Less than or equal to
#  >=: Greater than or equal to

speed = int(input("enter speed: " ))
limit = 60
if speed > limit :
    print("Warning don't cross the speed limit")

elif speed < limit:
    print("have a good journy")
    
else:
    print("invalid input")
    
    
#    Write a program that takes a number as input and classifies it as:

#     :Positive, Negative, or Zero
#     :Even or Odd

    
    
    
    
a = int( input(" enter a number : "))
b = 0
if a > 0:
    print(" enterd number is positve ")
    
elif a < 0:
    print(" enterd number is negetive ")
    
elif a == 0:
    print(" enterd number is negetive ")
    
elif a % 2 ==0:
    print(" enterd number is even ")
    
elif a % 2 != 0:
    print(" enterd number is odd ")
    
else :
    
    print (" invalid input...! ")
    
    
    
    
    #     5. Logical Operators in if Statements
    
    
    
temperature = 28
is_sunny = False

if temperature > 25 and is_sunny:
    print("It's a hot and sunny day")
elif temperature > 25 and not is_sunny:
    print("It's hot but not sunny")
else:
    print("The weather is moderate")
    
    

  #   6.  Nested if Statements  
    
gen = input("gende : ")
age = int(input("your age : "))

if gen == "female":
    print("ticket is free")
    
else:
    
    if age  < 5:
        print("ticket is free")
    elif age > 5 and age <= 15:
        print("you get a child discount") 
    elif age > 60:
        print("you get a senior sitizen discount")
    else :
        
        print("you pay the full prize")
        
        
#   Login System     
        
        
username = "admin"
password = "1234"

input_username = "admin"
input_password = "1234"

if input_username == username and input_password == password:
    print("Login successful!")
else:
    print("Invalid username or password.")
    
    
#  Discount Eligibility for Shopping


total_purchase = 1200 
is_member = False

if total_purchase > 1000 and is_member:
    print("you get the 20% discount")
    
elif total_purchase > 1000 and not is_member :
    print("you get the 10% discount")

else :
    print("no discount is avilable.")