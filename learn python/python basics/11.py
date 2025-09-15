                                                #   lists and Dictionaries with For Loops, List Comprehension, and Dictionary Comprehension
                                                


# 1.  Looping Through Lists

# sum of numbers using for loop





k = [2, 23, 34,45, 345,34, 334]
total = 0

for n in k :
    print(total)
    total= total + n
    
print(total)



#  Doubling each number in a list and add to that list


number = [12, 34, 234, 34, 67]

li = []

for x in number :
    li.append(x * 2)
    print(li)
    
print( "dubbeld numbres are: ", li)



         # OWN
         
         
# 2. Looping Through Dictionaries
         
         
         
         
#   Write a program that doubles numbers greater than 5 in a list and appends the doubled values to the list.

brothers = { "raju -": 20, "chidu -": 20, "sharath -": 18, "moni -" : 17}

for  age,bros in brothers.items():
    print(f"{age} age - {bros}" )
    
    
# addind two list items  to dictionaries





brs = ["raju", "chidu", "teju", "sharath", "mohan"]

mar = [87, 89 ,43, 68, 89]

brs_mar = {}


for mr , br in enumerate(brs):
    brs_mar[br] = mar[mr]
    
print(brs_mar)





       # 3. for Loops with range()




brs = ["raju", "chidu", "teju", "sharath", "mohan"]

mar = [87, 89 ,43, 68, 89]

brs_mar = {}


for b in range (1,len(brs),2):
    brs_mar [brs[b]] = mar[b]
    
    
print(brs_mar)









#                                        4.  List Comprehension    {[VVV.....IMP]}

# SYNTAX

# new_list = [exp for item in collection if condition]



m = [1,2,3,4,5,6,7]
       #or
# m = [x for x in range (1,7)]

n_m = [n**2  for n in m if n%2==1]
print(n_m)


#   Nested  List Comprehension


matrix = [[i + j for j in range(1,5)] for i in range (1,5)]

print(matrix)


# output:  
# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]

# access list of strings


li = ["raju", "teju", "chidu", "moni", "sharath"]

print(li)
f = [brose.upper()[1] for brose in li]
print(f)

print("1-R , 2-E , 3-D , 2-O , 1-S    ==   REDOS")

# # output: 
# ['raju', 'teju', 'chidu', 'moni', 'sharath']
# ['A', 'E', 'H', 'O', 'H']
# 1-R , 2-E , 3-D , 2-O , 1-S    ==   REDOS


#   List Comprehension with Multiple Conditions



divisible_by_2_and_3 = [x for x in range(1, 21) if x % 2 == 0 if x % 3 == 0]
print(divisible_by_2_and_3)

#output: [6, 12, 18]




#    List Comprehension with if-else


sanke = [1,2,3,4,5,6,7]

resultn = ["even-no." if a%2== 0 else "odd-no." for a in sanke]
print(resultn)


# #  output : 
# ['odd-no.', 'even-no.', 'odd-no.', 'even-no.', 'odd-no.', 'even-no.', 'odd-no.']


#  Flattening a 2D List


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)


# output : [1, 2, 3, 4, 5, 6, 7, 8, 9]



#  List comprehention Dictionres


our = ["teja", "raju", "chidu"]

our_dict = {nam : len(nam) for nam in our}

print(our_dict)

# # output : 
# {'teja': 4, 'raju': 4, 'chidu': 5}

#  Filter a Dictionary


original_dict = {"a": 5, "b": 15, "c": 8, "d": 20}
filtered_dict = {k: v for k, v in original_dict.items() if v > 10}
print(filtered_dict)


# output : {'b': 15, 'd': 20}




                                                        # DICTIONARY COMPREHENTION




# SYNTAX


# new_dict = {key_expression: value_expression for item in iterable if condition}


#   Dictionary Comprehension with Condition on Keys


text = "hello world"
vowels = {char: text.count(char) for char in text if char in "aeiou"}
print(vowels)

# output : {'e': 1, 'o': 2}



#   Dictionary Comprehension with if-else



numbers = [1, 2, 3, 4, 5]
even_odd_dict = {x: "Even" if x % 2 == 0 else "Odd" for x in numbers}
print(even_odd_dict)


# output : {1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even', 5: 'Odd'}





#                                      SPLITTING STRINGS TO CREATE LISTS


s = "To-take-INPUT-we-use-s.split()"

l = s.split("-")
print(l)

# #  output : 






#        VVVVVVVVVV ---------- IMPORTANT




# ['To', 'take', list as 'INPUT', 'we', 'use', 's.split()']


print("Now we take list input")

x = input("enter list of numbers: ").split()

lis = [int(nu) for nu in x]

print(lis)



#or






lis = [int(nu) for nu in input("enter list of numbers: ").split()]

print(lis)

