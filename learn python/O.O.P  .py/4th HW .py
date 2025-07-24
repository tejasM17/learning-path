#                     HOMEWORK

# Inheritance:

# Create a base class Vehicle with a start method. Then create a subclass Bike with an additional ride() method.
# Demonstrate how the Bike can use both start and ride.


class Vehicle:
    def start(self):
        print("vehicle is starting")


class bike(Vehicle):
    def ride(self):
        print("bike is on rideing")


bik = bike()
bik.ride()
bik.start()


#   Polymorphism:

# Implement a Shape class and derive Circle and Rectangle classes with a method calculate_area. Each class should calculate area differently based on its shape.
# Create a loop to calculate areas for both Circle and Rectangle objects.


class shape:
    print()


class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        print(f"area of circle is {22/7*self.radius*self.radius}")


class rectagle(shape):
    def calculate_area(self, len, brd):
        self.len = len
        self.brd = brd
        print(f"area of rectangle is {self.len*self.brd}")


circle = circle(5)
circle.calculate_area()

rectagle = rectagle()
rectagle.calculate_area(5, 6)
