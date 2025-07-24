                        #   FUNCTIONS

def bro():
    
    a = input("YOur car  : ")
    z =  input("Your name : ")
    print(f"BRo {z} have {a} CAr...!")


bro()
bro()
bro()
bro()
bro()


                        #  parameters and default parameters



def bro(Car,BRO = "BRO"): # a and z are 
    # parameters
    print(f"BRo {BRO} have {Car} CAr...!")     # a and z are arguments  when we call the function  we pass the arguments

    


bro("bmw")  # positional arguments
bro(BRO="RAJU",Car="RR")  # keyword arguments



def maggi(n):
    
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")


maggi(2)
maggi(3)
maggi(4)
maggi(5)



                                     # Returning Values from a Function


def fn(dolr):
    return int(str(dolr) *3)

x = 100
y = fn(5)

z = x  + y    # or z = x + fn(500)
print(z)







#                                   explaining Local and Global Variables 


def fn():
    a = input("Enter Your Bank balence : ")  # a is local variable
    print(f"Your bank balence is {a}")
    print(b)

b = input("enter your otp: ")  # global variable

print("thanks for entering your otp ")


#                                           MAP FUNCTION

# Define a function to add two numbers
def add(x, y):
    return x + y

# Two lists of numbers
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Apply the add function to corresponding elements using map
result = map(add, list1, list2)

# Convert the map object to a list
print(list(result))

# output : [5, 7, 9]