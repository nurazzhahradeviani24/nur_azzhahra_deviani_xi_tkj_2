# nama : NUR AZZHAHRA DEVIANI
# kelas : XI - TKJ 2
# nomor absen : 24


#Soal : Buat program python yang mengambil estimasi waktu selesai proyek  dan tanggal target selesai. Jika estimasi waktu selesai lebih awal atau sama dengan target,  program harus mencetak "Tepat waktu" jika tidak, program harus mencetak "Terlambat".

#jawaban 
estimasi_selesai = input("waktu selesai : ")
estimasi_target = input("waktu target : ")

if estimasi_selesai <= estimasi_target:
     print("Tepat waktu")
else:
    print("Terlambat")