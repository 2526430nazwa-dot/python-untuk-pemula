print("Hello, World!")

# Ini komentar
print("Halo, Python!")

if True:
    print("Indentasi itu penting")





nama = "Budi"          # str (teks)
umur = 17              # int (bilangan bulat)
tinggi = 170.5         # float (bilangan desimal)
siswa = True           # bool (benar/salah)

print(nama, type(nama))
print(umur, type(umur))
print(tinggi, type(tinggi))
print(siswa, type(siswa))




# Bab 4: Variable
nama = "Budi"
umur = 17
print(nama, umur)

# Mengubah nilai variable
umur = 18
print(umur)

# Assign beberapa variable sekaligus
x, y, z = 1, 2, 3
a = b = c = 0
print(x, y, z, a, b, c)

# Aturan penamaan: huruf, angka, underscore; tidak boleh diawali angka
nama_lengkap = "Budi Santoso"
print(nama_lengkap)




# Bab 5: Konstanta
# Python tidak punya konstanta sungguhan.
# Konvensinya: nama ditulis HURUF BESAR agar tidak diubah.
PI = 3.14159
GRAVITASI = 9.8
NAMA_SEKOLAH = "SMKN 2 Subang"

print(PI)
print(GRAVITASI)
print(NAMA_SEKOLAH)

# Contoh pemakaian
jari_jari = 7
luas_lingkaran = PI * jari_jari ** 2
print("Luas lingkaran:", luas_lingkaran)