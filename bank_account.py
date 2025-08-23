from abc import ABC, abstractmethod
from datetime import datetime


# 🔹 Abstract Class
class Account(ABC):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # Encapsulation (private balance)
        self.transactions = []     # Store transaction history

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__add_transaction("Deposit", amount)
            print(f"{self.owner} deposited {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if self._can_withdraw(amount):  # Different rules for different accounts
            self.__balance -= amount
            self.__add_transaction("Withdraw", amount)
            print(f"{self.owner} withdrew {amount}. New Balance: {self.__balance}")
        else:
            print("❌ Withdrawal not allowed!")

    def get_balance(self):
        return self.__balance

    def __add_transaction(self, type, amount):
        self.transactions.append({
            "type": type,
            "amount": amount,
            "balance": self.__balance,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def show_transactions(self):
        print(f"\n📜 Transaction history for {self.owner}:")
        for t in self.transactions:
            print(
                f"{t['time']} - {t['type']} {t['amount']} | Balance: {t['balance']}")

    @abstractmethod
    def _can_withdraw(self, amount):
        """Check if withdrawal is possible (subclass specific rules)"""
        pass

    @abstractmethod
    def account_type(self):
        pass


# 🔹 Savings Account
class SavingsAccount(Account):
    INTEREST_RATE = 0.03  # 3% interest

    def _can_withdraw(self, amount):
        return amount <= self.get_balance()  # No overdraft

    def add_interest(self):
        interest = self.get_balance() * self.INTEREST_RATE
        self.deposit(interest)
        print(f"💰 Interest added: {interest}")

    def account_type(self):
        return "Savings Account"


# 🔹 Current Account
class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 500

    def _can_withdraw(self, amount):
        return amount <= self.get_balance() + self.OVERDRAFT_LIMIT

    def account_type(self):
        return "Current Account"


# 🔹 Polymorphism
def print_account_info(account: Account):
    print(
        f"\n👤 {account.owner} has a {account.account_type()} | Balance: {account.get_balance()}")


# 🔹 Example Usage
if __name__ == "__main__":
    acc1 = SavingsAccount("Alice", 1000)
    acc2 = CurrentAccount("Bob", 300)

    acc1.deposit(500)
    acc1.withdraw(200)
    acc1.add_interest()

    acc2.withdraw(700)  # Uses overdraft
    acc2.deposit(400)

    print_account_info(acc1)
    print_account_info(acc2)

    acc1.show_transactions()
    acc2.show_transactions()
