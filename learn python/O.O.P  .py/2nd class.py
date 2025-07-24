#                                    Constructors and the self Keyword

# 1. The __init__() Constructor
# Constructor: The __init__() method in Python is a special method that initializes an object when it’s created. It’s called automatically when you create a new instance of a class.
# Purpose: It allows you to set the initial state of the object by defining its attributes.

class Car:            # class
    has = "4 wheels"  # class attribute/variable is always constant, and it is shared by all objects of the class
    # __init__() Constructor  
    def __init__(self, brand, model, year):
        print("Constructor called",brand)      # constructor 1st called it will be called when the object is created
        self.brand = brand   # object/attribute # variables
        self.model = model # variables
        self.year = year

    def display_info(self):               # method
        print(f"Car: {self.brand} model: {self.model} year : ({self.year}) {self.has}")  

car1 = Car("BMW ///M5 CS", "german", 2022, )     # object
car1.display_info()
car2 = Car("Audi", "honkong", 2011)     # object
car2.display_info()
car1.brand = "Benz"   # changing the attribute
print(car1.brand)
car1.display_info()


class human:          # class
    def __init__(self, name="unknown" , age=0 , salary=0):
    #  you can't give kwarguments before positional arguments         # constructor
        self.name = name
        self.age = age
        self.salary = salary
    def display_info(self):     # method
        print(f"{self.name} is {self.age} years old and their salary is {self.salary}")
        
human1 = human("John", 30,)
human1.display_info()
human2 = human(age=25, name="tejas",salary=30)      # human(age=25, name="tejas",[positional arguments = 30]) positional arguments cannot appear after keyword arguments
human2.salary = 5000 # accessing the attribute     
human2.display_info()
h3 = human('Teju',  )
h3.display_info() 
