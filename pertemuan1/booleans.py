# Boolean dari perbandingan
print(10 >= 5)    
print(7 != 7)     
print(3 == 3)     

# Evaluasi nilai dan variabel
# True
print(bool("Python"))
print(bool(1))
print(bool([1, 2, 3]))  

# False
print(bool(""))
print(bool(0))
print(bool([]))       

# Function mengembalikan boolean
def is_lulus(nilai):
    return nilai >= 70

print(is_lulus(80))  
print(is_lulus(60)) 