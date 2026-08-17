class Account:
    def __init__(self,account_number,account_type,balance):
        self.__account_numberaccount_number = account_number
        self.__account_type = account_type
        self.__balance = balance

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

    def get_account_number(self):
        return self.__account_number

    def get_account_type(self):
        return self.__account_type

    def set_account_type(self,new_account_type):
        self.__account_type = new_account_type

    def get_balance(self):
        return self.__balance