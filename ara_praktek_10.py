# nama : NUR AZZHAHRA DEVIANI
# kelas : XI - TKJ 2
# nomor absen : 24

#Buat program Python yang mengambil durasi peminjaman buku dalam hari dan menentukan jenis
#pinjaman berdasarkan aturan berikut:
#- peminjaman 7 hari atau kurang: "Peminjaman pendek"
#- peminjaman lebih dari 7 hari hingga 30  hari:  "Peminjaman menengah"
#- peminjaman lebih dari 30 hari: "peminjaman panjang"

durasi_peminjaman_buku = int(input("Berapa hari meminjam buku: "))

if durasi_peminjaman_buku < 7:
    jenis_peminjaman = "pendek"
elif durasi_peminjaman_buku < 30:
    jenis_peminjaman = "menengah"
else:
    jenis_peminjaman = "panjang"

print(f"Jenis peminjaman: Peminjaman {jenis_peminjaman}")