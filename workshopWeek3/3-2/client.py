from account import Account
from branch import Branch
# The Client class stores client information.
# It also manages the client's accounts and interacts with branches.
class Client:
    def __init__(self,client_id,name,email):
        self.__client_id = client_id
        self.set_name(name)
        self.set_email(email)
        self.__account = []

    def change_email(self,new_email):
        self.set_email(new_email)

    def __str__(self):
        return  (
            f"Client {self.__client_id}:"
            f"{self.__name},Content:{self.__email}"
            )
    def __repr__(self):
        return (
            f"Client(client_id='{self.__client_id}',"
            f"name='{self.__name}',"
            f"email='{self.__email}')"
        )

    def get_client_id(self):
        return self.__client_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def set_name(self,new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print("Invalid name.")


    def set_email(self,new_email):
        if isinstance(new_email, str):
            self.__email = new_email
        else:
            print("Invalid email.")

    def add_account(self,account):
        if isinstance(account,Account):
            self.__account.append(account)
            print("Account added.")
        else:
            print("Invalid account.")

    def display_accounts(self):
        for account in self.__account:
            print(account)

    def visit_branch(self,branch):
        if isinstance(branch,Branch):
            print(f"{self.__name} is visiting {branch.get_branch_name()}.")
        else:
            print("Invalid branch.")