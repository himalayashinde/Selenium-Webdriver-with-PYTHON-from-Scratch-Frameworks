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

#Tuples are immutable, meaning they cannot be changed after creation.
# They are defined using parentheses instead of square brackets.
# Tuples can hold a mix of data types, similar to lists.
# They are often used to group related data together, and can be unpacked into variables.
# Tuples are defined using parentheses
# and can contain elements of different data types, including other tuples.
# Tuples are useful for fixed collections of items that should not change.

#Below are the examples of Tuples
values_tuple = (1, 2, "Hello world", 4, 5)
print(values_tuple[0])

values_tuple[2]= "hello worlds"
print(values_tuple)

# Traceback (most recent call last):
#   File "I:\Coding_journey\Selenium-Webdriver-with-PYTHON-from-Scratch-Frameworks\DataType.py", line 52, in <module>
#     values_tuple[2]= "hello worlds"
#     ~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment


