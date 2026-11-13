# program 11.1 multi keys dan nesting dictionary
import datetime


mahasiswa1 = {
    'nama': 'Ucup Surucup',
    'nim': '19022001',
    'sks_lulus': 130,
    'beasiswa': False,
    'lahir': datetime.datetime(2001,4,10) # tahun, bulan, tanggal
}

mahasiswa2 = {
    'nama': 'Azan Magrib',
    'nim': '19022002',
    'sks_lulus': 140,
    'beasiswa': True,
    'lahir': datetime.datetime(2002,10,10) # tahun, bulan, tanggal
}

mahasiswa3 = {  
    'nama': 'Slamet skibidi',
    'nim': '19022003',
    'sks_lulus': 100,
    'beasiswa': True,
    'lahir': datetime.datetime(1977,5,10) # tahun, bulan, tanggal
}      

data_mahasiswa = {  'MAH001':mahasiswa1,
                    'MAH002':mahasiswa2,  
                    'MAH003':mahasiswa3, 
} 

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-" * 50)
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa 
    NAMA = data_mahasiswa[KEY]['nama']     
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus'] 
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:<9} {LAHIR:<10}")

# Program 11.2 Latihan Dictionary Bagian 1  
import datetime

mahasiswa_template = {
    'nama':'nama',
    'nim':00000000,
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11) 
}
data_mahasiswa = {}

print(f"{'SELAMAT DATANG':^50}")
print(f"{'DATA MAHASISWA':^50}")
print("-" * 65)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)
mahasiswa['nama'] = input("Nama Mahasiswa: ")
mahasiswa['nim'] = input("NIM Mahasiswa: ")
mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)
print(mahasiswa) 

# Program 11.3 Latihan Dictionary Bagian 2

import datetime
import os
import string
import random

# template dict mahasiswa
mahasiswa_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}
data_mahasiswa = {}

while True:
    # os.system("cls") # untuk windows
    # os.system("clear") # untuk linux
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})
    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal Lahir':<10}")
    print('-'*60)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
        print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")
    print("\n")
    is_done = input("Mau tambah lagi bro (y/n)? ")
    if is_done == "n":
        break
print("\nEnd of program, terima kasih")

# Tugas/Latihan praktikum pertemuan ke-11

import datetime
import os
import string
import random

# Template dictionary buku
buku_template = {
    'judul': 'judul',
    'penulis': 'penulis',
    'tahun_terbit': 0,
    'tanggal_terakhir_pinjam': datetime.datetime(1111, 1, 11),
    'status': 'status'
}

data_buku = {}

while True:
    os.system("cls")

    print(f"{'SELAMAT DATANG':^30}")
    print(f"{'SISTEM PERPUSTAKAAN':^30}")
    print("-" * 30)

    # Membuat dictionary buku
    buku = dict.fromkeys(buku_template.keys())

    buku['judul'] = input("Judul Buku: ")
    buku['penulis'] = input("Penulis Buku: ")
    buku['tahun_terbit'] = int(input("Tahun Terbit: "))

    TAHUN_PINJAM = int(input("Tahun Terakhir Pinjam (YYYY): "))
    BULAN_PINJAM = int(input("Bulan Terakhir Pinjam (1-12): "))
    TANGGAL_PINJAM = int(input("Tanggal Terakhir Pinjam (1-31): "))

    buku['tanggal_terakhir_pinjam'] = datetime.datetime(
        TAHUN_PINJAM, BULAN_PINJAM, TANGGAL_PINJAM
    )

    buku['status'] = input("Status (TERSEDIA/TIDAK): ").upper()

    # Membuat KEY acak
    KEY = ''.join(
        random.choice(string.ascii_uppercase) for i in range(6)
    )

    # Menambahkan buku ke data perpustakaan
    data_buku.update({KEY: buku})

    # Menampilkan data buku
    print(f"\n{'KEY':<6} {'Judul Buku':<20} {'Penulis':<17} {'Tahun':<6} {'Tanggal Pinjam':<15} {'Status':<10}")
    print("-" * 80)

    for buku in data_buku:
        KEY = buku

        JUDUL = data_buku[KEY]['judul']
        PENULIS = data_buku[KEY]['penulis']
        TAHUN = data_buku[KEY]['tahun_terbit']
        TANGGAL = data_buku[KEY]['tanggal_terakhir_pinjam'].strftime("%x")
        STATUS = data_buku[KEY]['status']

        print(f"{KEY:<6} {JUDUL:<20} {PENULIS:<17} {TAHUN:<6} {TANGGAL:<15} {STATUS:<10}")

    print("\n")
    is_done = input("Mau tambah buku lagi (y/n)? ")

    if is_done == "n":
        break

print("\nEnd of program, terima kasih")