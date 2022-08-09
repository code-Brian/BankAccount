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
        return self
    def withdraw(self, amount):
        # withdraw the amount from the balance variable
        if (self.balance < amount):
            print(f"Insufficient funds! Available balance is {self.balance}. Requested amount: {amount}")
        else:
            self.balance = self.balance - amount
        return self
    def display_account_info(self):
        # show all the information associated with the account
        print(f"The interest rate on is: {self.int_rate}")
        print(f"The available balance is: {self.balance}")
        return self
    def yield_interest(self):
        # increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if (self.balance > 0):
            self.balance = self.balance + (self.balance * self.int_rate)
        return self

rickAccount = BankAccount(0.420, 69)
mortyAccount = BankAccount(0.420, 69)

rickAccount.deposit(5).deposit(17).deposit(4).withdraw(1).yield_interest().display_account_info()
mortyAccount.deposit(50).deposit(690).withdraw(1).withdraw(2).withdraw(3).withdraw(4).yield_interest().display_account_info()

# Ninja bonus!!!!