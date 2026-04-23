# Lists
'''
- Can contain multiple values
- Ordered and changeable
- Use [] to define a list'''

daftarBuah = ["apel", "jeruk", "pisang", "mangga"]
print(daftarBuah)
print(daftarBuah[0])  # Mengakses elemen pertama
daftarBuah[1] = "anggur"  # Mengubah elemen kedua
daftarBuah.append("semangka")  # Menambahkan elemen baru
daftarBuah.insert(2, "kiwi")  # Menyisipkan elemen pada indeks tertentu
daftarBuah.remove("pisang")  # Menghapus elemen tertentu
daftarBuah.pop()  # Menghapus elemen terakhir
print(daftarBuah)
print(type(daftarBuah))

# Tuples
'''
- Can contain multiple values
- Ordered but unchangeable
- Use () to define a tuple'''

daftarLaptop = ("Asus", "Lenovo", "HP", "Dell")
print(daftarLaptop)
# daftarLaptop[1] = "Acer"  # Akan menghasilkan error karena tuple tidak dapat diubah
print(type(daftarLaptop))

# Sets
'''
- Can contain multiple values
- Unordered and unindexed
- Unchangeable but can add new items
- Use {} to define a set'''

daftarAngka = {1, 2, 3, 4, 5}
print(daftarAngka)
daftarAngka.add(6)  # Menambahkan elemen baru
daftarAngka.remove(2)  # Menghapus elemen tertentu
print(daftarAngka)
print(type(daftarAngka))


# Dictionaries
'''
- Can contain multiple values in key-value pairs
- Ordered and changeable
- Use {} to define a dictionary'''

daftarMahasiswa = {"nama": "John", "usia": 20, "jurusan": "Informatika"}
print(daftarMahasiswa)
daftarMahasiswa["nama"] = "Jackson" # Mengubah nilai berdasarkan kunci
print(daftarMahasiswa["usia"])  # Mengakses nilai berdasarkan kunci
print(type(daftarMahasiswa))