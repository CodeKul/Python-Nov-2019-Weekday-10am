class Employee:
    def __init__(self, name, Id, salary):
        super().__init__()
        self.name = name
        self.Id = Id
        self.salary = salary

    def display(self):
        print("Id:", self.Id)
        print("Name:", self.name)
        print("Salry:", self.salary)

    def increment(self):
        self.salary += (self.salary * 0.3)


class Developer(Employee):
    def __init__(self, name, Id, salary, deskId):
        super().__init__(name, Id, salary)
        self.deskId = deskId

    def display(self):
        super().display()
        print("Desk Id:", self.deskId)


class Manager(Employee):
    def __init__(self, name, Id, salary, cabinId):
        super().__init__(name, Id, salary)
        self.cabinId = cabinId

    def display(self):
        super().display()
        print("Cabin Id:", self.cabinId)

class Company:
    def __init__(self, name, employees):
        super().__init__()
        self.name = name
        self.employees = employees

    def display(self):
        print("Company Name:", self.name)
        self.show_list_employees()

    def show_list_employees(self):
        for emp in self.employees:
            print("Type:", type(emp))
            emp.display()

    def promote_all(self):
        for emp in self.employees:
            print("Type:", type(emp))
            emp.increment()

dev1 = Developer("ABC", 1, 10000, 101)
dev2 = Developer("XYZ", 2, 12000, 102)

man1 = Manager("PQR", 3, 20000, 103)
man2 = Manager("LMN", 4, 30000, 104)

# dev1.display()
# dev2.display()
# man1.display()
# man2.display()

# dev1.increment()
# dev1.display()

com1 = Company("CODEKUL", [dev1, dev2, man1, man2])
com1.display()
com1.promote_all()
com1.display()