                                    # For Loops in Python

# The Basic Structure of a for Loop

# Syntax:

# for item in sequence:
#     # Code to execute for each item in the sequence








# 2. Using range() with for Loops

# Syntax of range():
    
#     range(start, stop, step)



                        
for a in range (1,6):
    
    print(a)


for i in range (10,20,2):
    print(i)


bro = ["family","brothers","Teachers","Success"]

for words in bro:
    print(words)
    
    
# Counting Small Wins


z = ("day 1 : am learn todya something in python",
     "day 2 : am compleated my dorpshipping learning class",
     "day 3 : work in progrres  of my pu college website",
     "day 4 : i have started meditation form todya",
     "day 5 : am learn somthing in python today",
     "day 6 : i got a some success in dropshipping",
     "You had 6 small wins in this week. keep going!")

for st in z :
    print(st, end=" ")
    print()
    
    
books = ["week 1: How many books you read in this week? 0",
         "week 2: how many books? 1",
         "week 3: how  many? 2",
        " You read 3 books in this month, no worries there are some peoples not even try."]


for book in books:
    print(book, end=" ")
    print("")
    
    
    
      # LOOPING  OVER STRINGS
      
name = "raju"

for lettters in (name):
    print (lettters * 3)
    
    
    
l = ("raju", "chidu", "moni", "sharath"," tejas")


for nom , bros  in enumerate(l):
    print(f"bro {nom+1} is {bros},")
    
    
   # NESTEDD FOR LOops
   
   
# multiplication table

for x in range (1,11):
    for y in range (1,11):
        print(f"{x} X {y} = {x * y}", end="\n")
        
        
        
won = ("BUGATTI-raju", "SUPRA-chidu", "FERRARI-moni", "ROLLS ROYCE-sharath","BMW\\\M4 compitition - tejas")

   #index,variable
for car  , bhai     in enumerate (won): 
    print(f"NO:{car+1} {bhai} !!!") 
    
    if bhai == "BMW\\\M4 compitition - tejas" :
        continue
    print(bhai)
    
    
    
# Using else with for Loops

q = [12,345,56,67,43,4]

for n in q:
    print(n)
    if n == 56:
        break
    
else:      #importans of else           # output: 12
                                        #          345
                                        #          56 
    print("all prints")
    
    
    
    
    
    
    # DICTIONARES 
    
d = {"Name:": "Tejas", "age:" :"18", "Status:" : "0$", "Mindset:" : "Infinite POTENTIAL", "Need:" : "BMW\\\M4 compitition"}

print(d.items()) # makkes list of tuples   output:    dict_items([('Name:', 'Tejas'), ('age:', '18'), ('Status:', '0$'), ('Mindset', 'Infinite POTENTIAL')])

for key , value in d.items() :
    print(key, "  ", value, end="\n")