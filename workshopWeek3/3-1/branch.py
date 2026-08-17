class Branch:
    def __init__(self,branch_number,branch_name,location,phone_number,is_open=False):
        self.__branch_number = branch_number
        self.__branch_name = branch_name
        self.__location = location
        self.__phone_number = phone_number
        self.__is_open = is_open

    def open_branch(self):
        self.is_open = True
        print("Branch opened.")

    def close_branch(self):
        self.is_open = False
        print("Branch closed.")

    def update_phone_number(self,new_phone_number):
        self.phone_number = new_phone_number
        print("Phone number updated.")

    def __str__(self):
        if self.is_open:
            opening_state = "Open"
        else:
            opening_state = "Closed"

        return (
            f"Branch{self.branch_number}:"
            f"{self.branch_name},"
            f"{self.location},"
            f"{self.phone_number},"
            f"Status:{opening_state}"
        )

    def __repr__(self):
        return (
            f"Branch(branch_number='{self.branch_number}',"
            f"Branch_name='{self.branch_name}',"
            f"location='{self.location}',"
            f"phone_number='{self.phone_number}',"
            f"is_open={self.is_open})"
        )