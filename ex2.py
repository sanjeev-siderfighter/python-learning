# Exercise 2
print("Enter your age: ", end="")
age = int(input())
print("Your age is ", age)
if age > 18:
    print("You can drive")
elif age == 18:
    print("Can't Decide")
else:
    print("You can't drive")