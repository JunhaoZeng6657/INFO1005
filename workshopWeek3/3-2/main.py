from client import Client
from account import Account
from transaction import Transaction
from branch import Branch

# Show all methods
client1 = Client("A01", "Tom", "tom@email.com")
client2 = Client("A02", "Jack", "jack@email.com")
client3 = Client("A03", "Amy", "amy@email.com")

account1 = Account("A01", "Savings", 1000)
account2 = Account("A02", "Checking", 2000)

transaction1 = Transaction("T01", "Deposit", 500, "Cash deposit")
transaction2 = Transaction("T02", "Withdrawal", 300, "ATM withdrawal")

branch1 = Branch(
    "B01",
    "Main Branch",
    "Adelaide",
    "08 1234 5678"
)

branch2 = Branch(
    "B02",
    "City Branch",
    "Adelaide",
    "08 8765 4321"
)

# Client
print(client1)
client1.set_name("Thomas")
client1.set_name(123)   #Invalid name
print(client1)

# Account
print(account1)
account1.deposit(200)
account1.withdraw(150)
account1.withdraw(5000) #Not enough funds
print(account1)
print(account2)

# Transaction
print(transaction1)
transaction1.process_transaction()
print(transaction1)

transaction2.cancel_transaction()
print(transaction2)

# Branch
print(branch1)
branch1.open_branch()
branch1.set_phone_number("08 1111 2222")
print(branch1)

branch2.close_branch()
print(branch2)

# Aggregate relationships
client1.add_account(account1)
client1.add_account(account2)
client1.display_accounts()

# Association relationship
client1.visit_branch(branch1)
client1.visit_branch(branch2) #Invalid object