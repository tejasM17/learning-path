# OPERATORS 

# 1. Assignment Operators

a = 20
a += 20
a = 20
a += 20
a -= 20
a *= 20
a /= 20
a %= 20



print( a )

# 2. Comparison Operators

a = 30 
b = 10

print( a == b)  # false
print( a < b)   #false
print( a > b)   #true 
print( a <= b)  #false
print( a >= b)   #true
print( a != b)   #true

#3. Logical Operators              Logical operators are used to combine conditional statements.
#                                 They evaluate expressions and return either True or False

n1 = 10
n2 = 20


# and operator

print(True and True)

print (n1 < n2 and n1 < n2  )       # Output: True (both conditions are True)
print (n1 < n2 and n1 > n2  )           
print (n1 + n2 and n1 < n2  )        
print (n1 < n2 and n1 >= n2  )           
print (n1 < n2 and n1 <= n2  )        
               
               
# or operator

print(True or False)
                            
print (n1 < n2 or n1 < n2  )                 # Output: True (one of the conditions is True)
print (n1 < n2 or n1 > n2  )
print (n1 + n2 or n1 < n2  )
print (n1 < n2 or n1 >= n2  )
print (n1 < n2 or n1 <= n2  )


# not operator

print ( not(True or False))

print (not (n1 < n2 or  n1 < n2  ))                # Output: True (reverses False to True)
print (not (n1 < n2 or  n1 > n2  ))
print (not (n1 + n2 or  n1 < n2  ))
print (not (n1 < n2 or  n1 >= n2  ))
print (not (n1 < n2 or n1 <= n2  ))                                           


#  4. Membership Operators



n = "bugatti"
l = [ 2, 4, 6, 8]

print( "b" in n)              # in = present in
print( "b" not in n)          # not in = absent
print( not("b" in n)) 

print (1 in l)
print (1 not in l)

print(( "b" in n ) and ("6" in l))


# 5. Bitwise Operaters 


