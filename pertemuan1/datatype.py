# String (str)
x = "Pemrograman Python"
x = str("Pemrograman Python")
print(type(x))

# Integer (int)
x = 100
x = int(100)
print(type(x))

# Float
x = 99.9
x = float(99.9)
print(type(x))

# Complex
x = 2 + 5j
x = complex(2, 5)
print(type(x))

# List
x = ["Merah", "Kuning", "Hijau"]
x = list(("Merah", "Kuning", "Hijau"))
print(type(x))

# Tuple
x = ("Senin", "Selasa", "Rabu")
x = tuple(("Senin", "Selasa", "Rabu"))
print(type(x))

# Range
x = range(1, 10)
print(type(x))

# Dict
x = {"merk": "Samsung", "harga": 3000000}
x = dict(merk="Samsung", harga=3000000)
print(type(x))

# Set
x = {"Nasi Goreng", "Mie Ayam", "Sate"}
x = set(("Nasi Goreng", "Mie Ayam", "Sate"))
print(type(x))

# Frozenset
x = frozenset({"Tenang", "Santai", "Fokus"})
print(type(x))

# Boolean (bool)
x = False
x = bool(0)
print(type(x))

# Bytes
x = b"Hello"
x = bytes(4)
print(type(x))

# Bytearray
x = bytearray(6)
print(type(x))

# Memoryview
x = memoryview(bytes(6))
print(type(x))

# NoneType
x = None
print(type(x))