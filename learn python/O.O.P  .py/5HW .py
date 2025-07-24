#  getters and setters

class banck_account:
    def __init__(self,balance):
        self.__balance = balance
# Write a getter method to retrieve the balance and a setter method to update it, ensuring the balance never goes below zero.
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,updated_ammount):
        if updated_ammount < 0:     # this is the power of seters
            print("ERROR : cannot set negativebalance")
        else:
            self.__balance += updated_ammount
      


bnk_aacunt = banck_account(1000)
print(bnk_aacunt.get_balance())
bnk_aacunt.set_balance(2000)
print(bnk_aacunt.get_balance())



#  Method Overloading

class caluclator:
    def __init__(self,a,b,c):
        self.a = a
        self.b= b
        self.c = c

    def multiply(self):
        print(f"product of {self.a} and {self.b} is {self.a*self.b}")
        print(f"product of {self.a} & {self.c} is {self.a * self.c}")
        print(f"product of {self.a} & {self.b} & {self.c} is {self.a * self.b * self.c}")

claculat = caluclator(4,3,2)
print(claculat.multiply())

# 3.  Method Overriding:

# Create a parent class Shape with a method draw() that prints "Drawing shape".
# Create a child class Circle that overrides draw() to print "Drawing circle"

class shape :
    def draw(self):
        print("Drawing shape")

class circle(shape):
    def draw(self):    # this is the power of overriding
        super().draw()
        print("drawing circle broo!!!")

shape1 = shape()
shp = circle()
shp.draw()

#  abstract class   


# Define an abstract class Employee with an abstract method calculate_salary().
# Create a subclass Manager that implements calculate_salary() based on working hours and rate per hour.


from  abc import ABC, abstractmethod

class employee((ABC)):
    @abstractmethod # en-forcement
    def calculate_salary(self): # you must include this method in your subclass
        pass                        # otherwise you will get an error
        

class manager(employee):
    def __init__(self,name,working_hours,rate_per_hour):
        self.name = name
        self.working_hours = working_hours
        self.rate_per_hour = rate_per_hour
    def calculate_salary(self):
        return self.working_hours * self.rate_per_hour
    
manager1 = manager("HARSHITHA",1,20)
print( f"sallary of {manager1.name} is {manager1.calculate_salary()}" )
