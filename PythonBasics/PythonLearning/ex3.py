# Exercise 3
print("Enter operator (+, -, *, /): ", end="")
op = input()
print("Enter left operand (integer): ", end="")
n1 = int(input())
print("Enter right operand (integer): ", end="")
n2 = int(input())

print(n1, op, n2, "= ", end="")
if n1 == 45 and n2 == 3 and op == '*':
    print(555)
elif n1 == 56 and n2 == 9 and op == '+':
    print(77)
elif n1 == 56 and n2 == 4 and op == '/':
    print(4)
else:
    if op == '+':
        print(n1 + n2)
    elif op == '-':
        print(n1 - n2)
    elif op == '*':
        print(n1 * n2)
    elif op == '/':
        print(n1 / n2)
    else:
        print("wrong input")