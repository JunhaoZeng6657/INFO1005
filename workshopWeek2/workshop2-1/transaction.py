class Transaction:
    def __init__(self,transaction_id,transaction_type,amount,description):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description
        self.status = "Pending"

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
