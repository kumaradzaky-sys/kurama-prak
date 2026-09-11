# logical
a = True
b = not a
print("data a =", a)
print("data b =", b)
# or
a = True 
b = False 
c = a or b
print(a, "or" , b, "=", c)
# and
a = True
b = True
print(a, "and" , b, "=", c)
# XOR
a = False
b = False
c = a ^ b 
print(a, "xor" , b, "=", c)
# logika dan komparasi
angka = float(input("masukan angka: "))
kurang_dari_3 = angka < 3
lebih_dari_10 = angka > 10
hasil = kurang_dari_3 or lebih_dari_10 
print("diluar rentang 3-10:", hasil)
lebih_dari_3 = angka > 3
kurang_dari_10 = angka < 10
hasil2 = lebih_dari_3 and kurang_dari_10 
print("didalam rentang 3-10:", hasil2)
# if else elif
nama = input("siapa nama anda? ")
# program if inline
if nama=="ucup": print("halo bos")
# program if identation
if nama=="ucup":
    print("kece abiezz mas")
    print("kamu juga oke")
# else statement
if nama=="paijo":
    print("hey antek asing")
else:
     print("bukan kah ini my")
# elif statement(else if)
nama = input ("siapa nama anda?")
if nama=="ucup": 
    print("hi orang ganteng ")
elif nama=="wowok":
    print("salam pangeran sawit")
elif nama=="jack":
    print("jendral solo")
else:
    print("ini orang baik")

# tugas pertemuan 4
usia =int (input("berapa usia anda? = ")) 
if usia <= 12:
    print("anak-anak")
elif usia <= 17:
    print("remaja") 
elif usia <= 59:
    print("dewasa")
else:
    print("lansia")