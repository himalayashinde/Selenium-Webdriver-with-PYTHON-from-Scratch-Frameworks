str = "RahulShettyAcademy.com"
str1 = "consulting firm"
str3 = "RahulShetty"
str4 = " great "

print(str[1])   # character at specific index from a string

print(str[0:5]) # Substring in python

print(str+" "+str1) # Concatenation

print( str3 in str) # Substring Validation

var = str.split(".")  # Splitting a string

print(var)
print(var[0])
print(var[1])

print("\nBelow is the example for trim\n")

print("Original String :",str4)
print("\nRemove All white spaces from the string", str4.strip())
print("\nRemove Beginning white spaces from the string", str4.lstrip())
print("\nRemove Ending white spaces from  the string", str4.rstrip())
 