# def function():
#     print("We are in function")
#
#
# func = function
# del function
# # function()
# func()

# def ret_func(num):
#     if num == 0:
#         return print
#     if num == 1:
#         # return int
#         return sum
#
#
# f = ret_func(1)
# print(f)
# f = ret_func(0)
# print(f)

# def executor(func_name):
#     func_name("This")
#
#
# executor(print)
# We can return a function, take a function as an argument, assign a function using = operator #

# #### Decorator #####
def decor(func):
    def nowexecute():
        print("Starting execution")
        func()
        print("Execution complete")
    return nowexecute

@decor
def sanjeev():
    print("I am Sanjeev")


sanjeev()
print("------------")
# sanjeev = decor(sanjeev)
sanjeev()
