class BankAccount:
    def __init__(self, int_rate=1, balance=0):
        self.int_rate = (int_rate * .01)
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawl(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance += interest
        return self

account1 = BankAccount()
account2 = BankAccount()

account1.deposit(500).deposit(500).deposit(500).withdrawl(300).yield_interest().display_account_info()

account2.deposit(2000).deposit(1000).withdrawl(400).withdrawl(300).withdrawl(200).withdrawl(100).yield_interest().display_account_info()