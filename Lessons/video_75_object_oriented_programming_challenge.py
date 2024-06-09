# Create a bank account object
class Account() :
    def __init__(self, owner, balance) :
        self.owner = owner
        self.balance = balance

    def __str__(self) :
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

    def deposit(self, depositAmount) :
        self.balance = self.balance + depositAmount
        return f"Deposit Accepted"

    def withdraw(self, withdrawAmount) :
        if withdrawAmount > self.balance :
            return f"Funds Unavailable!"
        else :
            self.balance = self.balance - withdrawAmount
            return f"Withdrawal Accepted"
        
acct1 = Account(owner = "Jose", balance = 1200)
print(f"Initial Balance Post Creation: R{acct1.balance}")

print(acct1.deposit(200))


print(acct1.withdraw(2500))

print(acct1)

print(acct1.owner)
print(acct1.balance)