"""
myFile = open("exp_file.txt", "r+")
print(myFile.read())
n = myFile.write("\n\nThanks and Regards")
print(n)
myFile.close()
"""


"""
"r"=open file for reading(default)
"w"=open file for writing
"x"= create file if not exist
"a"= add more content to a file
"b"= binary mode
"r+"= read and write mode (read and append mode)
't'= text mode.(default)
"""

"""
file = open("exp_file.txt", "rt")
# jack = file.read()
# print(len(jack))

# for x in jack:
#     print(x)

# for x in file:
#     print(x, end="")

# print(file.readline())
# print(file.readline())
lineList = file.readlines()
print(lineList)

file.close()
"""

# file = open("exp_file.txt", "rt")
#
# content = file.read(10)
# print(content)
#
# content = file.read(20)
# print(content)
#
# file.close()

