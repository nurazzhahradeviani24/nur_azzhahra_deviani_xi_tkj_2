# nama : NUR AZZHAHRA DEVIANI
# kelas : XI - TKJ 2
# nomor absen : 24

#Buat program Python yang mengambil nilai peforma karyawan (1 hingga 5, 
#dengan 5 sebagai peforma terbaik ) dan menghiitung bonus tahunan berdasarkan aturan berikut 
#- peforma 5 ; bonus 20% dari gaji tahunan
#- peforma 4 ; bonus 10% dari gaji tahunan
#- peforma 3 ; bonus 5% dari gaji tahunan
#- peforma 2 ; bonus 2% dari gaji tahunan
#- peforma 1 ; tidak ada bonus
#Buatlah program menggunakan percabangan ternary untuk menghitung bonus tersebut 

nilai_peforma = int(input("masukkan nilai peforma karyawan (1-5): "))
gaji_tahunan = float(input("masukkan gaji tahunan karyawan: "))

if nilai_peforma == 5:
    bonus_tahunan = 0.20
elif nilai_peforma == 4:
    bonus_tahunan = 0.10
elif nilai_peforma == 3:
    bonus_tahunan = 0.05
elif nilai_peforma == 2:
    bonus_tahunan = 0.02
elif nilai_peforma == 1:
    bonus_tahunan = 0

print("gaji karyawan adalah", gaji_tahunan+gaji_tahunan*bonus_tahunan)