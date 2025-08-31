# Python List - Complete Guide with All Methods

# ---------------------------
# Creating Lists
# ---------------------------
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# ---------------------------
# append()
# ---------------------------
fruits.append("mango")
print("After append:", fruits)

# ---------------------------
# extend()
# ---------------------------
fruits.extend(["grape", "orange"])
print("After extend:", fruits)

# ---------------------------
# insert()
# ---------------------------
fruits.insert(1, "kiwi")
print("After insert at index 1:", fruits)

# ---------------------------
# remove()
# ---------------------------
fruits.remove("banana")
print("After remove 'banana':", fruits)

# ---------------------------
# pop()
# ---------------------------
popped = fruits.pop()  # removes last element
print("Popped element:", popped)
print("After pop:", fruits)

popped_at_index = fruits.pop(2)  # removes element at index 2
print("Popped at index 2:", popped_at_index)
print("After pop(2):", fruits)

# ---------------------------
# clear()
# ---------------------------
copy_list = fruits.copy()
copy_list.clear()
print("After clear:", copy_list)

# ---------------------------
# index()
# ---------------------------
numbers = [10, 20, 30, 20, 40, 50]
print("Index of 20:", numbers.index(20))
print("Index of 20 (search from index 2):", numbers.index(20, 2))

# ---------------------------
# count()
# ---------------------------
print("Count of 20:", numbers.count(20))

# ---------------------------
# sort()
# ---------------------------
nums = [5, 2, 9, 1, 7]
nums.sort()
print("Sorted ascending:", nums)

nums.sort(reverse=True)
print("Sorted descending:", nums)

# sort with key
words = ["banana", "apple", "cherry", "date"]
words.sort(key=len)
print("Sorted by length:", words)

# ---------------------------
# reverse()
# ---------------------------
words.reverse()
print("Reversed list:", words)

# ---------------------------
# copy()
# ---------------------------
original = [1, 2, 3]
copied = original.copy()
copied.append(4)
print("Original:", original)
print("Copied:", copied)

# ---------------------------
# Membership (in / not in)
# ---------------------------
print("'apple' in fruits:", "apple" in fruits)
print("'melon' not in fruits:", "melon" not in fruits)

# ---------------------------
# Iterating
# ---------------------------
for fruit in fruits:
    print("Fruit:", fruit)

# ---------------------------
# List Comprehension
# ---------------------------
squares = [x**2 for x in range(6)]
print("Squares:", squares)

# ---------------------------
# Nested Lists & Flatten
# ---------------------------
nested = [[1, 2], [3, 4], [5, 6]]
flat = [x for sublist in nested for x in sublist]
print("Flattened:", flat)
