
# Problem 1

class BankAccount:
    def __init__(self, account_number, customer_name, balance, date_of_opening):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)
        print("New balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance. Withdrawal cancelled.")
        else:
            self.balance = self.balance - amount
            print("Withdrew:", amount)
            print("New balance:", self.balance)

    def check_balance(self):
        print("Account Number :", self.account_number)
        print("Customer Name  :", self.customer_name)
        print("Date of Opening:", self.date_of_opening)
        print("Balance        :", self.balance)

account1 = BankAccount("23-50916-1", "Esrat Jahan", 5000, "2026-08-08")
account1.check_balance()
print()
account1.deposit(1500)
print()
account1.withdraw(2000)
print()
account1.withdraw(10000)
print()



# Problem 2:

class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        return amount + amount * 0.10


v1 = Vehicle("Car", 5)
print(v1.name, "fare:", v1.fare())

b1 = Bus("Bus", 40)
print(b1.name, "fare:", b1.fare())
