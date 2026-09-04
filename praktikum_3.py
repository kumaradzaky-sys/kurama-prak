hasil = 3+8
print(3,'+',8,'=',hasil)
hasil = 13-4
print(13,'-',4,'=',hasil)
hasil = 9*9
print(9,'*',9,'=',hasil)
hasil = 27/3
print(27,'/',3,'=',hasil)
hasil = 12**3
print(12,'**',3,'=',hasil)
hasil = 55%6
print(55,'%',6,'=',hasil)
hasil = 77//7
print(77,'//',7,'=',hasil)

celcius = float(input('masukan suhu dalam celcius : '))
print("suhu adalah", celcius, "Celcius")
reamur = (4/5) * celcius
print("suhu dalam reamur adalah ",reamur, "Reamur")
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit")
kelvin = celcius + 273
print("suhu dalam kelvin adalah ", kelvin, "Kelvin")

a = 4
b = 2
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)
hasil = a < 5
print(a,'<',5,'=',hasil)
hasil = b < 8
print(b,'<',8,'=',hasil)
hasil = a >= 8
print(a,'>=',8,'=',hasil)
hasil = a <= 9
print(a,'<=',9,'=',hasil)
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = a != 3
print(a,'!=',3,'=',hasil)

#tugas pertemuan 3
panjang = 12
lebar = 5
tinggi = 8
#luas
hasil = 2*(panjang*lebar+panjang*tinggi+lebar*tinggi)
print(2,'*',(panjang,'*',lebar,'+',panjang,'*',tinggi,'+',lebar,'*',tinggi),'=',hasil)
#volume
hasil = panjang*lebar*tinggi
print(panjang,'*',lebar,'*',tinggi,'=',hasil)
#keliling
hasil = 4*(panjang+lebar+tinggi)
print(4,'*',(panjang,'+',lebar,'+',tinggi),'=',hasil)

luas = 392
volume = 480
keliling = 100
hasil = luas > 50
print(luas,'>',50,'=',hasil)
hasil = volume == 480
print(volume,'==',480,'=',hasil)