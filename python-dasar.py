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







# Bab 9: List, Tuple, dan Set
# List: berurutan, bisa diubah
buah = ["apel", "jeruk", "mangga"]
print(buah)
print(buah[0])
buah.append("pisang")
buah.remove("jeruk")
buah[0] = "anggur"
print(buah)
print("Jumlah:", len(buah))

# Tuple: berurutan, TIDAK bisa diubah
koordinat = (10, 20)
print(koordinat)
print(koordinat[0])

# Set: tidak berurutan, tidak ada duplikat
angka = {1, 2, 3, 3, 2}
print(angka)
angka.add(4)
print(angka)

# Operasi set
a = {1, 2, 3}
b = {3, 4, 5}
print("Gabungan:", a | b)
print("Irisan:", a & b)
print("Selisih:", a - b)




# Bab 10: Dictionary
# Dictionary menyimpan data dalam pasangan key: value
siswa = {
    "nama": "Budi",
    "umur": 17,
    "jurusan": "RPL"
}
print(siswa)

# Mengakses nilai
print(siswa["nama"])
print(siswa.get("umur"))

# Menambah dan mengubah data
siswa["kelas"] = "XI"
siswa["umur"] = 18
print(siswa)

# Menghapus data
del siswa["kelas"]
print(siswa)

# Mengambil keys, values, dan items
print(siswa.keys())
print(siswa.values())
print(siswa.items())

# Perulangan pada dictionary
for key, value in siswa.items():
    print(key, "=", value)

# Mengecek key
print("nama" in siswa)





# Bab 11: Class & Object
# Class adalah cetakan, object adalah hasil cetakannya
class Mahasiswa:
    # Atribut class (dimiliki semua object)
    kampus = "SMKN 2 Subang"

    # Constructor: dijalankan saat object dibuat
    def __init__(self, nama, jurusan):
        self.nama = nama          # atribut object
        self.jurusan = jurusan

    # Method: function di dalam class
    def perkenalan(self):
        print(f"Halo, saya {self.nama} dari jurusan {self.jurusan}")

    def info_kampus(self):
        print("Sekolah:", self.kampus)

# Membuat object dari class
siswa1 = Mahasiswa("Budi", "RPL")
siswa2 = Mahasiswa("Ani", "TKJ")

# Mengakses atribut dan method
print(siswa1.nama)
siswa1.perkenalan()
siswa2.perkenalan()
siswa1.info_kampus()

# Mengubah atribut object
siswa1.jurusan = "DKV"
siswa1.perkenalan()





# Bab 12: Encapsulation
# Encapsulation menyembunyikan data agar tidak diubah sembarangan
class RekeningBank:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik        # public
        self._cabang = "Subang"       # protected (konvensi: satu underscore)
        self.__saldo = saldo          # private (dua underscore)

    # Getter: membaca data private
    def get_saldo(self):
        return self.__saldo

    # Setter: mengubah data private dengan validasi
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setor {jumlah} berhasil")
        else:
            print("Jumlah setor tidak valid")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Tarik {jumlah} berhasil")
        else:
            print("Saldo tidak cukup")

akun = RekeningBank("Budi", 100000)
print(akun.pemilik)
print("Saldo:", akun.get_saldo())

akun.setor(50000)
akun.tarik(30000)
akun.tarik(999999)
print("Saldo akhir:", akun.get_saldo())

# Akses langsung ke atribut private akan error
# print(akun.__saldo)






# Bab 13: Inheritance
# Inheritance: class anak mewarisi atribut dan method dari class induk
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def makan(self):
        print(f"{self.nama} sedang makan")

    def suara(self):
        print("Hewan mengeluarkan suara")

# Class anak mewarisi class Hewan
class Kucing(Hewan):
    def suara(self):                  # method overriding
        print(f"{self.nama}: Meong")

class Anjing(Hewan):
    def __init__(self, nama, ras):
        super().__init__(nama)        # memanggil constructor induk
        self.ras = ras

    def suara(self):
        print(f"{self.nama} ({self.ras}): Guk guk")

kucing = Kucing("Tom")
anjing = Anjing("Rex", "Husky")

kucing.makan()        # method warisan
kucing.suara()        # method yang di-override
anjing.makan()
anjing.suara()

# Mengecek hubungan class
print(isinstance(kucing, Hewan))
print(issubclass(Anjing, Hewan))




# Bab 14: Polymorphism
# Polymorphism: method dengan nama sama, tetapi perilakunya berbeda
class Burung:
    def bergerak(self):
        print("Burung terbang")

class Ikan:
    def bergerak(self):
        print("Ikan berenang")

class Kuda:
    def bergerak(self):
        print("Kuda berlari")

# Satu function dipakai untuk berbagai object
def gerakkan(hewan):
    hewan.bergerak()

for h in [Burung(), Ikan(), Kuda()]:
    gerakkan(h)

# Polymorphism lewat inheritance (method overriding)
class Bentuk:
    def luas(self):
        return 0

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return 3.14 * self.jari_jari ** 2

daftar_bentuk = [Persegi(4), Lingkaran(7)]
for bentuk in daftar_bentuk:
    print(type(bentuk).__name__, "luas:", bentuk.luas())

# Polymorphism pada function bawaan
print(len("Python"))
print(len([1, 2, 3, 4]))




# Bab 15: Abstraction
# Abstraction: menyembunyikan detail, hanya menampilkan hal yang penting
from abc import ABC, abstractmethod

# Abstract class: tidak bisa dibuat object langsung
class Kendaraan(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def jalan(self):
        pass

    @abstractmethod
    def suara(self):
        pass

    # Method biasa tetap boleh ada di abstract class
    def info(self):
        print(f"Kendaraan: {self.nama}")

# Class turunan wajib mengimplementasikan semua abstract method
class Motor(Kendaraan):
    def jalan(self):
        print(f"{self.nama} melaju dengan 2 roda")

    def suara(self):
        print("Brum brum")

class Mobil(Kendaraan):
    def jalan(self):
        print(f"{self.nama} melaju dengan 4 roda")

    def suara(self):
        print("Tin tin")

motor = Motor("Vario")
mobil = Mobil("Avanza")

for k in [motor, mobil]:
    k.info()
    k.jalan()
    k.suara()

# Membuat object dari abstract class akan error
try:
    k = Kendaraan("Umum")
except TypeError as e:
    print("Error:", e)






# Bab 16: Exception Handling
# Exception handling menangani error agar program tidak berhenti mendadak

# try dan except
try:
    hasil = 10 / 0
except ZeroDivisionError:
    print("Error: tidak bisa membagi dengan nol")

# Menangkap beberapa jenis error
try:
    angka = int("abc")
except ValueError:
    print("Error: input bukan angka")
except TypeError:
    print("Error: tipe data salah")

# Menampilkan pesan error asli
try:
    daftar = [1, 2, 3]
    print(daftar[5])
except IndexError as e:
    print("Error:", e)

# else dan finally
try:
    angka = int("42")
except ValueError:
    print("Gagal konversi")
else:
    print("Berhasil, nilainya:", angka)
finally:
    print("Blok finally selalu dijalankan")

# Membuat error sendiri







# Bab 17: File Handling
# Menulis file (mode "w": buat baru atau timpa isi lama)
with open("catatan.txt", "w") as f:
    f.write("Baris pertama\n")
    f.write("Baris kedua\n")

# Menambah isi file (mode "a": append)
with open("catatan.txt", "a") as f:
    f.write("Baris ketiga\n")

# Membaca seluruh isi file (mode "r")
with open("catatan.txt", "r") as f:
    isi = f.read()
    print(isi)

# Membaca per baris
with open("catatan.txt", "r") as f:
    for baris in f:
        print("Baris:", baris.strip())

# Menangani file yang tidak ada
try:
    with open("tidak_ada.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: file tidak ditemukan")





# Bab 18: Module
# Mengimpor module bawaan Python
import math
import random
from datetime import date

print("Akar 16:", math.sqrt(16))
print("Pembulatan ke atas:", math.ceil(4.2))
print("Angka acak 1-10:", random.randint(1, 10))
print("Tahun ini:", date.today().year)

# Mengimpor module buatan sendiri
import alat_hitung
print("Tambah:", alat_hitung.tambah(5, 3))
print("Kali:", alat_hitung.kali(4, 6))

# Mengimpor sebagian isi module dan memberi alias
from alat_hitung import luas_lingkaran as luas
print("Luas lingkaran:", luas(7))




# Bab 19: Package
# Package: folder berisi kumpulan module dan file __init__.py
from alat import matematika, teks

print("Tambah:", matematika.tambah(10, 5))
print("Pangkat:", matematika.pangkat(2, 8))
print("Huruf besar:", teks.huruf_besar("python"))
print("Dibalik:", teks.balik("python"))

# Mengimpor function langsung dari package
from alat.matematika import tambah as jumlah
print("Jumlah:", jumlah(7, 3))