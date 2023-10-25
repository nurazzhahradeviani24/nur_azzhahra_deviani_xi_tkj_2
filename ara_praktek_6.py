# nama : NUR AZZHAHRA DEVIANI
# kelas : XI - TKJ 2
# nomor absen : 24


#Buat program Python yang mengambil data penjualan bulanan produk dan menentukan kategori 
#produk berdasarkan penjualan 
#- Jika pennjualan lebih dari 1000 unit, dikategorikan sebagai "produk terlaris"
#- jika penjualan antara  500 hingga 1000  unit, dikategorikan sebagai "Produk Terpopuler"
#- Jika penjualan kurang dari 500 unit, dikategorikan sebagai "Produk biasa"

data_penjualan_bulanan_produk = int(input("Masukkan data penjualan: "))
if data_penjualan_bulanan_produk > 1000:
    kategori = "Produk Terlaris"
    
elif data_penjualan_bulanan_produk > 500:
    kategori = "Produk Populer"
elif data_penjualan_bulanan_produk >= 0:
    kategori = "Produk Biasa"
else:
    kategori = "Tidak Valid"

print(f"Produk tersebut termasuk dalam kategori", {kategori})