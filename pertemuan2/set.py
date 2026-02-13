# Create a Set
myset = {"car", "bike", "bus"}
print(myset)

# Duplicate Values Will Be Ignored
thisset = {"car", "bike", "bus", "car"}
print(thisset)

# True and 1 Are Considered the Same Value
thisset = {"car", "bike", "bus", True, 1, 3}
print(thisset)

# False and 0 Are Considered the Same Value
thisset = {"car", "bike", "bus", False, True, 0}
print(thisset)

# Get the Length of a Set
thisset = {"car", "bike", "bus"}
print(len(thisset))

# Set With String Data Type
set1 = {"red", "green", "blue"}
print(set1)

# Set With Integer Data Type
set2 = {10, 20, 30, 40, 50}
print(set2)

# Set With Boolean Data Type
set3 = {True, False, True}
print(set3)

# Set With Mixed Data Types
set1 = {"xyz", 99, False, 100, "female"}
print(set1)

# Check Set Data Type
myset = {"car", "bike", "bus"}
print(type(myset))

# Using the set() Constructor
thisset = set(("car", "bike", "bus"))
print(thisset)

# Loop Through a Set
thisset = {"car", "bike", "bus"}

for x in thisset:
    print(x)

# Check if an Item Exists in a Set
thisset = {"car", "bike", "bus"}

print("bike" in thisset)

# Check if an Item Does NOT Exist in a Set
thisset = {"car", "bike", "bus"}

print("bike" not in thisset)

# Add One Item to a Set Using add()
thisset = {"car", "bike", "bus"}

thisset.add("train")

print(thisset)

# Add Items from Another Set Using update()
thisset = {"car", "bike", "bus"}
tropical = {"plane", "boat", "truck"}

thisset.update(tropical)

print(thisset)

# Add Items from a List Using update()
thisset = {"car", "bike", "bus"}
mylist = ["scooter", "taxi"]

thisset.update(mylist)

print(thisset)

# Remove an Item Using remove()
thisset = {"car", "bike", "bus"}

thisset.remove("bike")

print(thisset)

# Remove an Item Using discard()
thisset = {"car", "bike", "bus"}

thisset.discard("bike")

print(thisset)

# Remove a Random Item Using pop()
thisset = {"car", "bike", "bus"}

x = thisset.pop()

print("Removed item:", x)
print("Remaining set:", thisset)

# Clear All Items from a Set
thisset = {"car", "bike", "bus"}

thisset.clear()

print(thisset)

# Delete the Entire Set Using del
thisset = {"car", "bike", "bus"}

del thisset

print(thisset)

#Loop Item
thisset = {"car", "bike", "bus"}

for x in thisset:
  print(x)

# ===== UNION =====
set1 = {"x", "y", "z"}
set2 = {4, 5, 6}

# Using union()
set3 = set1.union(set2)
print("Union using union():", set3)

# Using | operator
set3 = set1 | set2
print("Union using | :", set3)

# Join Multiple Sets
set3 = {"Ali", "Siti"}
set4 = {"orange", "grape", "melon"}

myset = set1.union(set2, set3, set4)
print("Union multiple (method):", myset)

myset = set1 | set2 | set3 | set4
print("Union multiple (|):", myset)

# Join Set and Tuple (only works with union method)
x = {"x", "y", "z"}
y = (7, 8, 9)

z = x.union(y)
print("Union set + tuple:", z)


# ===== UPDATE =====
set1 = {"x", "y", "z"}
set2 = {4, 5, 6}

set1.update(set2)
print("Update result:", set1)


# ===== INTERSECTION (Keep ONLY duplicates) =====
set1 = {"red", "green", "blue"}
set2 = {"black", "white", "red"}

# Using intersection()
set3 = set1.intersection(set2)
print("Intersection method:", set3)

# Using & operator
set3 = set1 & set2
print("Intersection using &:", set3)

# intersection_update() (modifies original set)
set1 = {"red", "green", "blue"}
set2 = {"black", "white", "red"}

set1.intersection_update(set2)
print("Intersection update:", set1)

# True/False and 1/0 duplicate example
set1 = {"red", 1, "green", 0, "blue"}
set2 = {False, "black", 1, "red", 2, True}

set3 = set1.intersection(set2)
print("Intersection with boolean duplicates:", set3)


#  DIFFERENCE
set1 = {"red", "green", "blue"}
set2 = {"black", "white", "red"}

# Using difference()
set3 = set1.difference(set2)
print("Difference method:", set3)

# Using - operator
set3 = set1 - set2
print("Difference using - :", set3)

# difference_update() (modifies original set)
set1 = {"red", "green", "blue"}
set2 = {"black", "white", "red"}

set1.difference_update(set2)
print("Difference update:", set1)


# SYMMETRIC DIFFERENCE 
set1 = {"red", "green", "blue"}
set2 = {"black", "white", "red"}

# Using symmetric_difference()
set3 = set1.symmetric_difference(set2)
print("Symmetric difference method:", set3)

# Using ^ operator
set3 = set1 ^ set2
print("Symmetric difference using ^ :", set3)

# symmetric_difference_update() (modifies original set)
set1 = {"red", "green", "blue"}
set2 = {"black", "white", "red"}

set1.symmetric_difference_update(set2)
print("Symmetric difference update:", set1)

#Frozen Set
x = frozenset({"car", "bike", "bus"})
print(x)
print(type(x))
