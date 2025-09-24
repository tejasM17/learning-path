# Building A Hash Table from Scratch

# We will build the Hash Table in 5 steps:

# Create an empty list (it can also be a dictionary or a set).
# Create a hash function.
# Inserting an element using a hash function.
# Looking up an element using a hash function.
# Handling collisions.


# Step 1: create an empty liist

my_lis = [[], [], [], [], [], [], []]  # None - empty eliments

# each of the eliment is "BUCKET" in hash table

# Step 2: Create a Hash Function

# A common way is to find a way to convert the value into a number
# that equals one of the Hash Table's index numbers,
#  in this case a number from 0 to 9.

# EXAMPLE :
# Create a Hash Function that sums the Unicode numbers of each
# character and return a number between 0 and 9:


def hash_func(valu):
    sum_ofchar = 0

    for l in valu:
        sum_ofchar += ord(l)
        print(f"ord of char : {ord(l)}")
        print(f"sum of cahr : {sum_ofchar}\n")
    print(f"sum_ofchar % 10 : {sum_ofchar % 10}")
    return sum_ofchar % 10


print(hash_func("tejas"))

# Example:

# 10 % 3 = 1   (because 10 ÷ 3 = 3 remainder 1)
# 14 % 5 = 4   (because 14 ÷ 5 = 2 remainder 4)

# So, 275 % 10 = 5
# (because 275 ÷ 10 = 27 remainder 5).


# Step 3: Inserting an Element

# Lets create a function that add items to our hash table:


def add(name):
    index = hash_func(name)
    my_lis[index].append(name)


add("teju")  # to add list
add("raju")
add("moni")
add("sharattu")
add("chidu")
print(my_lis)
print(f"\nmy list : {my_lis}")  # ['mon', 'cHd', 'sharatm', 'tej', 'raju', None, None]

# Rewrite the add() function, and add the same names as before:


# Step 4: Looking up a name

# To find "cHd" in the Hash Table, we give the name "cHd" to our hash
#  function. The hash function returns 8, meaning that "cHd"
# is stored at index 8.


def contain(name):
    index = hash_func(name)
    return my_lis[index] == name


# print(f"is contain : ", contain("cHd"), "\nhello chidu")


# Step 5: Handling collisions

# We give "Stuart" to our hash function, which returns 3, meaning
#  "Stuart" should be stored at index 3.

# Trying to store "Stuart" in index 3, creates what is called a
#  collision, because "Lisa" is already stored at index 3.

# To fix the collision, we can make room for more elements in the same
#  bucket. Solving the collision problem in this way is called
#  chaining, and means giving room for more elements in the same
#  bucket.


# Uses of Hash Tables

# Hash Tables are great for:

# Checking if something is in a collection (like finding a book in
#  a library).
# Storing unique items and quickly finding them
# (like storing phone numbers).
# Connecting values to keys (like linking names to phone numbers).
