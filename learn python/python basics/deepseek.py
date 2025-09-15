#
    #  2. Nested while Loops
#   A nested while loop is a loop inside another loop. The inner loop completes all its iterations for each iteration of the outer loop.

#    Multiplication Table Using Nested while Loops

i = 1
while i <= 10:  # Outer loop
    j = 1
    while j <= 10:  # Inner loop
        print(f"{i} * {j} = {i * j}" )
        j += 1
        print(" ")
    i += 1