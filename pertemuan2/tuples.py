# Menghitung Panjang Tuple
thistuple = ("car", "bike", "bus")
print(len(thistuple))

# Tuple Allows Duplicate Values
thistuple = ("car", "bike", "bus", "car", "bus")
print(thistuple)

# Get Tuple Length
thistuple = ("car", "bike", "bus")
print(len(thistuple))

# Create a Tuple With One Item (Comma Required)
thistuple = ("car",)
print(type(thistuple))

# NOT a Tuple
thistuple = ("car")
print(type(thistuple))

# Tuple With Different Data Types
tuple1 = ("red", "green", "blue")
tuple2 = (10, 20, 30, 40, 50)
tuple3 = (True, False, True)

print(tuple1)
print(tuple2)
print(tuple3)

# Tuple With Mixed Data Types
tuple1 = ("xyz", 99, False, 100, "female")
print(tuple1)

# Check Tuple Data Type
mytuple = ("car", "bike", "bus")
print(type(mytuple))

# Using the tuple() Constructor
thistuple = tuple(("car", "bike", "bus"))
print(thistuple)

# Access Tuple Items
thistuple = ("car", "bike", "bus")
print(thistuple[1])

# Negative Indexing
thistuple = ("car", "bike", "bus")
print(thistuple[-1])

# Range of Indexes
thistuple = ("car", "bike", "bus", "train", "plane", "boat", "truck")
print(thistuple[2:5])

# Range Without Start Index
thistuple = ("car", "bike", "bus", "train", "plane", "boat", "truck")
print(thistuple[:4])

# Range Without End Index
thistuple = ("car", "bike", "bus", "train", "plane", "boat", "truck")
print(thistuple[2:])

# Range of Negative Indexes
thistuple = ("car", "bike", "bus", "train", "plane", "boat", "truck")
print(thistuple[-4:-1])

# Check if Item Exists
thistuple = ("car", "bike", "bus")
if "car" in thistuple:
    print("Yes, 'car' is in the tuple")

# Change Tuple Values (Using List Conversion)
x = ("car", "bike", "bus")
y = list(x)
y[1] = "scooter"
x = tuple(y)

print(x)

# Add Items (Convert to List and Append)
thistuple = ("car", "bike", "bus")
y = list(thistuple)
y.append("train")
thistuple = tuple(y)

print(thistuple)

# Add Tuple to a Tuple
thistuple = ("car", "bike", "bus")
y = ("plane",)
thistuple += y

print(thistuple)

# Remove Items (Using List Conversion)
thistuple = ("car", "bike", "bus")
y = list(thistuple)
y.remove("car")
thistuple = tuple(y)

print(thistuple)

# Delete the Entire Tuple
thistuple = ("car", "bike", "bus")
del thistuple
print(thistuple)
