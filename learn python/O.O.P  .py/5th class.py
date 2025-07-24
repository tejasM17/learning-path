#    Getters, Setters, Method Overloading & Overriding, super(), Abstract Classes

# 1. . Getters and Setters
# Definition: Getters and setters are methods that allow controlled access to an object's attributes.
class brothers:
    def __init__(self, name , age):
        self.__name = name  # attribute
        self.__age = age

    def get_name (self):      # getter  if an attribute is taken by method 
        return self.__name  # only asscesble inside the class

    def set_name (self,name):   # setter
        if isinstance(name, str):   # validation
            self.__name = name

# Purpose: They help in validating data, protecting data from accidental modification, and providing controlled access.
# example:
    def set_age(self, age):   # setter
        if isinstance(age, int):  # validation
            self.__age = age
        else:
            print("Age must be aan integer... ERROR!!!")

bro = brothers("raju", 14)
print(bro.get_name())

bro.set_name("chidu")
print(bro.get_name())

bro.set_age(2)






# 2.   method overloading  

class clalculator:
    # def add(self, x,y): # overloading
    #     print(x + y)    

    def add(self , x,y,z=0):
        print(x - y + z)   
c1 = clalculator()
c1.add(4,5)
c1.add(4,5,6)



# 3.  method overriding  

# defination : parent class alliro method na child class alliro method [dominate] override madutte

class animal:  #[parent class]
    def make_sound(self):
        print("Animal makes a sound")
    
class dog(animal): #[child class]
    def make_sound(self):
        print("bark")

d = dog()
d.make_sound()



# 4. super() funtion

# defination: Method overriding allows a child class to provide a specific implementation for a method that is already defined in its parent class.

class human:
    
    def run(self,):
        print ("human can run fastly")

class child(human):
    def __init__(self,status):
        self.status = status
    def run(self):
        super().run()  # parent class method
        print(f"{self.status} can run fast")
    def success(self):
        super().run() # parent class method
        self.run() # child class method


chi = child("Billionaires")
chi.run()
chi.success()


#  Abstract Classes

# Definition: An abstract class in Python is a class that cannot be instantiated directly. It can have abstract methods, which must be implemented by subclasses.
# Purpose: Abstract classes provide a blueprint for other classes, enforcing a structure where subclasses must implement certain methods.


from  abc import ABC, abstractmethod

class gadi(ABC):
    @abstractmethod  # enforcement
    def start_engine(self):
        pass
class bike(gadi):
    def __init__(self,name ):
        self.name = name
    def start_engine(self):     # enforcing a structure
        print(f"{self.name} engine started")

b = bike("BMW")
print(b.name)