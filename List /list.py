# Python List 

# ---------------------------
# Creating Lists
# ---------------------------
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "apple", 3.5, False]
nested = [[1, 2], [3, 4]]

print("Created Lists:", empty_list, numbers, mixed, nested)

# ---------------------------
# Accessing Elements
# ---------------------------
fruits = ["apple", "banana", "cherry"]
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Sliced fruits:", fruits[0:2])

# ---------------------------
# List Operations
# ---------------------------
a = [1, 2, 3]
b = [4, 5]
print("Concatenation:", a + b)
print("Repetition:", a * 2)

# ---------------------------
# Modifying Lists
# ---------------------------
fruits[1] = "orange"
print("Modified fruits:", fruits)
fruits.append("mango")
fruits.insert(1, "grape")
print("After append & insert:", fruits)
fruits.remove("apple")
print("After remove:", fruits)
popped = fruits.pop()
print("Popped element:", popped)
print("After pop:", fruits)

# ---------------------------
# Useful Methods
# ---------------------------
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print("Sorted numbers:", numbers)
numbers.reverse()
print("Reversed numbers:", numbers)
print("Index of 7:", numbers.index(7))
print("Count of 5:", numbers.count(5))
numbers.clear()
print("Cleared list:", numbers)

# ---------------------------
# Copying Lists
# ---------------------------
a = [1, 2, 3]
b = a.copy()
b[0] = 99
print("Original list:", a)
print("Copied list:", b)

# ---------------------------
# List Comprehension
# ---------------------------
squares = [x**2 for x in range(5)]
print("Squares:", squares)
even = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", even)

# ---------------------------
# Nested Lists
# ---------------------------
matrix = [[1, 2], [3, 4], [5, 6]]
print("Element from nested list:", matrix[0][1])

# ---------------------------
# Built-in Functions
# ---------------------------
nums = [4, 1, 7, 3]
print("Length:", len(nums))
print("Min:", min(nums))
print("Max:", max(nums))
print("Sum:", sum(nums))

# ---------------------------
# Conversion to List
# ---------------------------
text = "hello"
print("Converted string:", list(text))
tuple_data = (1, 2, 3)
print("Converted tuple:", list(tuple_data))

# ---------------------------
# Membership Test
# ---------------------------
fruits = ["apple", "banana", "cherry"]
print("'apple' in fruits:", "apple" in fruits)
print("'grape' not in fruits:", "grape" not in fruits)

# ---------------------------
# Iterating Over List
# ---------------------------
for fruit in fruits:
    print("Fruit:", fruit)

# ---------------------------


# ---------------------------
# Flatten Nested List
# ---------------------------
nested = [[1, 2], [3, 4]]
flat = [x for sublist in nested for x in sublist]
print("Flattened list:", flat)
