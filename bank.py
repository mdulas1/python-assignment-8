"""
TASK: Create a BankAccount class.

Requirements:
1. Each account should have an owner name and a starting balance.
2. Provide a method to deposit money.
3. Provide a method to withdraw money (only if sufficient balance).
4. Provide a method to check current balance.

Example Usage:
    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc.get_balance())  # 1300
"""
class BankAccont:
  def __init__(self,name, account_number,balance=0):
    self.name = name
    self.account_number = account_number
    self.balance = balance
  
  def deposit(self,amount):
    if amount > 0:
      self.balance += amount
      print(f"dear {self.name} your acct {self.account_number} has been credited with {amount} and your new account balace is {self.balance}")
    else:
      print("invalid amount must be > 0 naira")

  def withdraw(self,amount):
    if amount > self.balance:
      print(f"insufficient balance")
    else:
      self.balance - amount
      print(f"dear {self.name} your account has beed debted with {amount} and your new acct/balance: {self.balance - amount}")
  
  def check_balance(self,):
    return self.balance

  
  

jibrin = BankAccont("jibrin tanimu",1111,)
godiya = BankAccont("godiya joshua",1112)
oklo = BankAccont("Oklo yakubu",1123)
victor = BankAccont("victor jatau",1234)
vincent = BankAccont("vincent sati",72344)
vincent.deposit(30000)
vincent.deposit(50000)
print(oklo.check_balance())
print(vincent.check_balance())
vincent.withdraw(30000)

