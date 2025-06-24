file = open('test.txt')
#Read all contents of the file
# print(file.read())

# Read few characters of the file by passing character
# print(file.read(3))

# Reads file line by line
# print(file.readline())
# print(file.readline())
# print(file.readline())

# Print line by line using readLine method
# line = file.readline()

# while line!="":
#     if line!="":
#         print(line)
#         line =file.readline()

# for line in file:
#         print(line.strip())

# for line in file:
#     if line!="":
#         print(line)
#         line =file.readline()


# print(lines)

# print(file.readlines())

for lines in file.readlines():
    print(lines)

file.close
