#   SWAPING VARIABLE VALUSE

x,y = 5,10

print(f"before swaping X:{x} and Y:{y}")

# y,x = 5,10

#  or 

# z = x
# x = y
# y = z

# or

# x = x + y # 15
# y = x - y # 5
# x = x + y # 10

# or 

x = x ^ y
y = x ^ y
x = x ^ y

print(f"after swaping X:{x} and Y:{y}")


