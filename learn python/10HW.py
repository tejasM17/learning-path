     #  Multiples of 3

for x in range(3,4):
    for y in range(1,11):
        print(f"{x*y}")
     
    print("All the multiples of 3 is printed")
    
    
    
    #Sum of First 10 Numbers:
    
for a in range(1,11):
    c = 10*(10+1)/2
    
    
print(f"the sum of 1 st 10 nubers  is {c}")


#  Print Your Name Letter by Letter:

name = ("TEJAS")

for l in (name) :
    print(f"{l}")
    
    
#   Count Vowels in a String:

vovels = "aeiou"

enter_string = input("enter the string:")
count = 0
for letter in enter_string:
    if letter in vovels:
        count += 1

print(f"the number of vovels in the string is {count}")