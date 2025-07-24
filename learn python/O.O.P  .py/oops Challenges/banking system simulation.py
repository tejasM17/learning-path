# Design a system to simulate a bank's operations, where users can create accounts, deposit and withdraw money, and check their account balance.

# Extend functionality to include multiple account types (e.g., savings, current) with unique behaviors like interest calculation or overdraft limits.
# Emphasize encapsulation, inheritance and polymorphism.

class Account:
    def __init__(self, id, holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0   # Encapsulation
        pass

    def check_balance (self):
        print(f"Balance : {self._balance}")

    def deposit(self, amount):
        self._balance += amount
        print(f"Depositted total money: {self._balance}")
    
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"withdra successful & total money: {self._balance}")
        else:
            print("You don't have that much of Money")


class SavingsAccount(Account):  # Inheritance
    def calculate_interest(self):
        INTEREST_RATE = 0.05
        interest = self._balance * INTEREST_RATE
        print(f"Interest earned: {interest}")


class CurrentAccount(Account):
    def withdraw(self, amount):  # polymorphism
        OVERDRAFT_LIMIT = 500
        if self._balance + OVERDRAFT_LIMIT >= amount:
            self._balance -= amount
            print(f"withdra successful & total money: {self._balance}")
        else:
            print("your limit is over")
    
class Bank:
    def __init__(self,name, location,):
        self.name = name
        self.location = location
        self.__accounts = {}

    def create_account(self, id, holder_name, account_type):
        if account_type == "savings":
            new_account = SavingsAccount(id, holder_name)
        elif account_type == "current":
            new_account = CurrentAccount(id, holder_name)
        self.__accounts[id] = new_account
        print(f"Account created for {holder_name} with ID {id}.")
        return new_account
    
    def get_account(self, id):
        if id not in self.__accounts:
            print(f"No account found with ID {id}.")
            return None
        else:
            account = self.__accounts[id]
            print(f"\nID: {account.id} \n Holder Name: {account.holder_name} \n Balance: {account._balance}")
            return account
        
RCSMT = Bank("Brothers Bank of India", "DUBAI")

sav1 = RCSMT.create_account(4444, "1st_bro", "savings")
cr1 = RCSMT.create_account(5555, "2nd_bro", "current")

sav1.deposit(1000)
cr1.deposit(20)

sav1.withdraw(2000)
cr1.withdraw(100)

sav1.calculate_interest()