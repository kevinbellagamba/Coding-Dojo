class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    def show_balance(self, amount):
        self.account_balance = amount
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawl(amount)
        

kevin = User("Kevin Bellagamba")
dan = User("Daniel Romanello")
jack = User("Jack Shaw")

kevin.make_deposit(500)
kevin.make_deposit(500)
kevin.make_deposit(500)
kevin.make_withdrawl(300)
print(kevin.account_balance)

dan.make_deposit(1000)
dan.make_deposit(2000)
dan.make_withdrawl(500)
dan.make_withdrawl(200)
print(dan.account_balance)

jack.make_deposit(4000)
jack.make_withdrawl(1000)
jack.make_withdrawl(1000)
jack.make_withdrawl(1000)
print(jack.account_balance)

dan.transfer_money(kevin,200)
print(kevin.account_balance)
print(dan.account_balance)

