#  Write a program to check if someone is eligible for a bus pass. If they are below 5 years, the bus pass is free. If they are 60 years or older, they get a senior citizen discount. Otherwise, they pay the full price.

# Here's a Python program to check if someone is eligible for a bus pass based on the given criteria:

bus_pass_age = int(input("Enter your age: "))


if  bus_pass_age <= 5:
    print("Bus pass is free.")
elif bus_pass_age >= 60:
    print("you have senior citizen discount.")
else:
    print("you must pay the full price.")
    
# #  Create a program that checks the time of day (24-hour format) and prints whether it's time for breakfast, lunch, or dinner.
# Breakfast: 8 AM
# Lunch: 1 PM
# Dinner: 8 PM
# If none of these times, print "It's not meal time."

time = int(input("Enter the time : "))

if time == 8:
    print("It's time for breakfast.")
elif time==1:
    print("It's time for lunch.")
elif time==8:
    print("It's time for dinner.")
else:
    print("It's not meal time.")
    
    
    
# Write a program that checks whether a person is eligible for a library membership. If they are under 18, they get a student membership. If they are 60 or older, they get a senior citizen membership. Otherwise, they get a regular membership.
    
age = int(input("Enter your age: "))
if age < 18:
    print("Student membership.")
elif age >= 60:
    print("Senior citizen membership.")
else:
    print("Regular membership.")
