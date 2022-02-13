class Account:
    def __init__(self, account):
        self.balance = 0 
        self.holdeer = account
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        if amount  > self.balance:
            return " no money" 
        self.balance = self.balance - amount
        return self.balance
        