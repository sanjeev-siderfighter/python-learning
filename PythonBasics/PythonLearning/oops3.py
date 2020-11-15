class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def get_details(self):
        return f"Name is {self.name} and salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 9, "SDE-1")

print(harry.get_details())
