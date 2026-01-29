# Variabel
nama = "Andi"      # string
umur = 19          # integer
tinggi = 170.5     # float

print(f"{nama} sekarang umur {umur} tahun")

# Casting
nilai = 75
print(nilai + 5, type(nilai))

nilai = str(nilai)   # casting int ke string
print(nilai, type(nilai))

# Penamaan variabel yang bener
"""
nilaiUjian = 90
nilai_ujian = 85
_NilaiUjian = 80
NILAIUJIAN = 75
nilaiujian1 = 70
"""

# Penamaan variabel yang salah
"""
1nilai = 10          (nggak boleh diawali angka)
nilai-ujian = 80     (nggak boleh pake tanda minus)
nilai ujian = 90     (nggak boleh ada spasi)
"""

# Jenis penamaan variabel
"""
Camel Case   : nilaiUjianAkhir
Pascal Case  : NilaiUjianAkhir
Snake Case   : nilai_ujian_akhir
"""

# Assign banyak variabel sekaligus (beda nilai)
matematika, fisika, kimia = 88, 90, 85
print(f"Nilai matematika {matematika}")
print(f"Nilai fisika {fisika}")
print(f"Nilai kimia {kimia}")

# Assign banyak variabel satu nilai
izin = sakit = alpha = "tidak masuk"
print("izin:", izin)
print("sakit:", sakit)
print("alpha:", alpha)