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