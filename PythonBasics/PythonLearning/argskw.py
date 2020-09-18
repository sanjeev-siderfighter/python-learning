def func(*args, **kwargs):
    print(args, " ", kwargs)
    for arg in args:
        print(arg)

    print()

    for key, value in kwargs.items():
        print(f"{key}, is {value}")


mylist = ["Hello", "Sup"]
mydict = {"sanjeev": "first name", "kumar": "last name"}
# func("Hello", 5, {25: 24}, {"sanjeev": 24, "kumar": 24})
func(*mylist, **mydict)


# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)
#
#
# def funargs(normal, *argsrohan, **kwargsbala):
#     print(argsrohan)
#     print(kwargsbala)
#     print(normal)
#     for item in argsrohan:
#         print(item)
#     print("\nNow I would Like to introduce some of our heroes")
#     for key, value in kwargsbala.items():
#         print(f"{key} is a {value}")
#
#
# # function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")
#
# har = ["Harry", "Rohan", "Skillf", "Hammad",
#        "Shivam", "The programmer"]
# normal = "I am a normal Argument and the students are:"
# kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor",
#       "The Programmer": "Coordinator", "Shivam": "Cook"}
# funargs(normal, *har, **kw)


