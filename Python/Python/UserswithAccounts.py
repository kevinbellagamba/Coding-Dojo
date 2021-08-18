class BankAccount:
    def __init__(self, int_rate=1, balance=0):
        self.int_rate = (int_rate * .01)
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance += interest
        return self

class User:
    def __init__(self, name, int_rate=0, balance=0):
        self.name = name
        self.account = BankAccount(int_rate, balance)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawl(amount)
        return self

user1=User('Kevin')

user1.make_deposit(100).make_deposit(300).make_withdrawl(350).display_user_balance()

user2=User('Bob',.2,1000)

user2.make_withdrawl(100).make_withdrawl(200)

user2.display_user_balance()
user2.account.yield_interest()
user2.display_user_balance()