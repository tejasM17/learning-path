foods = ["idli", "dose", "palavu", "chitranna","uppittu", "chapathi"]

n_fod = [fd.upper() for fd in foods]
print(n_fod)





#Sum of Prices


#  Create a dictionary of 5 items with their prices. Write a 
# program that calculates the total price of all items using a for loop.




itms = {"BMMW-M4" : "150",
        "BUGATTI": "35",
        "Rolls Royce" : "50",
        "Supra" : "30",
        "Ferrari" : "160"}
sum_pric = 0
n_dic = {}

for itm,pric in itms.items() :
    int_pric = int(pric)
    n_dic[int_pric] = itm
    sum_pric = sum_pric + int_pric
    
print("new dic with int price : ",n_dic)
print("Sum of prices : ",sum_pric)
    
  
  
  

#  List of Squares:


#  Create a list of numbers from 1 to 10. Use list comprehension 
# to generate a list of their squares


li = list(range(1,11))

n_li = [num * 2 for num in li]

print(n_li)



#  sutdent data task 


#Create a list of 3 dictionaries, where each dictionary contains the 
# name, age, and marks of a student. 
# Loop through the list and print each student's information.




stu_lis =[ 
    {"Name : ": "Sharath", "Age : ": 19, "Marks : " : 92 },
    {"Name : ": "Tejas", "Age : ": 18, "Marks : " : 45 },
    {"Name : ": "Mohan", "Age : ": 17, "Marks : " : 84 }
]


for stud in stu_lis :
    print(f"Name : {stud['Name : ']}, Age : {stud['Age : ']}, Marks : {stud['Marks : ']}")
    
    
    
    
# Dictionary Comprehension:


#  Create a dictionary where the keys are Kannada cities, and the values are their populations. 
# Use dictionary comprehension to filter out cities with populations below 10 lakhs.



stat_dict = {"Tiptur" : 5000,
             "hassan" : 8000,
             "Manjunatha_nagara" : 3800,
             "Banglore" : 30000,
             "Halepalya" : 70000,
             "Dubai" : 2}


dic_compra = {key : pop for key,pop in stat_dict.items() if pop<=10000}

print(dic_compra)




# Nested List Challenge: Write a Python program that takes a list of lists (a 2D list) as input and:

# Prints the entire matrix row by row.
# Prints the sum of each row in the matrix.

    

rows = int((input("Give number of rows: ")))
columns = int((input("Give number of columns: ")))
matrix = []

for x in range(rows) :
    a =[]

    for y in range(columns) :

        z = int(input("Enter the eliments: "))
        a.append(z)
    matrix.append(a)
print(matrix)