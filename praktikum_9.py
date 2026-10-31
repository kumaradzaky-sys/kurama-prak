# pengenalan list
konstelasi = ["ophiuchus", "libra", "gemini", "virgo"]
print(konstelasi)

# mutable list (dapat di ubah)
konstelasi = ["ophiuchus", "libra", "gemini", "virgo"]
konstelasi[2] = "scorpio"
print(konstelasi)

# list menggunakan range
data_range = range(0, 15, 4)
print(list(data_range))

# list comprehension
list_for = [i**3 for i in range(0,7)]
print(list_for)

# list comprehension dengan kondisi if
list_for_if = [i for i in range(0,5) if i != 3]
print(list_for_if)

# indeks
data = ["freyja", "kelly", "alok", "jamal"]
print(data[2]) # positif (indeks dari depan)
print(data[-1]) # negatif (indeks dari belakang)

# menghitung jumlah data dengan len()
data = ["hubert", "shuko", "deden", "pablo"]
print(len(data))

# manipulasi list
# A. insert (menambah elemen pada posisi tertentu)
data = ["sijon", "dunga", "siri"]
data.insert(2, "dodo")
print(data)
# B. append (menambah elemen di akhir list)
data.append("luna")
print(data)
# C. extend (meenggabungkan dari list lain)
data.extend(["alvarez", "lutpi"])
print(data)
# D. remove (menghapus berdasar elemen)
data.remove("dunga")
print(data)
# E. pop (menghapus berdasar indeks)
data.pop(1)
print(data)

# operasi list
# A. count
data = [31, 32, 43, 54, 55 ,66 ,87 ,38 ,89 ,10 ,43 , 42, 57, 79 ,24]
print(data.count(43))
# B. indeks
print(data.index(55))
# C. sort (mengurutkan data)
data.sort() # kecil ke besar
data.sort(reverse=True) # besar ke kecil 
print(data)
# D. reverse (cuma membalik data)
data.reverse()
print(data)

# nested list
data_1 = [1, 2, 3]
data_2 = [4, 5, 6]
data_3 = [data_1, data_2]
print(data_3)

# mengambil elemen nested list
data = [[1, 2, 3], [4, 5, 6]]
print(data[0][1])  # mengambil nilai indeks ke 1 dari list pertama

# contoh penerapan nested list dengan perulangan
peserta = [["andi", "laki-laki", 20], ["budi", "laki-laki", 21], ["citra", "perempuan", 19]]
for peserta in peserta:
    print(f"Nama   : {peserta[0]}")
    print(f"Gender : {peserta[1]}")
    print(f"Umur   : {peserta[2]}")
    print()


# tugas pertemuan ke 7 (bab 9)

# no.1
data_kendaraan = ['motor', 'mobil', 'sepeda', 'bus']
#a.
data_kendaraan.append('truk')
print(data_kendaraan)
#b.
data_kendaraan.insert(1, "becak")
print(data_kendaraan)
#c.
data_kendaraan.pop(5)
print(data_kendaraan)
#d. 
data_kendaraan[3] = "skuter"
print(data_kendaraan)
#e. 
total = len(data_kendaraan)
print(f"Jumlah data = {total}")

# no.2
angka = [75, 80, 90, 75, 85, 100, 65] 
#a.
data = angka.index(100)
print(f"Indeks dari 100 = {data}")
#b.
count_75 = angka.count(75)
print(f"Jumlah skor 75 = {count_75}")
#c. 
data1 = sorted(angka)
print(f"Data setelah diurutkan = {data1}")
#d. 
data2 = data1[::-1]
print(f"Data setelah dibalik = {data2}")

# no.3
menu_utama = ["Nasi Goreng", "Mie Ayam"] 
menu_tambahan = ["Kerupuk", "Es Teh"] 
menu_utama.extend(menu_tambahan)
print(f"Menu komplit = {menu_utama}")

# no.4
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]] 
#a.
harga = data_barang[1][1]
print(f"Harga Pensil = {harga}")
#b.
for barang in data_barang:
    print(f"Nama Barang : {barang[0]}")
    print(f"Harga       : {barang[1]}")
    print()