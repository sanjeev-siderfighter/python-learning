items = [int, float, bool, "sanjeev", "ilias", 62, 3]
for item in items:
    if str(item).isnumeric() and int(item) > 6:
        print(item)

    if  str(item).isalnum():
        print("encountered alpha numeric")

    if str(item).isalpha():
        print("it's alphabets")
