def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b 

def divide(a,b):
    return a/b

def menu():
    print('\n # select an option to clauclate operations' ) 
    print('1 - for addition\n 2 - for subtraction\n 3 - for multiplication\n 4 - for division\n 5 - to EXIT')
    
while True:
    menu()

    choice = float(input("enter your choice (1/2/3/4/5): "))


    if choice in {1, 2, 3, 4}:
        num1 = int(input("enter the first number:"))
        num2 = int(input("enter the second number:"))

        if choice == 1:
            print("result:", add(num1, num2))
        elif choice == 2:
            print("result:", subtract(num1, num2))
        elif choice == 3:
            print("result:", multiply(num1, num2))
        elif choice == 4:
            if num2 == 0:
                print("error: division not done by zero")
                continue
            else:
                print("result:", divide(num1, num2))
    elif choice == 5:
        print("exiting the calculator...")
        break

    else:
        print("invalid choice. please try again.")
