# nama : NUR AZZHAHRA DEVIANI
# kelas : XI - TKJ 2
# nomor absen : 24


# Soal 3:
# Deskripsi Pekerjaan: Sebagai seorang sistem administrator, Anda bertanggung jawab untuk
# memeriksa apakah suatu file di server sudah ada atau belum sebelum menggantinya.
#Soal:
# Buat program Python yang memeriksa apakah suatu file sudah ada di direktori server. Jika file sudah ada, program harus mencetak "File sudah ada," jika tidak, program harus mencetak "File belumada."

nama_file = "data.txt"
daftar_file = ["file1.txt", "file2.txt", "file3.txt"]
if nama_file in daftar_file:
    print(f"File {nama_file} ada di server.")
else:
    print(f"File {nama_file} tidak ada di server.")
