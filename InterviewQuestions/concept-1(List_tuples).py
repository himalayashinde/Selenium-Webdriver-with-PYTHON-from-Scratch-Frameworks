# Lists are mutuable and Tuples are immutable

print("\nList Concept \n")
my_list= [1,2,3]

my_list[0]= 100
my_list.append(200)
my_list.pop(1)
print(my_list)

print("\n Tuple Concept \n")

my_tuple = (4, 5, 6)

try:
    my_tuple[0] = 100
except TypeError as e:
    print("Error occurred:", e)

print("Tuple after attempted modification:", my_tuple)

print("\nData types in python \n")

x=1
y=3.14
z= "hello"
dictionary ={"a": 1}
a = True

print(type(x))
print(type(y))
print(type(z))
print(type(dictionary))
print(type(a))
