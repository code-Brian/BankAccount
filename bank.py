# Woohoo! We got this! :)

# let's create the BankAccount class
class BankAccount:
    # initializer/constructor for bank account
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        # deposit the amount to the balance variable
        self.balance = self.balance + amount
    def withdraw(self, amount):
        # withdraw the amount from the balance variable
        if (self.balance < amount):
            print(f"Insufficient funds! Available balance is {self.balance}. Requested amount: {amount}")
        else:
            self.balance = self.balance - amount
    def display_account_info(self):
        # show all the information associated with the account
        print(f"Your interest rate is: {self.int_rate}")
        print(f"Your available balance is: {self.balance}")
    def yield_interest(self):
        # increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if (self.balance > 0):
            self.balance = self.balance * self.int_rate
        return self.balance

rickAccount = BankAccount(0.420, 69)
mortyAccount = BankAccount(0.420, 69)
