list1 = [3, 5, 2, 1, 4]
print(list1)
# -------------MAP-----------#
print("**************** MAP ***************")
list1_squared = list(map(lambda x: x ** 2, list1))
print(list1_squared)


def cube(x):
    return x ** 3


list1_cubed = list(map(cube, list1))
print(list1_cubed)

# -------------FILTER-----------#
print("**************** FILTER ***************")
list1_greater_3 = list(filter(lambda x: x > 3, list1))
print(list1_greater_3)

# -------------REDUCE-----------#
print("**************** REDUCE ***************")
from functools import reduce
list1_sum = reduce(lambda x, y: x + y, list1)
print(list1_sum)
list1_prod = reduce(lambda x, y: x * y, list1)
print(list1_prod)

# -------------LIST1 REMAINS UNCHANGED-----------#
print("**************** LIST1 REMAINS UNCHANGED ***************")
print(list1)
