# Perulangan
# for 
angka = [1,2,3,4,5]
for i in angka:
    print(i)
# menggunakan  range
angka = range(1,8)
for i in angka:
    print(i)
# menggunakan string
kata = "dahar"
for huruf in kata:
    print(huruf)
# while loop
angka = 1
while angka < 5:
    print(f"numero -> {angka}")
    angka = angka + 1
    print("live score")    
# pass
angka = 0
while angka < 5:
    if(angka == 3):
        pass
        print("kamu yang jaga")
    angka = angka + 1    
# continue
angka = 1
while angka < 5:
    if(angka == 3):
        angka = angka + 1    
        continue
    print("dupak")
    angka = angka + 1    
# break
angka = 1
while angka < 5:
    print("yoloo")
    angka = angka + 1
    if(angka == 3):
        break
    print("yoloo")   
# latihan perulangan
# menggunakan for
sisi = 4
count = 1
for i in range(sisi):
    print("*" * count)
    count = count + 1
# menggunakan while
sisi = 4
count = 1
while True:
    print("*" * count)
    count += 1
    if count > sisi:
        break

# tugas pertemuan 5
for angka in range(1,51):
    if angka % 2 == 0:
        print(f"{angka} angka genap")
    else:
        print(f"{angka} angka ganjil")

for angka in range(2, 101):
    prima = True
    for pembagi in range(2, int(angka ** 0.5) + 1):
        if angka % pembagi  == 0:
            prima = False
            break
    if prima:
        print(angka)