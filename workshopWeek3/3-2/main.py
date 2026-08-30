from client import Client
from account import Account
from transaction import Transaction
from branch import Branch

client1 = Client("A01","Tom","tom@email.com")
client2 = Client("A02","Jack","jack@email.com")
client3 = Client("A03","Amy","amy@email.com")

account1 = Account("A01","Savings",1000)
account2 = Account("A02","Checking",2000)
account3 = Account("A03","Savings",500)

branch1 = Branch(
    "B01",
    "Main Branch",
    "Adelaide",
    "08 1234 5678"
    )

print(client1.get_name())
print(account1.get_balance())

client1.set_name("Thomas")
print(client1.get_name())

client1.set_name(123)
print(client1.get_name())

client1.add_account(account1)
client1.add_account(account2)

client1.display_accounts()

client1.visit_branch(branch1)
