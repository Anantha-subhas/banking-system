#Deposit,Withdraw,check balance

class BankAccount:
    def __init__(self,account_number,initial_balance):
        #validate the argument which is easy to debug later
        assert initial_balance >=1,f"initial_balance{initial_balance} is less than 1"
        self.account_number = account_number
        self.initial_balance = initial_balance
    
    def deposit(self,amount):
        self.initial_balance = self.initial_balance + amount #updated NOTE which is  append on above constructor and it accessed anywhere in this class bank account
        return f"deposited amount = {amount} total balance ={self.initial_balance}"
    def with_draw(self,amount):
        if self.initial_balance >= amount:
            self.initial_balance = self.initial_balance - amount
            return f"with_draw amount = {amount} total balance {self.initial_balance}"
        
        return "you doesn't have enough balance!! sir"
    def check_balance(self):
        return f"Account {self.account_number} has a Balance ==> {self.initial_balance}"
    
p1 = BankAccount(333,0)
print(p1.check_balance())
# print(p1.with_draw(500))

# print(p1.deposit(1000))
# print(p1.check_balance())



    
            