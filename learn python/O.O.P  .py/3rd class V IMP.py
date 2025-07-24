#                                    the four pillars of OOP

# 1. Abstraction
# 2. Encapsulation
# 3. Inheritance
# 4. Polymorphism

# what is Abstraction?
# Abstraction is the process of hiding the complex internal details and showing only the essential features of an object to the user.

# son ---> biriyani ---> mother ---> biriyani ---> son

l = [1,2,3,4,5]

l.remove(1)  # metod of list

print(l)

# what is Encapsulation?
# my ans
#  it is the process in which data only accessable thorough methods.
# and it protects the data from external interaction and missing the data, improve security and maintainability.

class atm:
    def __init__(self, card_number):  
        self.__card_number = card_number  # attribute
     

    def check_balance(self):  # method
        print(self.__card_number)
        
t_card = atm("123456789")
t_card.check_balance()  
# print(t_card.__card_number)  it will show error

# t_card.card_number = "1"
# print(t_card.card_number)   only accessable inside the class




#   designing simple database system

class database:
    def __init__(self):
        self.__store = {}  # private

    def write(self, key, value):
        self.__store[key] = value

    def read(self, key):
        if key in self.__store:
            return self.__store[key]
            
        else:
            print("database not found")
            
    
d1 = database()

d1.write("name", "teju")
d1.write("age", 18)
print(d1.read("name"))
print(d1.read("age"))

# print(d1.__store)   # it will show error


d2 = database()

d2.write("name", "raju")
d2.write("age", 20)
print(d2.read("name"))
print(d2.read("age"))

# print(d2.__store)  # it will show error

d3 = database()

d3.write("name", "chidu")
d3.write("age", 19)

print(d3.read("name"))
print(d3.read("age"))  