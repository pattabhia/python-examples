from Employee import Employee


class EmployeeClient(Employee):

    def __init__(self, o):
        print("calling employee client...")

    def displayEmployee(self):
        print("calling from client ...")


emp = Employee("ram", 10000)
emp.displayEmployee()
