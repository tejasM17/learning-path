 # INPUT AND OUT PUT, AND STRING MANUPULAION, AND COMMENTS
 
 
#  The data entered by the user is always received as a string,


a = input ("age- ")

print (a)

b_name = input ("boy_name- ")
b_age = int(input ("boy_age- "))
G_name = input ("girl_name- ")
G_age = int(input ("girl_age- "))

age_dif = abs(b_age - G_age)



print (b_name +" LOVES " + G_name + ". their Age diffrenc is" + str(age_dif)  ) # Concatinatin

print (f"{b_name} loves {G_name}. age diffrenc is {age_dif}")                    # Formated strings




#  String Methods:


msg = "Hello, brothers!"

print(msg)
print(msg.strip())
print(msg.replace("Hello", "Hi"))
print(msg.upper())        #str.upper() takes no arguments
print(msg.lower())    #str.lower() takes no arguments



#Accessing String Characters:

text = "Python"
print(text[0])  # Output: P
print(text[2])  # Output: t


print(text[-1])  # Output: n
print(text[-3])  # Output: h



#Slicing Strings:


text = "Python Programming"
print(text[0:6])  # Output: Python (extracts from index 0 to 5)
print(text[:6])  # Output: Python (same as above)
print(text[7:])  # Output: Programming (from index 7 to the end)




# COMMENTS


# This is a single-line comment
print("Hello, World!")




# Multi-line comments

"""
This is a multi-line comment.
It can span multiple lines.
"""
print("Hello, Python!")



#  Escape Sequences


print("Hello\nWorld")  # Output: 
# Hello
# World

print("Hello\tPython")  # Output: Hello    Python










# HOME WORK 1 - ADD TWO NUMBERS

num1 = int(input("no1 : "))    # all inputs are in string we must convert to what data type we want

num2 = int(input("no2 : "))

sum = num1 + num2
print (sum)

# STRING MANUPULATION 


    # CONATINATION 

first_name = 'tejas'
last_name = 'raju'

full_name = first_name + " " + last_name

print(full_name)


# REPITION


messagee = "Dreams are waiting......! "*3

print(messagee*10)

# STRING METHODS

print(messagee.upper())
print(messagee.lower())
print(messagee.strip()*3)


# TO REPLACE


print(messagee.replace("warning", "CHANCE"))  




name = '''Raju buy a 'lambo'
       and all my brothers bought their 
       dream cars'''
       
print(len(name))    # LENGTH
print(name)








# IMPORTANT CONNSEPT TO DATASTRUCTURS AND ALOGORITHIMS

                # ACSESSING STRING CHARECTORS
                
                
                
name = "tejas"
print(name[1])        #index = position - 1   output = e

print(name[2:5])     # indentation     output = jas   end idx 4 give 5

print(name[:2])      # slicing  of strings

print(name[2:])



Name = "Rajesh"            # R  a  j  e  s  h
                           #-6 -5 -4 -3 -2 -1        
print(Name[-2])             #output = s


# ALTERNATIVE              format = [start : stop : step ]
                            #                +1   (skip)


print(Name[::2])             #output = Rjs


# Escape Sequences

a = " we are \n all brothers"    #output = we are
                                #           all brothers

a = " we are \t all brothers"    # output = we are      all brothers

a = " we are \\ all brothers"
print(a)  

# sum of two num