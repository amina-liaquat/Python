tuple1 = (1, 2, 3, 4, 5, 6, 7)
tuple2 = ("Red", "Green", "Yellow")

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

details = ("Abhijeet", 8, "Buddy", 1234)
print("Details:", details)

country = ("Pakistan", "India", "Italy", "Dubai")

print("Positive Indexing:", country[1])
print("Negative Indexing:", country[-3])

if "Pakistan" in country:
    print("Pakistan is present.")
else:
    print("Pakistan is not present.")

country2 = ("Spain", "Italy", "India", "England", "Germany")

if "Russia" in country2:
    print("Russia is present.")
else:
    print("Russia is absent.")

animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")

print(animals[3:7])
print(animals[-7:-2])

print(animals[4:])
print(animals[-4:])

print(animals[:6])
print(animals[:-3])

print(animals[::2])
print(animals[-8:-1:2])

print(animals[1:8:3])

