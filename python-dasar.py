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




# Bab 6: Operator
a = 10
b = 3

# Operator aritmatika
print("Tambah:", a + b)
print("Kurang:", a - b)
print("Kali:", a * b)
print("Bagi:", a / b)
print("Bagi bulat:", a // b)
print("Sisa bagi:", a % b)
print("Pangkat:", a ** b)

# Operator perbandingan
print(a == b)
print(a != b)
print(a > b)
print(a <= b)

# Operator logika
print(a > 5 and b < 5)
print(a > 5 or b > 5)
print(not (a > b))

# Operator assignment
c = 5
c += 2
c *= 3
print("Nilai c:", c)





# Bab 7: Control Flow
nilai = 80

# Percabangan if, elif, else
if nilai >= 90:
    print("Grade A")
elif nilai >= 75:
    print("Grade B")
else:
    print("Grade C")

# Perulangan for
for i in range(1, 6):
    print("Perulangan ke-", i)

# Perulangan while
n = 1
while n <= 3:
    print("While:", n)
    n += 1

# break dan continue
for i in range(1, 10):
    if i == 3:
        continue
    if i == 6:
        break
    print("Angka:", i)





# Bab 8: Function
# Function tanpa parameter
def sapa():
    print("Halo, selamat belajar Python!")

sapa()

# Function dengan parameter
def sapa_nama(nama):
    print("Halo,", nama)

sapa_nama("Budi")

# Function dengan return
def tambah(a, b):
    return a + b

hasil = tambah(5, 3)
print("Hasil tambah:", hasil)

# Parameter default
def perkenalan(nama, kota="Subang"):
    print(f"Nama saya {nama}, dari {kota}")

perkenalan("Budi")
perkenalan("Ani", "Bandung")

# Function dengan banyak return value
def hitung(a, b):
    return a + b, a * b

jumlah, kali = hitung(4, 5)
print(jumlah, kali)