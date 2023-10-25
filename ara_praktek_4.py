# nama : NUR AZZHAHRA DEVIANI
# kelas : XI - TKJ 2
# nomor absen : 24

#Soal 4:
#Deskripsi Pekerjaan: Sebagai seorang kasir di toko, Anda harus menghitung jumlah diskon
#berdasarkan total belanjaan pelanggan dan jenis anggota (anggota biasa atau anggota premium).
#Soal:
#Buat program Python yang mengambil total belanjaan dan status anggota (biasa atau premium). Berikan diskon berdasarkan aturan berikut:
#• Anggota premium: Jika total belanjaan lebih dari 500.000, berikan diskon 15%. Jika tidak, berikan diskon 10%.
#• Anggota biasa: Jika total belanjaan lebih dari 300.000, berikan diskon 7%. Jika tidak, berikan diskon 0%.

total_belanja = float(input("Total Belanjaan Anda: "))
member = input("Status Anggota (biasa/premium): ")
diskon = 0
if member == "premium":
    if total_belanja > 500000:
        diskon = 0.15
    else:
        diskon = 0.10
elif member == "biasa":
    if total_belanja > 300000:
        diskon = 0.07
total_membayar = total_belanja - (total_belanja * diskon)
print(f"Total yang harus dibayar: Rp {total_membayar:.2f}")
