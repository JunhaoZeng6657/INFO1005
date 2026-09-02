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

transaction1 = Transaction(
    "T01",
    "Deposit",
    500,
    "Cash deposit"
)

transaction2 = Transaction(
    "T02",
    "Withdrawal",
    200,
    "ATM withdrawal"
)

transaction3 = Transaction(
    "T03",
    "Transfer",
    300,
    "Transfer payment"
)

branch1 = Branch(
    "B01",
    "City Branch",
    "Adelaide",
    "08 1111 1111"
)

branch2 = Branch(
    "B02",
    "North Branch",
    "North Adelaide",
    "08 2222 2222",
    True
)

branch3 = Branch(
    "B03",
    "West Branch",
    "West Adelaide",
    "08 3333 3333"
)

#Demonstrate Client Methods
print(client1.email)
client1.change_email("newtom@email.com")
print(client1.email)

#Demonstrate Account Methods
print(account1.balance)
account1.deposit(200)
print(account1.balance)

#Demonstrate Transaction Methods
print(transaction1.status)
print(transaction2.status)

transaction1.process_transaction()
transaction2.cancel_transaction()

print(transaction1.status)
print(transaction2.status)

#Change Description
print(transaction3.description)
transaction3.update_description("Payment to another account")
print(transaction3.description)

#Demonstrate Branch Methods
print(branch1.is_open)
branch1.open_branch()
print(branch1.is_open)

branch2.close_branch()
print(branch2.is_open)

#Change phone number
print(branch3.phone_number)
branch3.update_phone_number("08 9999 9999")
print(branch3.phone_number)

