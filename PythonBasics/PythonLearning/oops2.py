class Employee:
    leaves = 8
    pass


harry = Employee()
larry = Employee()

harry.name = "Harry"
harry.salary = 9
harry.role = "SDE-2"

larry.name = "Larry"
larry.salary = 12
larry.role = "Fresher"

print(larry.leaves)
print(harry.leaves)
print(Employee.leaves)

print(harry.__dict__)
print(larry.__dict__)
print(Employee.__dict__)

harry.leaves = 9
print(harry.__dict__)
print(larry.__dict__)
print(Employee.__dict__)

Employee.leaves = 10

print(harry.__dict__)
print(larry.__dict__)
print(Employee.__dict__)

print(harry.leaves)
print(larry.leaves)
print(Employee.leaves)

