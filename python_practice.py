# Task 1: Variable Declaration and Data Types

# Declaring variables
age = 25                # integer
height = 5.9            # float
name = "Elizabeth"      # string
is_student = True       # boolean

# Printing values and types
print("Task 1: Variable Types")
print(age, type(age))
print(height, type(height))
print(name, type(name))
print(is_student, type(is_student))


# Task 2: String Manipulation

text = "hello world"

print("\nTask 2: String Manipulation")
print(text.upper())        # Converts to uppercase
print(text.capitalize())  # Capitalizes first letter
print(text.replace("world", "Python"))  # Replaces word


# Task 3: Basic Operations

a = 10
b = 3

print("\nTask 3: Basic Operations")

# Arithmetic
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# Comparison
print("Greater than:", a > b)
print("Less than:", a < b)
print("Equal to:", a == b)
print("Not equal:", a != b)
print("Greater or equal:", a >= b)
print("Less or equal:", a <= b)

# Logical
print("Logical AND:", a > 5 and b < 5)
print("Logical OR:", a > 5 or b > 5)
print("Logical NOT:", not(a > 5))


# Task 4: Data Collections

# List
fruits = ["apple", "banana", "cherry"]
print("\nTask 4: List")
print(fruits)

# Tuple
numbers = (1, 2, 3)
print("Tuple:", numbers)

# Dictionary
person = {"name": "Elizabeth", "age": 25}
print("Dictionary:", person)


# Task 5: Conditional Statements

print("\nTask 5: Conditional Statements")

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# Task 6: Loops

print("\nTask 6: Loops")

# For loop
for fruit in fruits:
    print("Fruit:", fruit)

# While loop
count = 0
while count < 3:
    print("Count is:", count)
    count += 1


# Task 7: Functions

print("\nTask 7: Functions")

def greet(name):
    return f"Hello, {name}!"

print(greet("Elizabeth"))