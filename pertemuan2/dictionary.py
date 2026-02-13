# Create and Print a Dictionary
thisdict = {
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2015
}

print(thisdict)

# Access Dictionary Item by Key
thisdict = {
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2015
}

print(thisdict["brand"])

# Duplicate Keys Will Overwrite Existing Values
thisdict = {
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2015,
  "year": 2022
}

print(thisdict)

# Get the Length of a Dictionary
thisdict = {
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2015
}

print(len(thisdict))

# Dictionary With Different Data Types
thisdict = {
  "brand": "Toyota",
  "electric": True,
  "year": 2023,
  "colors": ["black", "silver", "gray"]
}

print(thisdict)

# Check Dictionary Data Type
thisdict = {
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2015
}

# Using the dict() Constructor
thisdict = dict(name="Alice", age=28, country="Canada")

print(thisdict)

# ===== ACCESS VALUE USING KEY =====
thisdict = {
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2015
}

x = thisdict["model"]
print("Access using []:", x)

# Using get() method
x = thisdict.get("model")
print("Access using get():", x)


#  GET KEYS
x = thisdict.keys()
print("Keys:", x)

# Keys view updates automatically
car = {
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2015
}

x = car.keys()
print("Before adding new key:", x)

car["color"] = "blue"

print("After adding new key:", x)


# GET VALUES 
x = thisdict.values()
print("Values:", x)

# Values view updates automatically (change value)
car = {
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2015
}

x = car.values()
print("Before change:", x)

car["year"] = 2024

print("After change:", x)

# Values view updates automatically (add new item)
car = {
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2015
}

x = car.values()
print("Before adding new item:", x)

car["color"] = "green"

print("After adding new item:", x)


#  GET ITEMS (KEY:VALUE PAIRS) 
x = thisdict.items()
print("Items:", x)

# Items view updates automatically (change value)
car = {
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2015
}

x = car.items()
print("Before change:", x)

car["year"] = 2024

print("After change:", x)

# Items view updates automatically (add new item)
car = {
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2015
}

x = car.items()
print("Before adding new item:", x)

car["color"] = "yellow"

print("After adding new item:", x)


#  CHECK IF KEY EXISTS 
thisdict = {
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2015
}

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#  CHANGE VALUE USING KEY 
thisdict = {
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2015
}

thisdict["year"] = 2019

print("After changing year:", thisdict)


# UPDATE DICTIONARY USING update() METHOD 
thisdict = {
  "brand": "Toyota",
  "model": "Corolla",
  "year": 2015
}

thisdict.update({"year": 2021})

print("After update() method:", thisdict)
