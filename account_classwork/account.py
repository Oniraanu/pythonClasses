class Account:
    def __init__(self, name):
        self.balance = 0
        self.name = name

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("You cannot withdraw more than balance")
        else:
            self.balance -= amount

    def mobile_top_up(self, amount):
        self.balance -= amount

    def transfer(self, transfer_amount, transfer_to):
        self.balance -= transfer_amount



