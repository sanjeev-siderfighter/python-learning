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


harry = Employee("Harry", 9, "SDE-1")
print(harry.no_of_leaves, Employee.no_of_leaves)
# harry.no_of_leaves = 5
# harry.no_of_leaves = 5 will create if not exists the instance variable
Employee.no_of_leaves = 9
print(harry.no_of_leaves, Employee.no_of_leaves)
harry.change_leaves(12)
print(harry.no_of_leaves, Employee.no_of_leaves)
# harry.no_of_leaves will first look for instance variable, if not present, then it will look for class variable
# if not present but accessed then error

rohan = Employee("Rohan", 12, "SDE-2")
print(rohan.no_of_leaves)
rohan.change_leaves(20)
print(harry.no_of_leaves, Employee.no_of_leaves, rohan.no_of_leaves)
