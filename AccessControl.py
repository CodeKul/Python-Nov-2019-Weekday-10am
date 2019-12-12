class Account:
    def __init__(self, name, acc_no, phone):
        super().__init__()
        self.name = name
        self.acc_no = acc_no
        self.phone = phone
        self.__balance = 0

    def display(self):
        print("Name:", self.name)
        print("Account no:", self.acc_no)
        print("Phone:", self.phone)
        print("Balance:", self.__balance)

    def deposite(self, amt):
        self.__balance += amt
        print("Money is deposited")

    def withdraw(self, amt):
        self.__balance -= amt
        print("Money is withdraw")

    def monthly_calc(self):
        self.__balance += self.__calculate_interest()

    def __calculate_interest(self):
        interest = self.__balance * 0.07
        return interest
    

a1 = Account("ABCD", 12345, 9999999999)
a1.deposite(1000)
a1.display()
a1.withdraw(100)
a1.display()

a1.balance = 10000
a1.display()

a1.monthly_calc()
a1.display()
