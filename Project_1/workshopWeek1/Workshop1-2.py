class Client:
    def __init__(self,client_id,name,email):
        self.client_id = client_id
        self.name = name
        self.email = email

    def change_email(self,new_email):
        self.email = new_email

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


client1 = Client("A01","Tom","tom@email.com")
client2 = Client("A02","Jack","jack@email.com")
client3 = Client("A03","Amy","amy@email.com")

account1 = Account("A01","Savings",1000)
account2 = Account("A02","Checking",2000)
account3 = Account("A03","Savings",500)

print(client1.name)
print(client2.email)

print(client2.name)
print(client2.email)

print(account1.balance)
print(account2.balance)

#Change email function
client1.change_email("newtom@email.com")
client2.change_email("newjack@email.com")

print(client1.email)
print(client2.email)

#Saving money
account1.deposit(200)
account2.deposit(500)

#withdraw
account1.withdraw(100)
account2.withdraw(300)

#Print balance
print(account1.balance)
