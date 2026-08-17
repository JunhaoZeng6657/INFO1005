class Transaction:
    def __init__(self,transaction_id,transaction_type,amount,description):
        self.__transaction_id = transaction_id
        self.__transaction_type = transaction_type
        self.__amount = amount
        self.__description = description
        self.__status = "Pending"

    def process_transaction(self):
        if self.status == "Pending":
            self.status = "Processed"
            print("Transaction processed.")
        else:
            print("Transaction cannot be processed.")

    def cancel_transaction(self):
        if self.status == "Pending":
            self.status = "Cancelled"
            print("Transaction cancelled.")
        else:
            print("Transaction cannot be cancelled.")

    def update_description(self,new_description):
        self.description = new_description

    def __str__(self):
        return (
            f"Transaction {self.transaction_id}:"
            f"{self.transaction_type},"
            f"${self.amount:.2f},"
            f"{self.description},"
            f"Status:{self.status}"
        )

    def __repr__(self):
        return (
            f"Transaction(transaction_id='{self.transaction_id}',"
            f"transaction_type='{self.transaction_type}',"
            f"amount={self.amount},"
            f"description='{self.description}',"
            f"status='{self.status}')"
        )