# nama : NUR AZZHAHRA DEVIANI
# kelas : XI - TKJ 2
# nomor absen : 24

#Buat program Python yang mengambil informasi pembaruann perangkat lunak dan menentukan
#apakah sistem perlu di-restart. Jika pembaruan mengharuskan restart, reset program harus mencetak 
#"Sistem perlu di-restart". Jika tidak, programm harus mencetak "Sistem tidak perlu direstart"

informasi_pembaruan_perangkat_lunak = (input("Masukkan informasi pembaruan perangkat lunak (perlu/tidak): ").lower())

if informasi_pembaruan_perangkat_lunak == "perlu":
   informasi = "Sistem perlu di-restart."
elif informasi_pembaruan_perangkat_lunak == "tidak":
   informasi = "Sistem tidak perlu di-restart."
else:
   informasi = "Informasi yang dimasukkan tidak valid."
print(informasi)
