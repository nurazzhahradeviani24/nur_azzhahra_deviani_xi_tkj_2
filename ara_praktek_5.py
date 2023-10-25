# nama : NUR AZZHAHRA DEVIANI
# kelas : XI - TKJ 2
# nomor absen : 24

#Soal 5:
#Deskripsi Pekerjaan: Sebagai seorang guru, Anda harus menentukan nilai akhir siswa berdasarkan
#nilai tugas dan ujian.
#Soal:
#Buat program Python yang mengambil nilai tugas (skala 0-100) dan nilai ujian (skala 0-100) seorang
#siswa dan menentukan nilai akhirnya. Jika nilai tugas lebih dari 70 dan nilai ujian lebih dari 60, siswa
#lulus dengan nilai "Lulus". Jika tidak, siswa gagal dengan nilai "Gagal".

nilai_tugas = float(input("Masukkan nilai tugas (skala 0-100): "))
nilai_ujian = float(input("Masukkan nilai ujian (skala 0-100): "))

lulus_tugas = nilai_tugas > 70
lulus_ujian = nilai_ujian > 60

if lulus_tugas and lulus_ujian:
    keterangan = "Selamat, Anda Lulus!"
else:
    keterangan = "Maaf, Anda Gagal."

if not lulus_tugas:
    print("Anda tidak lulus karena nilai tugas Anda di bawah 70.")
elif not lulus_ujian:
    print("Anda tidak lulus karena nilai ujian Anda di bawah 60.")
else:
    print(keterangan)
