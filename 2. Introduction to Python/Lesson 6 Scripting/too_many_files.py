import os

file_location = os.getcwd()


files = []
for i in range(10000):
    files.append(open(file_location + "\\"+"test.txt"))
    print(i)


