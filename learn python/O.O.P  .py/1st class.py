# #     how to create class

# class humaan:                                   #  class
#     def __init__(self , name):         #       attribute
#         self.name = name

#     def walk(self):                   #        Method
#         print(f"{self.name} is walking")

# tejs = humaan("teja")                  #   objects
# raju = humaan("raju")

# tejs.walk()
# raju.walk()


#       Adding Attributes (Variables)   AND   Adding Methods (Functions Inside Class)

class car:
    def __init__(self , brand, model, year):
        self.brand = brand #        attribute  / variables
        self.model = model #        attribute  / variables
        self.year = year  #        attribute  / variables

     # Method to print car info

    def display_info(self): 
        print(f"Car: {self.brand} {self.model}")

# creatinng object with attribute

car1 = car ("BMW \\\M4", "csl", 2014)
car2 = car ("SUPRA", "mk4", 2014)

print(car1.brand, car1.model, car1.year)
print(car2.brand, car2.model, car2.year)