data=[
    {"name": "Alice", "Age": 30},
    {"name": "Bob", "Age": 23},
    {"name": "Charlie", "Age": 27},
    {"name": "Diana", "Age": 22},
    {"name": "Ethan", "Age": 35},
    {"name": "Fiona", "Age": 29},
    {"name": "George", "Age": 40},
    {"name": "Hannah", "Age": 24},
    {"name": "Ian", "Age": 31},
    {"name": "Jasmine", "Age": 26}
]

print(data[3]["name"])
# dictionary={"name":"Bob", "Age": 23}

def add(x,y):
    print(f"Additon = {x+y}")

add(2,3)

summation = lambda x,y : x + y
print(f"Summation = {summation(4,6)}")

numbers= [1,2,3,4,5]

print(numbers[::-1])
squared_numbers = list(map(lambda x: x*x,numbers))
print(squared_numbers)

even_numbers= list(filter(lambda x: x%2 == 0, squared_numbers))

print(even_numbers)

num = [42, 7, 89, 23, 65, 38, 91, 12, 56, 74]
sorted_list = sorted(num)
print(sorted_list)



print("##################################################")
# ChatGpt response

# lambda_map_filter_reference.py

# -------------------------------
# 📌 What is lambda in Python?
# -------------------------------
# A lambda function is a small anonymous function.
# Syntax: lambda arguments: expression

# ✅ Example 1: Simple lambda
square = lambda x: x ** 2
print("Square of 5:", square(5))  # Output: 25

# Equivalent to:
def square_def(x):
    return x ** 2

print("Square of 5 using def:", square_def(5))


# -------------------------------
# 📌 Using lambda with map()
# -------------------------------
# map(function, iterable) → applies function to every element in iterable

nums = [1, 2, 3, 4]
squared_nums = list(map(lambda x: x ** 2, nums))
print("\nUsing map() with lambda - Squares:", squared_nums)
# Output: [1, 4, 9, 16]


# -------------------------------
# 📌 Using lambda with filter()
# -------------------------------
# filter(function, iterable) → filters elements where function returns True

nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print("Using filter() with lambda - Even numbers:", even_nums)
# Output: [2, 4, 6]


# -------------------------------
# 📌 Combining filter() and map()
# -------------------------------
# First filters even numbers, then squares them

result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums)))
print("Filter even → square result:", result)
# Output: [4, 16, 36]


# -------------------------------
# 📌 Bonus: Without lambda (for comparison)
# -------------------------------

def is_even(x):
    return x % 2 == 0

def square(x):
    return x ** 2

even_nums_def = list(filter(is_even, nums))
squares_def = list(map(square, even_nums_def))
print("Using def - Even then square:", squares_def)


# -------------------------------
# ✅ Summary
# -------------------------------
print("""
Summary:

- lambda x: x ** 2         → Anonymous function to square a number
- map(lambda, list)        → Apply function to each element
- filter(lambda, list)     → Keep elements that return True

Example:
nums = [1, 2, 3, 4]
map → [1, 4, 9, 16]
filter (even) → [2, 4]
map + filter (square even) → [4, 16]
""")
