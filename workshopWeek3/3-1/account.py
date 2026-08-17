class Account:
    def __init__(self,account_number,account_type,balance):
        self.__account_number = account_number
        self.__account_type = account_type
        self.__balance = balance

    def deposit(self,amount):
        if isinstance(amount, (int, float)):
            if amount > 0:
                self.__balance = self.__balance + amount
                print("Deposit successful.")
            else:
                print("Invalid amount.")
        else:
            print("Invalid amount.")
            
    def withdraw(self,amount):
        if isinstance(amount, (int, float)):
            if amount > 0:
                if amount <= self.__balance:
                    self.__balance = self.__balance - amount
                    print("Withdrawal successful.")
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid amount.")
        else:
            print("Invalid amount.")

    def __str__(self):
        return (
            f"Account {self.__account_number}:"
            f"{self.__account_type},Balance:${self.__balance:.2f}"
            )

    def __repr__(self):
        return (
            f"Account(account_number='{self.__account_number}',"
            f"account_type='{self.__account_type}"
            f"balance={self.__balance})"
        )

    def get_account_number(self):
        return self.__account_number

    def get_account_type(self):
        return self.__account_type

    def set_account_type(self,new_account_type):
        if isinstance(new_account_type, str):
            self.__account_type = new_account_type
        else:
            print("Invalid account type.")

    def get_balance(self):
        return self.__balance