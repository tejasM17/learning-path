#                                                         While Loops in Python


# A while loop in Python is used to repeatedly execute a block of code as long as a specified condition is True.
# The loop continues to run until the condition becomes False.








#  Key Points:
# 1.  Condition: The loop continues as long as this condition evaluates to True.

# 2.  Indentation: The code block under the while loop must be indented.

# 3.  Infinite Loop: If the condition never becomes False, the loop will run indefinitely.










defeat = True
attempt = 1
while defeat and attempt <=100:
    print( f"I'm The Best, fuck your motivation now am attempting no: {attempt}" )
    attempt += 1
    
print("Hoo!  This f***** succuss is difficult thing but I made it, lol lol lol HA HA HA HA HA")










i = int(input("enter a valid  number: "))
while i <= 100:
    print(i)
    if i == 100:
     break
    i += 1
 
else:
  print("i is no longer less than 100")




attempt = True
c = 1

while attempt  :
    if c % 2 == 0:
        c += 1
        continue  # munde iro code na exicute madalla
    print(f"attempt{c}")
    c += 1
    if c > 50:
        break
    
    
    
    
    
                                     # attemts = iteration
                               #IMPORTANT CONSEPTS       
a = 0

while a < 10: 
    b = 0 
    while b < a :
        print  ("tejas" , end=" " )
        b += 1
    print("")
    a += 1
    
    
    
    
               #6. Using while Loops for User Input
               
               
pin = "123"        
tra = 1

while tra <= 3 :
    input_pin = input(f"Trail-{tra}| PIN >  ")
    tra += 1
    
    if input_pin == pin:
        print ("You Loged In!")
        break
    else:
        print("Incorect PIN")