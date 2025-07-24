"""
Banking System Simulation
-------------------------
A menu-driven program that simulates a basic banking system with options to:
- Check Balance
- Deposit Money
- Withdraw Money
- Exit
"""

class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
        account_holder (str): Name of the account holder
        account_number (str): Account number
        balance (float): Current account balance
    """

    def __init__(self, account_holder, account_number, initial_balance=1000.0):
        """
        Initialize a new bank account.

        Args:
            account_holder (str): Name of the account holder
            account_number (str): Account number
            initial_balance (float, optional): Initial account balance. Defaults to 1000.0.
        """
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

    def check_balance(self):
        """
        Check and return the current account balance.

        Returns:
            float: Current account balance
        """
        return self.balance

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount (float): Amount to deposit

        Returns:
            bool: True if deposit was successful, False otherwise
            str: Success or error message
        """
        try:
            amount = float(amount)
            if amount <= 0:
                return False, "Error: Deposit amount must be positive."

            self.balance += amount
            return True, f"Success: ${amount:.2f} has been deposited."
        except ValueError:
            return False, "Error: Please enter a valid number."

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Args:
            amount (float): Amount to withdraw

        Returns:
            bool: True if withdrawal was successful, False otherwise
            str: Success or error message
        """
        try:
            amount = float(amount)
            if amount <= 0:
                return False, "Error: Withdrawal amount must be positive."

            if amount > self.balance:
                return False, "Error: Insufficient funds. Cannot withdraw more than your balance."

            self.balance -= amount
            return True, f"Success: ${amount:.2f} has been withdrawn."
        except ValueError:
            return False, "Error: Please enter a valid number."


def display_menu():
    """Display the main menu options."""
    print("\n===== BANKING SYSTEM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


def main():
    """Main function to run the banking system."""
    # Create a bank account with default values
    account = BankAccount("John Doe", "ACC123456", 1000.0)

    while True:
        display_menu()

        # Get user choice
        try:
            choice = input("\nEnter your choice (1-4): ")

            if choice == '1':
                # Check balance
                balance = account.check_balance()
                print(f"Current balance: ${balance:,.2f}")

            elif choice == '2':
                # Deposit money
                amount = input("Enter amount to deposit: $")
                success, message = account.deposit(amount)
                print(message)
                if success:
                    print(f"New balance: ${account.balance:,.2f}")

            elif choice == '3':
                # Withdraw money
                amount = input("Enter amount to withdraw: $")
                success, message = account.withdraw(amount)
                print(message)
                if success:
                    print(f"New balance: ${account.balance:,.2f}")

            elif choice == '4':
                # Exit the program
                print("Thank you for using our banking system. Goodbye!")
                break

            else:
                print("Error: Invalid choice. Please enter a number between 1 and 4.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
