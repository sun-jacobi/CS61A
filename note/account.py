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

class  CheckingAccount(Account):
    withdraw_fee = 1
    interest = 0.01
    def withdraw(self, amount):
        return super().withdraw(amount + self.withdraw_fee)
    

class SavingAccount(Account):
    deposit_charge = 2
    def deposit(self,amount):
        return Account.deposit(self,amount - self.deposit_charge)
    
    
class MutAccount(CheckingAccount,SavingAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1
    