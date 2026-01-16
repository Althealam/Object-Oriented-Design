# Goal: Prevent external code from directly modifying internal data
# Think First:
# 1. Which data should be protected
# 2. How should outside code interact with it?
# BankAccount only show deposit, withdraw, get the balance of the bank account for outside.
# So these three methods are abstraction layers

class BankAccount:
    def __init__(self):
        # we can not change the data directly
        # initial balance in the bank account
        # This is the most important thing for encapsulation
        self.__balance = 0 # Encapsulation: private internal state

    def deposit(self, amount): # Abstraction: public operation
        if amount<=0:
            raise ValueError("amount must be positive")
        self.__balance+=amount
    
    def withdraw(self, amount): # Abstraction
        if amount<=0:
            raise ValueError("amount must be positive")
        if amount>=self.__balance:
            raise ValueError("insufficient funds")
        self.__balance-=amount
    
    def get_balance(self): # Abstraction: read-only access
        return self.__balance
    
account = BankAccount()
account.deposit(100)
account.withdraw(30)
print(account.get_balance())