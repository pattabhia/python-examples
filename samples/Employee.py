class Employee:
    employeeCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employeeCount += 1

    def displayCount(self):
        print("Total Employees %d" % Employee.employeeCount)

    def displayEmployee(self):
        print("name = ", self.name, ", salary =", self.salary)


employee1 = Employee("Ram", 1000)
employee2 = Employee("Rahim", 2000)
