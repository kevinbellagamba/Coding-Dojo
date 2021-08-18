class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def show_balance(self):
        print(self.account_balance)
        return self
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawl(amount)
        return self
        

kevin = User("Kevin Bellagamba")
dan = User("Daniel Romanello")
jack = User("Jack Shaw")

kevin.make_deposit(500).make_deposit(500).make_deposit(500).make_withdrawl(300).show_balance()

dan.make_deposit(1000).make_deposit(2000).make_withdrawl(500).make_withdrawl(200).show_balance()

jack.make_deposit(4000).make_withdrawl(1000).make_withdrawl(1000).make_withdrawl(1000).show_balance()

dan.transfer_money(kevin,200).show_balance()
kevin.show_balance()
