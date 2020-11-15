class Student:
    pass


harry = Student()
larry = Student()

harry.name = "Harry"
harry.std = 12
harry.section = 'A'

larry.name = "Larry"
larry.salary = 9
larry.mentees = ["Fresher", "SDE-1"]

print(harry, '\n', larry)

print(harry.name, harry.std, harry.section)
# print(larry.name, larry.section)
print(larry.name, larry.salary, larry.mentees)