# string
print("ini contoh string")

# masukin string ke variabel
nama = "belajar python"

# tanda kutip di dalam string
print('dia bilang "python itu gampang"')

# string banyak baris
print("""halo dunia
lagi belajar python
biar makin jago""")

# string itu kayak array
kata = "Coding"
print(kata[0])   
# looping string
for huruf in kata:
    print("jalan")

# panjang string
print(len(kata))

# slicing
print(kata[1:4])   # ambil sebagian
print(kata[:3])    # dari awal
print(kata[2:])    # sampe akhir
print(kata[-2:-1]) # dari belakang

# ubah string
print(kata.upper())   # jadi gede semua
print(kata.lower())   # jadi kecil semua
print(kata.strip())   # hapus spasi kalo ada

# ganti isi string
print(nama.replace("python", "coding"))

# mecah string
print(nama.split(" "))

# gabung string
print(kata + " " + nama)
