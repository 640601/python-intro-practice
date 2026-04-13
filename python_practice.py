# ======================================
# TASK 1: VARIABLE DECLARATION AND DATA TYPES
# ======================================

print("\n" + "="*40)
print("TASK 1: VARIABLE DECLARATION")
print("="*40)

age = 25
height = 5.9
name = "Elizabeth"
is_student = True

print(age, type(age))
print(height, type(height))
print(name, type(name))
print(is_student, type(is_student))


# ======================================
# TASK 2: STRING MANIPULATION
# ======================================

print("\n" + "="*40)
print("TASK 2: STRING MANIPULATION")
print("="*40)

text = "hello world"

print("Uppercase:", text.upper())
print("Capitalized:", text.capitalize())
print("Replace:", text.replace("world", "Python"))


# ======================================
# TASK 3: BASIC OPERATIONS
# ======================================

print("\n" + "="*40)
print("TASK 3: BASIC OPERATIONS")
print("="*40)

a = 10
b = 3

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
print("Equal:", a == b)
print("Not equal:", a != b)
print("Greater or equal:", a >= b)
print("Less or equal:", a <= b)

# Logical
print("AND:", a > 5 and b < 5)
print("OR:", a > 5 or b > 5)
print("NOT:", not(a > 5))


# ======================================
# TASK 4: DATA COLLECTIONS
# ======================================

print("\n" + "="*40)
print("TASK 4: DATA COLLECTIONS")
print("="*40)

# List
fruits = ["apple", "banana", "cherry"]
print("List item:", fruits[1])

# Tuple
numbers = (1, 2, 3)
print("Tuple item:", numbers[2])

# Dictionary
person = {"name": "Elizabeth", "age": 25}
print("Dictionary item:", person["name"])


# ======================================
# TASK 5: EXPRESSION COMBINATION
# ======================================

print("\n" + "="*40)
print("TASK 5: EXPRESSION COMBINATION")
print("="*40)

x = 5
y = 2
z = 3

result = (x + y) * z / y ** 2
print("Result:", result)


# ======================================
# TASK 6: LOOPS
# ======================================

print("\n" + "="*40)
print("TASK 6: LOOPS")
print("="*40)

# For loop
for i in range(1, 6):
    print("Number:", i)

# While loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1


# ======================================
# TASK 7: FUNCTIONS
# ======================================

print("\n" + "="*40)
print("TASK 7: FUNCTIONS")
print("="*40)

def greet(name):
    return f"Hello, {name}!"

print(greet("Elizabeth"))

def add_numbers(a, b):
    return a + b

print("Sum:", add_numbers(5, 3))
