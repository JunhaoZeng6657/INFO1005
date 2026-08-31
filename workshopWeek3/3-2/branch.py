# The Branch class stores branch information.
# It manages contact details and opening status.
class Branch:
    """Represents a financial branch and manages branch information."""
    def __init__(self,branch_number,branch_name,location,phone_number,is_open=False):
        self.__branch_number = branch_number
        self.__branch_name = branch_name
        self.__location = location
        self.set_phone_number(phone_number)
        self.__is_open = is_open

    def open_branch(self):
        self.__is_open = True
        print("Branch opened.")

    def close_branch(self):
        self.__is_open = False
        print("Branch closed.")

    def update_phone_number(self,new_phone_number):
        self.__phone_number = new_phone_number
        print("Phone number updated.")

    def __str__(self):
        if self.__is_open:
            opening_state = "Open"
        else:
            opening_state = "Closed"

        return (
            f"Branch{self.__branch_number}:"
            f"{self.__branch_name},"
            f"{self.__location},"
            f"{self.__phone_number},"
            f"Status:{opening_state}"
        )

    def __repr__(self):
        return (
            f"Branch(branch_number='{self.__branch_number}',"
            f"Branch_name='{self.__branch_name}',"
            f"location='{self.__location}',"
            f"phone_number='{self.__phone_number}',"
            f"is_open={self.__is_open})"
        )

    def get_branch_number(self):
        return self.__branch_number

    def get_branch_name(self):
        return self.__branch_name

    def get_location(self):
        return self.__location

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self,new_phone_number):
        if isinstance(new_phone_number, str):
            self.__phone_number = new_phone_number
        else:
            print("Invalid phone number.")

    def get_is_open(self):
        return self.__is_open