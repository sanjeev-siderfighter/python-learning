class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def get_details(self):
        return f"Name is {self.name} and salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    def __mod__(self, other):
        return self.salary % other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"({self.name}, {self.salary}, {self.role})"

    # def __str__(self):
    #     return f"('{self.name}', {self.salary}, '{self.role}')"


emp1 = Employee("Sanjeev", 120, "Android")
emp2 = Employee("Shivansh", 116, "Android Kotlin")

print(emp1 % emp2, " ", emp1 == emp2, " ", emp1 / emp2)
print(emp2)
print(repr(emp1))
print(str(emp1))
