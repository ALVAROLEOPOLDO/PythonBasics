class BankAccount:
    def  __init__(self, num_account, name, balance):
        self.num_account=num_account
        self.name=name
        self.balance=balance

    def generate_balance(self):
        print(self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

mybankaccount= BankAccount("10523546", "James Yr", 5600)

mybankaccount.generate_balance()
mybankaccount.deposit(400)
mybankaccount.generate_balance()
    

