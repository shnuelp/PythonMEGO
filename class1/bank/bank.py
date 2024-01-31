class Bank():

    def __init__(self, account_number, account_holder, balance):
        self.account_holder = account_number
        self.account_holder = account_holder
        self.balance = balance
        with open("bank.txt", "a") as f:
            f.write(f"{account_number},{account_holder},{balance}\n")

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Enter amount positve")


    def withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount
                print("\n You Withdrew:", amount)
            else:
                print(" balance ")


a=Bank(1234,"ABA",150)
a.deposit()
print(a.balance)

