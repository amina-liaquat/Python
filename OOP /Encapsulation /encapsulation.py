class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}, New Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}, Remaining Balance: {self.__balance}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

# Usage
acc = BankAccount("Amina", 500)
acc.deposit(200)
acc.withdraw(100)
print(acc.get_balance())  # 600
