              #  Homework

# 1.    Tuple Operations

#       Create a tuple with 5 elements

tup = ("raju",2, 2,1,4,True,"teju")
print(tup)

#tup[0] = 10 # it will show error because tuple is immutable 

#      Perform slicing on the tuple to extract the second and third elements

print(tup[1:3])

#      Concatenate the tuple with another tuple.

tup1 = ("chidu", "moni", "sharath" )

add = tup + tup1
print(add)   # allow duplicates


#  2.      Set Operations:

mine = {"//M","tesla", "RR", "lambo", "bugatti", "BMW", "ferrari"}
bros = {"bugatti", "ferrari", "Z-900", "phantom", "BMW", "RR", }

print (mine & bros)   # intersection operation
print(mine - bros)   # difference operation
print(mine | bros )   # union operation

print("after adding")
mine.add("poruche")
print(mine)


print("after removing" )
mine.remove("tesla")
mine.discard("TATA")  # it will not show any error even if the element is not present in the set
print(mine)


#    3.Tuple and Set Comparison:


l = [1, 3, 5, 7, "supra", "bugatti", "ferrari", "BMW", "RR", "done"]
print(type(l))

z = set(l)
print(type(z))
print(set(l))

y = tuple(l)
print(type(y))
print(tuple(l))

print(z, y)  # set and tuple are unordered