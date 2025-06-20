values=[1, 2, "Hello world", 4 ,5]

print(values[0])
print(values[1])
print(values[2])
print(values[3])
print(values[4])

print("\nReverse String\n")

print(values[-1])
print(values[-2])
print(values[-3])
print(values[-4])
print(values[-5])

print("\nSlice the List\n")

print(values[0:3])

print(values[0:-1])

#Insert

values.insert(3,"Himalaya Shinde")
print(values)

#Appending
values.append("End")
print(values)

#Updating
values[2]= "Hello There"
print(values)

#Deleting
del values[0]
print(values)

