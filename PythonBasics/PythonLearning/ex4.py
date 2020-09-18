# print the pattern
# *
# **
# ***
# ****

n = input("Enter the no. of rows: ")
sequence = input("Enter 1 for backwards and 0 for forward: ")


def print_stars(rows, seq):
    if not seq:
        for i in range(rows, 0, -1):
            for j in range(0, i):
                print("*", end=" ")
            print()
    else:
        for i in range(0, rows + 1):
            for j in range(0, i):
                print("*", end=" ")
            print()


try:
    n = int(n)
    if int(sequence) != 0 and int(sequence) != 1:
        raise Exception("should have entered number as suggested")
    sequence = bool(int(sequence))
    print_stars(n, sequence)
except Exception as e:
    print(e)
    print("please enter as suggested")
print("program finished")
