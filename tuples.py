tuple1=(1,2,3,4,5,6,7)
tuple2=("Red","Green","Yellow")
print(tuple1)
print(tuple2)
details=("Abhijeet",8,"Buddy",1234)
print(details)
# Tuples indexes
country=("Pakistan","India","Italy","Dubai")
print(country[1])      # Positive indexing
print(country[-3])     # Negative Indexing 
  # Check for item
country=("Pakistan","India","Italy","Dubai")
if "Pakistan" in country:
    print("YES This IS Present" )
else:
    print("No This is not present")
    #!! !! !!! //// ///// !!!! !!!  !!
country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")
    # Range of index
     #!! !! !!! //// ///// !!!! !!!  !!
#  Syntax: Tuple[start : end : jumpIndex]
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes
           #!! !! !!! //// ///// !!!! !!!  !!
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[4:])      #using positive indexes
print(animals[-4:])     #using negative indexes
           #!! !! !!! //// ///// !!!! !!!  !!
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[:6])      #using positive indexes
print(animals[:-3])     #using negative indexes
           #!! !! !!! //// ///// !!!! !!!  !!
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes
           #!! !! !!! //// ///// !!!! !!!  !!
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])
