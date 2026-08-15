class Client:
    def __init__(self,client_id,name,email):
        self.client_id = client_id
        self.name = name
        self.email = email

    def change_email(self,new_email):
        self.email = new_email