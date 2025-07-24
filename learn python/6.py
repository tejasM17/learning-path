#                                                         Tuples and Sets in Python

 #  1. Tuples in Python    :   ordered and immutable (unchangeable). we cannot change, add or remove items after the tuple has been created
   
   #Syntax:   my_tuple = (element1, element2, element3, ...)
   
   
   
t = (" BMW ", "RR", "TATA", "LAMBO", 5, 4, 3, 2, 1, (5, 4, 3, 2, 1))   # hold any data type

t1 = (21, 31, 41, 51, 7, 1, 2, 3, 4)

print(type(t1))
print(t)       
  

#   reating a Tuple with One Element:

single_element_tuple = ("apple",)
print(single_element_tuple)




#   2. Accessing Tuple Elements

#indexing
print(t[0]) 
print(t[-2])
print(t1[4])

#    licing Tuples

print(t[1:4])

#    3. Tuple operations   :  tuples are immutable

#  Tuple Concatenation:

tup1 = (1, 2, 4, 6, 7, 8)
tup2 = (2, 3, 5, 7, 9 ,0 ,10 )

add = tup1 + tup2
print(add)     # not-unique


#OR


x = ("BUGATTI", "Z900", "RR", "FERRARI")
y = list(x)
y.append("BMW")
a = tuple(y)
print (y)


#Tuple Repetition:

print(t[0] *3)    #output : BMW  BMW  BMW

#  Checking Membership 

print(" BMW " in t)


#   4.  Tuple Methods

tup3 = ( 1, 2, 3, 3,"bmw", 5, 6, 7, "bmw", 2, 3, 3, 4, 4,5, "bmw", "bmw", ) 

print(tup3.count(3))
print(tup3.index(6))
print(tup3.index("bmw"))   # prints 1st bmw's index



#                                                       Sets in Python


#  A set is a collection of unique items that is unordered and unindexed. Sets do not allow duplicate values.
# Sets are useful for performing operations like union, intersection, and difference.


set1 = {"BMW", "RR", "TATA", "LAMBO", "BMW", 1, 1, 1, 2, 2, 3}


print(type(set1))
print(set1)   # unique, unorderd,  unindexd. 
# print(set1[2])  output:  'set' object is not subscriptable

 #  5.   Set Operations

 
s1 = {1, 2, 3 ,4, 5}
s2 = {3, 4, 5, 6, 7, 8, 9}

print(s1 & s2)     #a.  intersection
print(s1 | s2)     #b.  union
print(s1 - s2)     #c.  diffreence
print(s1 ^ s2)     #d.  (intersection)'  = symmitric diffrence [same iro eliment na remove madutte]






a = {"apple", "banana", "cherry", True, 1, 2}  # True and 1 is considered the same value

print(a)


 
 
 # 6. set methods
  
#   remove(): Removes a specified element from the set. Raises an error if the element does not exist

 
thisset = {"M-3", "M-2", "M-1", "tesla"}
thisset.remove("tesla")

print(thisset)


#    add(): Adds exactly only one element to the set


a = {1, 2, 3, 4, "raju", "chidu", "moni", "sharath"}
print(a)
a.add("teju")
print(a)

#   discard(): Removes a specified element without raising an error if it does not exist

f = {"apple", "mango", }
f.discard("banana") 

print(f)



#   pop(): Removes a random element from the set.

x = a.pop()

print(x)  # removed item
print(a)  # after removel

#   clear(): Removes all elements from the set.

a.clear()
print(a)


#  Add Set Items  :  [ var1.update(var2)]


st1 = {"Raju", "Teju", "Chidu", "Moni"}
st2  = {"Sharath", "Suvi" }

st1.update(st2)

print (st1)



#        Join Sets  : 

 
#There are several ways to join two or more sets in Python.

#The union() and update() methods joins all items from both sets.

#The intersection() method keeps ONLY the duplicates.

#The difference() method keeps the items from the first set that are not in the other set(s).

# ***  [The symmetric_difference() method keeps all items EXCEPT the duplicates.]


#                                                     UNION:


set10 = {"a", "b", "c"}
set20= {1, 2, 3}

set30 = set10.union(set20)
print(set30)



#       Join Multiple Sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
#   or
print(set1 | set2 | set3 |set4 )
print(myset)


#              Loop Sets



thisset = {"Raju", "Teju", "Chidu", "Moni"}

for x in thisset:
  print(x)
  print(type(thisset))



















               #Differences Between Lists, Tuples, and Sets
 
 
#Feature       .     	List	                  Tuple                   	Set
#              .
#Ordering      . 	    Ordered	                Ordered                  	Unordered
#Mutability	   .      Mutable	                Immutable	                Mutable
#Duplicates	   .      Allows duplicates	      Allows duplicates	        No duplicates
#Indexing	     .      Supports indexing	      Supports indexing	        No indexing
#Operations	   .      List operations	        Tuple operations	        Set operations
#Common Uses	 .      General collection     	Fixed data              	Unique items


l = []
t = (1)
s = {2}

print(l)
print(t)
print(s)


