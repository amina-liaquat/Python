from datetime import datetime

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute
        self.__transactions = []  # List to track transaction history

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__record_transaction("Deposit", amount)
            print(f"Deposited {amount}, New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount <= self.__balance:
            self.__balance -= amount
            self.__record_transaction("Withdraw", -amount)
            print(f"Withdrew {amount}, Remaining Balance: {self.__balance}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

    def transfer(self, amount, recipient_account):
        if amount <= 0:
            print("Transfer amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance for transfer!")
        else:
            self.withdraw(amount)
            recipient_account.deposit(amount)
            self.__record_transaction(f"Transfer to {recipient_account.owner}", -amount)
            recipient_account.__record_transaction(f"Transfer from {self.owner}", amount)
            print(f"Transferred {amount} to {recipient_account.owner}")

    def apply_interest(self, rate_percent):
        if rate_percent > 0:
            interest = self.__balance * (rate_percent / 100)
            self.__balance += interest
            self.__record_transaction("Interest", interest)
            print(f"Applied {rate_percent}% interest. Interest: {interest:.2f}, New Balance: {self.__balance:.2f}")
        else:
            print("Interest rate must be positive.")

    def show_transactions(self):
        if not self.__transactions:
            print("No transactions yet.")
        else:
            print(f"Transaction history for {self.owner}:")
            for t in self.__transactions:
                print(f"{t['timestamp']} - {t['type']}: {t['amount']}")

    def __record_transaction(self, transaction_type, amount):
        self.__transactions.append({
            "type": transaction_type,
            "amount": amount,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self.__balance:.2f})"
