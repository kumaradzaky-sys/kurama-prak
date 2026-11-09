# Tuple, set, dictionary

# Tuple 
data = (7, 8, 10, 11)
print(data)
print(data[-1])
# data.append(12)  # akan error karena tuple bersifat immutable (tidak bisa diubah)

# Sets (himpunan)
data = {10, 4, 3, 2, 7, 6, 5,}
print(data)
#print(data[3])  # akan error karena set tidak memiliki indeks

# Dictionary
data = {
    "nama":"Reza",
    "umur":67,
    "asal":"ngawi"}
print(data) # langsung semua key dan value
# key = nama,umur,asal (yang ada di depan)
# value = Reza,67,ngawi (yang ada di belakang)

# cara mengambil data
print(data["nama"])  # mengambil value dari key "nama"
print(data["umur"])  # mengambil value dari key "umur"
print(data["asal"])  # mengambil value dari key "asal"

# mengambil menggunakan get()
print(data.get("nama"))
print(data.get("alamat", "data tidak ada"))  # jika key tidak ada, akan menampilkan pesan default

# A.1) mengubah data
data = {
    "hewan":"kucing",
    "makanan":"wortel"} 
data["hewan"] = "badag"
print(data)  # akan menampilkan data yang sudah diubah

# A.2) menambahkan data   
data["habitat"] = "alam liar"
print(data)

# A.3) menggunakan update() (memperbarui data)
data.update({"hewan":"kuda"})
data.update({"makanan":"daging"})
print(data)

# B menghapus data (menggunakan del)
del data["habitat"]
print(data)

# looping dictionary
sports = {
    "SB":"sepak bola",
    "BB":"bola basket",
    "BV":"bola voli",}

# looping biasa
for key in sports:
    print(key)
# (secara default, looping dictionary akan menampilkan key)

# menggunakan .keys()
for key in sports.keys():
    print(key)

# menggunakan .values()
for value in sports.values():
    print(value)

# menggunakan .items()
for key, value in sports.items():
    print(f"key = {key}, value = {value}")

# Tugas pertemuan ke-8 bab(10)

# 1.a
mahasiswa = ("patrick", "676767", "teknologi informasi")
print(mahasiswa)

# 1.b
print("NIM:", mahasiswa[1])
print("Prodi:", mahasiswa[2])

# 1.c
# mahasiswa[2] = "sastra zimbabwe"  # akan error, karna ruple bersifat immutable (tidak bisa diubah)

# 1.d
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)
# Penjelasan: Angka 10 dan 4 yang ditulis dua kali hanya disimpan satu kali karena set tidak menerima duplikasi.

# 2.a
data_mahasiswa = {
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}
print(data_mahasiswa)

# 2.b
data_mahasiswa["prodi"] = "Sastra Mesin"
data_mahasiswa["angkatan"] = 2026
print(data_mahasiswa)

# 2.c
del data_mahasiswa["nim"]
print(data_mahasiswa)

# 3.a
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}
print(keranjang)

# 3.b
for buah, harga in keranjang.items():
    print(f"Harga {buah}: Rp {harga}")

# 3.c
total = 0
for harga in keranjang.values():
    total += harga
print("Total belanja: Rp", total)