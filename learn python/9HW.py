#Write a program that counts from 1 to 10 using a while loop.

a = 1

while  a<=10:
    print(f"Count {a}")
    a +=1
    
    
    

# Create a program that prints all odd numbers between 1 and 20 using a while loop
    
    
num = 1

while num <=20:
    
    if num % 2 != 0:
        num +=1
        continue
    print(f"{num}")
    num+=1
    
    
    # Bus Ticket Booking System

bus_seet = 8
set_no = 0
set_price = 100
total = 0
while bus_seet>0:
    print("book one seet")
    bus_seet -=1
    set_no +=1
    total += set_price    
    print(f"Your seet number is {set_no}, and {bus_seet} are avilabel now ")
    
print ("Sorry we already booked all seets")
print(f"total price is {total}")
    
        
    

# Write a program that counts down from 10 to 1 using a while loop and prints "Happy New Year!" after the countdown is over.


import time

z = 10
x=0
while z <= 10:
    print(f"{z - x}sec.")
    time.sleep(1)
    x += 1
    if x > 10 and x != 10:
        break
print('HAPPY NEW YEAR!')
    