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

print(client1)
print(account1)

print(client1.get_name())

client1.set_name("Thomas")
print(client1.get_name())

client1.set_name(123)
print(client1.get_name())

#Test account validation
print(account1.get_balance())

account1.deposit(200)
print(account1.get_balance())

account1.deposit("hello")
print(account1.get_balance())

#Create relationships
client1.add_account(account1)
client1.add_account(account2)

client2.add_account(account3)

#Display relationship
print("Client 1 account:")
client1.display_accounts()

print("Client 2 account:")
client2.display_accounts()

#Test invalid relationship
client1.add_account("Not an account")