# Manuplating Tuples
countreis=("Pakistan","India","Saudia","Italy","Dubai")
temp=list(countreis)
temp.append("England")    # Add item
temp.pop(1)                # Remove item
temp[2]="Finland"           # Change Item
countreis=tuple(temp)
print(countreis)
# Concatenate Two Tuples
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)
    # Count()
    # Syntax      tuple.count(element)
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)
     # Inde()
     # tuple.index(element, start, end)
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)
