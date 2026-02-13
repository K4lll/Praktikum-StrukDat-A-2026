nilai = [75, 80, 65, 90, 85]

nilai.append(95)
print(nilai)

nilai_terkecil = min(nilai)


nilai.remove(nilai_terkecil)
print(nilai)

nilai.sort()
print(nilai)

nilai_tertinggi = max(nilai)
print(nilai_tertinggi)

print(nilai_terkecil)

print (sum(nilai)/len(nilai))
print()


#Nomor 2

dosen = ("D001", "Dr. Andi", "Struktur Data", 12)
print (dosen[1:3])
for x in dosen:
  print(x)

y = list(dosen)
y[3] = 14
dosen = tuple(y)
print(dosen)#mengubah menjad list dan mengubah data di dalam lalu di ubah menjadi tuple kembali
print("lebih cepat dan efisien")

#Nomor 3
keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}

#Nomor 4
mahasiswa = {
"M001": {"nama": "Rina", "prodi": "Informatika", "ipk":
3.60},
"M002": {"nama": "Doni", "prodi": "Sistem Informasi",
"ipk": 3.25},
"M003": {"nama": "Lina", "prodi": "Informatika", "ipk":
3.80}
}

