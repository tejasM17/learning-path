#                 Homework

# Create a Class:

# Write a class Mobile with attributes brand and price.
# Create two objects of the class and display
#  their attributes using a method.

class mobile :  # class
    def __init__(self, brand,price):  # attribute
        self.brand = brand
        self.price = price

    def details(self):  # methods
        return (f"{self.brand} is good and its price is {self.price}")
    
mobile1 = mobile("Samsung" , 20000)  #  object      
mobile2 = mobile("Starlink", 1)

print(mobile1.details())
print(mobile2.details())


#                       Method Definition:

# Define a class Student with attributes name and marks.
# Write a method display_info() that prints the student's name and marks.
# Create multiple objects of the Student class and call the method on each.

class student :
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks

    def inf(self):
        print(f"student name : {self.name}   score : {self.marks}")

student1 = student("CHIDU", "12")
student2 = student("MOHAN", "14")
student3 = student("SHARATH", "9")
student4 = student("RAJU", "10")

student1.inf()
student2.inf()
student3.inf()
student4.inf()
