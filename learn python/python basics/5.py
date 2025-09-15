#LISTS  IN  PYTHON (Arryas)


items = ["BMW","MErcidice","Bugatti",  "///M","bike"]
     # indexing

#a. Accessing List Elements

s = [1,2, "teja", "RR", [9, 7, 10, "brothers"],False,True,"noob"]   

print(s[-4][3])
 

#b. Modifying Lists

items.pop()   #  Removes the element at a specific index
items.pop(0)   #to remove first item
items.append("Ferrari")  # Adds an element to the end of the list.
items.remove("Bugatti")    #  Removes the first occurrence of an element.
items.insert(1, "RR")      #Inserts an element at a specific index.
print(items)

items[0] = "RR"  # to acces the list items
print(items)


#c. Slicing Lists         list_name[start:stop:step]

a = [10, 2, 73,11, 51, 26]

print(a[1:5:2])

a2 = a[0:4]

print(a2)

#d.  List Functions and Methods

print(len(a2))
a.sort()
sorted_item = sorted(a)# gives assending order
z = a.sort(reverse=True)  # revers the valus

a.reverse() # revers the valus

print(z)
print(a)                 # assending order

print(sum(a)) 

#e. Common Methods:

fruits = ["apple", "banana", "cherry"]

print(fruits.index("apple"))  # Output: 0

numbers = [1, 2, 3, 1, 1]
print(numbers.count(1))  # Output: 3

fruits.reverse()
print(fruits)  # Output: ['cherry', 'orange', 'apple']

numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 9]

#f. Nested Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
print(matrix[0])  # Output: [1, 2, 3] (first row)
print(matrix[1][1])  # Output: 5 (element in the second row, second column)