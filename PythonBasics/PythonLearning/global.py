myglobal = 5


def func():
    global myglobal
    myglobal = myglobal + 5
    print("func: ", myglobal)


func()
print("out", myglobal)