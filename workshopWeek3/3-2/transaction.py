# The Transaction class stores transaction information.
# It manages the processing status of a transaction.
class Transaction:
    """Represents a financial transaction and mananges its status."""
    def __init__(self,transaction_id,transaction_type,amount,description):
        self.__transaction_id = transaction_id
        self.__transaction_type = transaction_type
        self.__amount = amount
        self.set_description(description)
        self.__status = "Pending"

    def process_transaction(self):
        if self.__status == "Pending":
            self.__status = "Processed"
            print("Transaction processed.")
        else:
            print("Transaction cannot be processed.")

    def cancel_transaction(self):
        if self.__status == "Pending":
            self.__status = "Cancelled"
            print("Transaction cancelled.")
        else:
            print("Transaction cannot be cancelled.")

    def update_description(self,new_description):
        self.set_description(new_description)

    def __str__(self):
        return (
            f"Transaction {self.__transaction_id}:"
            f"{self.__transaction_type},"
            f"${self.__amount:.2f},"
            f"{self.__description},"
            f"Status:{self.__status}"
        )

    def __repr__(self):
        return (
            f"Transaction(transaction_id='{self.__transaction_id}',"
            f"transaction_type='{self.__transaction_type}',"
            f"amount={self.__amount},"
            f"description='{self.__description}',"
            f"status='{self.__status}')"
        )

    def get_transaction_id(self):
        return self.__transaction_id

    def get_transaction_type(self):
        return self.__transaction_type

    def get_amount(self):
        return self.__amount

    def get_description(self):
        return self.__description

    def get_status(self):
        return self.__status

    def set_description(self,new_description):
        if isinstance(new_description, str):
            self.__description = new_description
        else:
            print("Invalid description.")