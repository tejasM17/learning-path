#                                                 HOMEWORK

# Abstraction:

# Design a Phone class with methods to call_contact and take_picture. Abstract away any internal processing details and focus on creating a user-friendly interface.


class Phone:
    def call_contact(self):
        
        print("Calling contact...")

    def take_picture(self):
        print("Taking picture...")

    def __init__(self):
        pass

phone = Phone()
phone.call_contact()
phone.take_picture()





# Encapsulation:

# Create a BankAccount class with private attributes for account_number and balance.
# Add methods to check balance, deposit, and withdraw funds.
# Try accessing the balance directly and observe the result.


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def check_balance(self):
        return self.__balance

    def account_number(self):
        return self.__account_number
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance.")



balance = BankAccount("123456", 1000)

balance.deposit(500)
print(balance.check_balance())
balance.withdraw(2000)  # output: Insufficient balance   
balance.withdraw(600)
print(balance.check_balance())# This will raise an AttributeError
