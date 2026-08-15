class Account:
    def __init__(self,account_number,account_type,balance):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Insufficient funds")

    def __str__(self):
        return (
            f"Account {self.account_number}:"
            f"{self.account_type},Balance:${self.balance:.2f}")

    def __repr__(self):
        return (
            f"Account(account_number='{self.account_number}',"
            f"account_type='{self.account_type}"
            f"balance={self.balance})"
        )