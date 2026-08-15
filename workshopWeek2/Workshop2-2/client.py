class Client:
    def __init__(self,client_id,name,email):
        self.client_id = client_id
        self.name = name
        self.email = email

    def change_email(self,new_email):
        self.email = new_email

    def __str__(self):
        return  f"Client {self.client_id}:{self.name},Content:{self.email}"

    def __repr__(self):
        return (
            f"Client(client_id='{self.client_id}',"
            f"name='{self.name}',"
            f"email='{self.email}')"
        )
            