class Client:
    def __init__(self,client_id,name,email):
        self.__client_id = client_id
        self.__name = name
        self.__email = email

    def change_email(self,new_email):
        self.__email = new_email

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
        self.__name = new_name

    def set_email(self,new_email):
        self.__email = new_email

    