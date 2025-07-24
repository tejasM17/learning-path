# .                                  Homework
# Create a Class with a Constructor:

# Write a class Movie with attributes title and rating using the __init__() constructor.
# Define a method to display the movie’s title and rating.
# Add Default Parameters:

# Create a class Employee with attributes name, designation, and salary (default value of salary is 30,000).
# Write a method that displays the details of each employee.
# Create multiple Employee objects with different values for name and designation, and test the default salary behavior

class movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def display_info(self):
        print(f"{self.title} has a rating of {self.rating}")

movie1 = movie("The INTERSTELLAR rating is" , 9.3)
movie2 = movie("The kingdoms of heven has a rating", 9.2)

movie1.display_info()
movie2.display_info()


class Employee:
    def __init__(self, name, designation, profit=10000000000):
        self.name = name
        self.designation = designation
        self.profit = profit

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")
        print(f"Profit: {self.profit}")

employee1 = Employee("raju", "entripreneur", "infinity")
employee2 = Employee("Tejas", "Developer", 5)

employee1.display_info()
employee2.display_info()    

