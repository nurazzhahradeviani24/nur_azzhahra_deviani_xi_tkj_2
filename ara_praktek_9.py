# nama : NUR AZZHAHRA DEVIANI
# kelas : XI - TKJ 2
# nomor absen : 24

#Buat program Python yang mengambil status persiapan proyek dan menentukan apakah proyek 
#tersebut dapat diluncurkan. jika status  persiapan "Siap", program harus mencetak "Proyek 
#diluncurkan". Jika status  persiapan "Tunda", program harus mencetak "Proyek ditunda"

status_persiapan_proyek = str(input("Masukkan status persiapan proyek (Siap/Tunda): ").lower())

if status_persiapan_proyek == "siap":
    tindakan = "diluncurkan."
elif status_persiapan_proyek == "tunda":
    tindakan = "ditunda."
else:
    tindakan = "tidak valid."

print(f"Proyek akan {tindakan}")
