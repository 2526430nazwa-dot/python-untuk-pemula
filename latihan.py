print("Halo Python")



# Tipe data floating numbers
a = 7.5

print(a)


# Tipe data integers
x = 5
y = 3
z = 5 + 3

print(z)

# Tipe data floating numbers
a = 7.5

print(a)


# Menggunakan single quote
myFirstName = 'Rizqi'

# Menggunakan double quote
myLastName = "Maulana"

# Penulisan Angka sebagai string
myAge = "25"

# Penulisan string multiline
myHobby = """Hobi saya adalah
bersepeda dan bermain game.
"""

# Mencetak 2 variabel string dengan perintah print
print(myFirstName + " " + myLastName)
print("Umur saya " + myAge)


# Contoh penulisan boolean yang benar
a = True
b = False

# Contoh penulisan boolean yang salah
# Jika dijalankan, pada baris ini akan error
# c = true

# print(c)


a = 4
b = 2
# Penjumlahan
c = a + b
# Pengurangan
d = a - b
# Perkalian
e = a * b
# Pembagian
f = a / b
# Modulus
g = a % b
# Eksponensial
h = a ** b

# Cetak output
print(c) # 6
print(d) # 2
print(e) # 8
print(f) # 2
print(g) # 0
print(h) # 16


a = 3
b = 5
# Perbandingan sama dengan
c = a == b
# Perbandingan tidak sama dengan
d = a != b
# Perbandingan lebih kecil
e = a < b
# Perbandingan lebih kecil sama dengan
f = a <= b
# Perbandingan lebih besar
g = a > b
# Perbandingan lebih besar sama dengan
h = a >= b

# Cetak output
print(c) # False
print(d) # True
print(e) # True
print(f) # True
print(g) # False
print(h) # False


a = 3
b = 9

# Contoh Penggunaan "and"
print(a < 5 and b > 6) # True
print(a < 5 and b < 6) # False
print(a > 5 and b < 6) # False

# Contoh Penggunaan "or"
print(a < 5 or b > 6) # True
print(a < 5 or b < 6) # True
print(a > 5 or b < 6) # False

# Contoh Penggunaan "not"
print(not(a < 5 or b > 6)) # False
print(not(a > 5 or b < 6)) # True




# Membuat lists yang berisi nama-nama hewan
animals = ["Ayam", "Bebek", "Cicak"]

# Kita bisa mengakses item di dalam "Lists" berdasarkan urutannya (indexing)
# semisal kita ingin mengakses item "Bebek" (urutan kedua), maka kita bisa menggunakan indexing "1"
# kenapa tidak menggunakan indexing "2"? karena indexing dimulai dari angka 0, bukan 1 (n - 1)

print(animals[1]) # Bebek

# Jika kita ingin mengakses dengan urutan sebaliknya (dari urutan paling akhir),
# kita bisa menggunakan negative indexing
# Jika kita menggunakan indexing "-1", artinya kita mengakses item terakhir
# Jika menggunakan indexing "-2", artinya kita mengakses item kedua dari urutan terakhir

print(animals[-1]) # Cicak
print(animals[-2]) # Bebek



animals = ["Ayam", "Bebek", "Cicak"]

# Menambah item pada "Lists" dengan posisi (indexing) terakhir menggunakan function "append"
animals.append("Domba")
print(animals) # ["Ayam", "Bebek", "Cicak", "Domba"]

# Menambah item pada "Lists" dengan posisi (indexing) tertentu menggunakan function "insert"
# Contoh kita ingin menambahkan 1 item dengan posisi ketiga (indexing = 2)

animals.insert(2, "Buaya")
print(animals) # ['Ayam', 'Bebek', 'Buaya', 'Cicak', 'Domba']



animals = ["Ayam", "Bebek", "Cicak"]

# Menghapus item tertentu (Bebek) pada "Lists" dengan method "remove"
animals.remove("Bebek")
print(animals) # ["Ayam", "Cicak"]

# Menghapus item terakhir pada "Lists" dengan method "pop"
animals = ["Ayam", "Bebek", "Cicak"]
animals.pop()
print(animals) # ["Ayam", "Bebek"]

# Menghapus item berdasarkan posisinya (indexing) pada "Lists" dengan method "pop"
animals = ["Ayam", "Bebek", "Cicak"]
animals.pop(0)
print(animals) # ["Bebek", "Cicak"]

# Menghapus semua item pada "Lists" dengan method "clear"
animals = ["Ayam", "Bebek", "Cicak"]
animals.clear()
print(animals) # []


# Menggabungkan sebuah "Lists" dengan "Lists" lainnya
animals = ["Ayam", "Bebek", "Cicak"]
otherAnimals = ["Domba", "Elang", "Gajah"]
animals.extend(otherAnimals)
print(animals) # ["Ayam", "Bebek", "Cicak", "Domba", "Elang", "Gajah"]

fruits = ["Apel", "Mangga", "Pisang"]
otherFruits = ["Durian", "Semangka", "Jeruk"]
allFruits = fruits + otherFruits
print(allFruits) # ["Apel", "Mangga", "Pisang", "Durian", "Semangka", "Jeruk"]



# Membuat Dictionaries untuk menyimpan informasi biodata seseorang (nama dan umur)
firstPerson = {
    "first_name": "Hana",
    "last_name": "Malika",
    "age": 10
}

# Untuk mengakses item pada Dictionaries bisa menggunakan 2 cara
# Cara pertama
print(firstPerson['first_name']) # Hana
# Cara kedua dengan method "get"
print(firstPerson.get('age')) # 10

# Untuk mendapatkan semua "keys" dari Dictionaries
print(firstPerson.keys()) # dict_keys(['name', 'age'])

# Untuk mendapatkan semua "values" dari Dictionaries
print(firstPerson.values()) # dict_values(['Hana', 'Malika', 10, 12])



firstPerson = {
    "first_name": "Hana",
    "last_name": "Malika",
    "age": 10
}

# Menambahkan item ke dalam Dictionaries
# Menambahkan item berat bedan (weight) ke dalam firstPerson
firstPerson['weight'] = 12
print(firstPerson) # {'first_name': 'Hana', 'last_name': 'Malika', 'age': 10, 'weight': 12}




firstPerson = {
    "first_name": "Hana",
    "last_name": "Malika",
    "age": 10
}

# Ada 2 cara untuk mengubah atau mengupdate sebuah value dari item pada Dictionaries

# Cara Pertama
firstPerson['age'] = 15

# Cara Kedua dengan method "update"
# Jika kita menggunakan cara ini, ketika item yang di update berdasarkan key (age) ditemukan,
# maka akan diupdate.
# Namun jika item belum ada, maka otomatis akan menambahkan item baru
firstPerson.update({"age": 15})
firstPerson.update({"hair_color": "black"})
print(firstPerson) # {'first_name': 'Hana', 'last_name': 'Malika', 'age': 15, 'hair_color': 'black'}



firstPerson = {
    "first_name": "Hana",
    "last_name": "Malika",
    "age": 10
}

# Untuk menghapus item dari Dictionaries, kita bisa menggunakan method "pop"
# Kita wajib menambahkan nama "key" jika menggunakan method "pop"
firstPerson.pop("age")
print(firstPerson) # {'first_name': 'Hana', 'last_name': 'Malika'}

# Untuk menghapus semua item, kita bisa menggunakan method "clear"
firstPerson.clear()
print(firstPerson) # {}


"""
Note:
Penulisan kode di dalam blok atau scope pada Python bergantung pada Indentation (spasi di awal baris). Contoh jika kita ingin 
menulis kode di dalam blok/scope Statemen if, maka penulisanny seperti ini:
"""

# Penulisan yang benar:
if(True):
    print("Benar.") # ada spasi di awal baris (lebih menjorok ke dalam)

# Penulisan yang salah:
# if(True):
# print("Benar.") # tidak ada spasi di awal baris (sejajar dengan kode di atasnya)


x = 5
y = 10

# karena x lebih kecil dari y adalah benar. maka kode di dalam scope statemen if akan dijalankan.
if(x < y):
    print("nilai x lebih kecil dari y.") # ini akan dijalankan

# karena x lebih besar dari y adalah salah. maka kode di dalam scope statemen if tidak akan dijalankan.
if(x > y):
    print("nilai x lebih besar dari y.") # ini tidak akan dijalankan


a = 80

# disini kita melakukan pengecekan kedua dan ketiga jika pada statemen if bernilai False. Kode pada blok ini
# akan dijalankan hanya jika statemen elif bernilai True.

# Pengecekan pertama dengan if: if(a > 90)
# Pengecekan kedua dengan elif: elif(a > 70)

if(a > 90):
	print("Dapat nilai A.") # ini tidak akan dijalankan
elif(a > 70):
    print("Dapat nilai B.") # ini akan dijalankan 


a = 60

if(a > 90):
	print("Dapat nilai A.") # ini tidak akan dijalankan
elif(a > 70):
    print("Dapat nilai B.") # ini tidak akan dijalankan
else:
    print("Dapat nilai C.") # ini akan dijalankan




# Mencetak kata "Halo Python" sebanyak 5 kali
for x in range(5):
    print("Halo Python.")



# Mencetak semua item pada variabel fruits (lists)
fruits = ['Apple', 'Banana', 'Mango', 'Durian']
for fruit in fruits:
    print(fruit)

# Mencetak semua huruf satu per satu pada kata "Indonesia"
myCountry = "indonesia"
for x in myCountry:
    print(x)
    
    # Mencetak angka, jika angka lebih kecil dari 5
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# Menghentikan perulangan jika nilai x adalah 3
# Pada kode di bawah ini, jika nilai x sama dengan 3,
# maka perulangan akan dihentikan. Walaupun seharusnya
# perulangan akan berhenti setelah 5 kali berjalan.
for x in range(5):
    print(x)
    if x == 3:
        break

# Melewati perulangan jika nilai x adalah angka genap (2, 4, 6 dst)
# Pada kode di bawah ini, hanya akan mencetak angka ganjil 
# karena jika angka adalah genap,maka proses mencetak akan
# kita skip menggunakan keyword "continue"

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)