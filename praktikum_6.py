# nested if

status_akun = "aktif"
saldo = 1000000000
nominal_penarikan = 1000000
if status_akun == "aktif":
    if nominal_penarikan <= saldo:
        if nominal_penarikan >= 1000000000:
            saldo = saldo - nominal_penarikan
            print(f"penarikan berhasil: rp{nominal_penarikan:,}")
            print(f"sisa saldo: rp{saldo:,}")
        else:
            print("penarikan gagal: minimal penarikan rp100.000")
    else:
        print("penarikan gagal: saldo tidak mencukupi")    
else:
    print("akses ditolak: kartu kadaluarsa")