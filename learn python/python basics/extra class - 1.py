#LEARNING HOW TO USE THE DEBUGGURE



tejas = 1

while tejas  <= 12:
    print(f"ALL THE {tejas} CLASS am Present SIR" , end="\n")
    tejas += 1
    
    

# multiplication table

for x in range (1,11):
    for y in range (1,11):
        print(f"{x} X {y} = {x * y}", end="\n")


ca = [21 , 234, 44, 56 , 6, 23, 67, 80]

nulit = []

for x in range(len(ca)):
    c = ca[x]
    d = ca[-x]
    z = c*d
    if z%2 == 0:
        nulit.append(z)
        
print(nulit)
    
    
