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

    @classmethod
    def alternative_constructor(cls, string, delim):
        # params = string.split(delim)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split(delim))

    @staticmethod
    def printstring(string):
        print("Your string was: " + string)


class Programmer (Employee):

    def __init__(self, name, salary, role, languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages

    def printprog(self):
        return f"Name of the programmer is {self.name} and salary is {self.salary} and role is {self.role}. The languages are {self.languages}"


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
sanjeev = Programmer("Sanjeev", 555, "Programmer", ["C", "C++", "Java", "Python"])
print(sanjeev.printprog())
