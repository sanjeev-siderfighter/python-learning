class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property # getter
    def email(self):
        if self.fname is None or self.lname is None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter # setter
    def email(self, arg):
        print("setting your email now...")
        names = arg.split('@')[0]
        lst = names.split('.')
        self.fname = lst[0]
        self.lname = lst[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


sanjeev = Employee("Sanjeev", "Kumar")

print(sanjeev.email)

sanjeev.fname = "Sider"
print(sanjeev.email)

sanjeev.email = "sanjeev.siderfighter@gmail.com"
print(sanjeev.fname, sanjeev.lname, sanjeev.email)

del sanjeev.email
print(sanjeev.fname, sanjeev.lname, sanjeev.email)

sanjeev.email = "Sider.Fighter@gmail.com"
print(sanjeev.fname, sanjeev.lname, sanjeev.email)

