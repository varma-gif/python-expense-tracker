class BankAccount:
    def __init__(self, owner, acc_no, bal):
        self.owner = owner
        self.acc_no = acc_no
        self.bal = bal

    def display(self):
        print(f"Account Owner Name : {self.owner}")
        print(f"Account Number : {self.acc_no}")
        print(f"Account Balance : {self.bal}")

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be Positive")
        else:
            print("=" * 35)
            print(f"Amount to be Deposited : {amount}")
            print(f"Previous Balance:{self.bal}")
            self.bal = self.bal + amount
            print(f"Latest Balance : {self.bal}")
            print("=" * 35)
    def withdraw(self,amount):
        if amount <=0:
            print("Amount must be Positive")
        elif amount >self.bal:
            print(f"Your balance :{self.bal},Insufficeint Balance, you are trying to")
        else:
            print("=" * 35)
            print(f"Amount to be Deposited : {amount}")
            print(f"Previous Balance:{self.bal}")
            self.bal = self.bal - amount
            print(f"Latest Balance : {self.bal}")
            print("=" * 35)
if __name__ == "__main__":
    acc1 = BankAccount("Yashwanth", 10, 10000)
    acc2 = BankAccount("Mani", 20, 20000)
    acc1.display()
    acc2.display()
    acc1.deposit(1000)
    acc2.deposit(2000)
    acc1.withdraw(500)
    acc2.withdraw(230)
