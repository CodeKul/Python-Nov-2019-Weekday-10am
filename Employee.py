class Employee:

    def __init__(self, emp_id, emp_name, emp_salary, designation):
        super().__init__()
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.designation = designation

    def display(self):
        print("Id:", self.emp_id)
        print("Name:", self.emp_name)
        print("Salary:", self.emp_salary)
        print("Designation:", self.designation)

    def increament(self):
        self.emp_salary += (0.3 * self.emp_salary)

    def promotion(self, new_designation):
        self.designation = new_designation
        self.increament()

class Company:

    def __init__(self, name, employees):
        super().__init__()
        self.name = name
        self.employees = employees
    
    def display(self):
        print("Comapny Name:", self.name)
        print("Employee count:", len(self.employees))

    def show_employees(self):
        for emp in self.employees:
            emp.display()
    
    def promote_all(self):
        for emp in self.employees:
            emp.promotion('Sr. ' + emp.designation)


emp1 = Employee(1, 'ABC', 10000, 'Trainee')
emp2 = Employee(2, 'XYZ', 20000, 'Developer')
emp3 = Employee(3, 'PQR', 30000, 'Manager')
    
# emp1.display()
# emp2.display()
# emp3.display()

# emp1.promotion('Intern')
# emp1.display()

emps = [emp1, emp2, emp3]
com1 = Company('LMN', emps)

com1.display()
com1.show_employees()
com1.promote_all()
com1.show_employees()