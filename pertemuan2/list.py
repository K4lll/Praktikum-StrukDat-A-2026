#List
thislist = ["car", "bike", "bus"]
print(thislist)

#Duplicates
thislist = ["car", "bike", "bus", "car", "bus"]
print(thislist)

#Negative Index
thislist = ["car", "bike", "bus"]
print(thislist[-1])

#Range of Indexes
thislist = ["car", "bike", "bus", "train", "plane", "boat", "truck"]
print(thislist[2:5])

#Change Item Value
thislist = ["car", "bike", "bus"]
thislist[1] = "scooter"
print(thislist)

#Change a Range of Item Values
thislist = ["car", "bike", "bus", "train", "plane", "truck"]
thislist[1:3] = ["scooter", "van"]
print(thislist)

#Insert Item
thislist = ["car", "bike", "bus"]
thislist.insert(2, "taxi")
print(thislist)

#Append Items
thislist = ["car", "bike", "bus"]
thislist.append("tram")
print(thislist)

#Extend List
thislist = ["car", "bike", "bus"]
tropical = ["subway", "helicopter", "jet"]
thislist.extend(tropical)
print(thislist)

#Remove Specified Item
thislist = ["car", "bike", "bus"]
thislist.remove("bike")
print(thislist)

#Clear the List 
thislist = ["car", "bike", "bus"]
thislist.clear()
print(thislist)

#Loop Through a List
thislist = ["car", "bike", "bus"]
for x in thislist:
  print(x)

#Loop Through the Index Numbers
thislist = ["car", "bike", "bus"]
for i in range(len(thislist)):
  print(thislist[i])

#Using a While Loop
thislist = ["car", "bike", "bus"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Looping Using List Comprehension
thislist = ["car", "bike", "bus"]
[print(x) for x in thislist]

#Contoh Tanpa List Comprehension
fruits = ["grape", "melon", "berry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "e" in x:
        newlist.append(x)

print(newlist)

#Contoh Dengan List Comprehension (1 Baris)
fruits = ["grape", "melon", "berry", "kiwi", "mango"]

newlist = [x for x in fruits if "e" in x]

print(newlist)

#Syntax Umum List Comprehension\
newlist = [expression for item in iterable if condition == True]

#Sort List Secara Alphabet (Ascending - Default)
thislist = ["zebra", "lion", "tiger", "elephant", "monkey"]

thislist.sort()

print(thislist)

#Sort List Secara Numerik (Ascending)
thislist = [45, 12, 89, 33, 7]

thislist.sort()

print(thislist)

#Sort List Secara Descending
thislist = ["zebra", "lion", "tiger", "elephant", "monkey"]

thislist.sort(reverse=True)

print(thislist)

#Menggunakan copy() Method
# thislist = ["car", "bike", "bus"]

mylist = thislist.copy()

print(mylist)

#Menggunakan list() Method
thislist = ["car", "bike", "bus"]

mylist = list(thislist)

print(mylist)

#Menggunakan Slice Operator [:]
thislist = ["car", "bike", "bus"]

mylist = thislist[:]

print(mylist)

#Menggunakan Operator +
list1 = ["x", "y", "z"]
list2 = [10, 20, 30]

list3 = list1 + list2

print(list3)

#Menggunakan Loop dan append()
list1 = ["x", "y", "z"]
list2 = [10, 20, 30]

for x in list2:
    list1.append(x)

print(list1)

#Menggunakan extend() Method
list1 = ["x", "y", "z"]
list2 = [10, 20, 30]

list1.extend(list2)

print(list1)
