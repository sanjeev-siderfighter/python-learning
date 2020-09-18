# Health Management System

def getdate():
    import datetime
    return datetime.datetime.now()


def get_file_name(name, logtype):
    filename = ""
    if name == 1 and logtype == 1:
        filename = "FileWork/harry_food_log.txt"
    elif name == 1 and logtype == 2:
        filename = "FileWork/harry_workout_log.txt"
    elif name == 2 and logtype == 1:
        filename = "FileWork/rohan_food_log.txt"
    elif name == 2 and logtype == 2:
        filename = "FileWork/rohan_workout_log.txt"
    elif name == 3 and logtype == 1:
        filename = "FileWork/hammad_food_log.txt"
    elif name == 3 and logtype == 2:
        filename = "FileWork/hammad_workout_log.txt"

    return filename


def retrieve(name, logtype):
    filename = get_file_name(name, logtype)
    with open(filename) as file:
        print(file.read())


def log(name, logtype):
    filename = get_file_name(name, logtype)
    day = input("Enter what you did: ")
    with open(filename, "a") as file:
        file.write("[" + str(getdate()) + "]" + " " + day + "\n")
    print("Logged!!")


managementType = int(input("1 for log, 2 for retrieve: "))
person = int(input("1 for harry, 2 for rohan, 3 for hammad: "))
filetype = int(input("1 for food logs, 2 for workout logs: "))
if managementType == 1:
    log(person, filetype)
else:
    retrieve(person, filetype)
