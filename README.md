# lab2-3

# struktur kondisi
<P>LATIHAN 1</P>
buat program sederhana dengan input 2 buah
bilangan, kemudian tentukan bilangan terbesar dari kedua bilangan tersebut menggunakan statement if.

![lat ss1](https://github.com/annisasaidah06/lab2-3.py/assets/148035766/2e06a324-2334-4be2-98a4-af7817f718af)


<p>LATIHAN 2</p>
buat program untuk mengurutkan data berdasarkan input sejumlah 
data(minimal 3 variable input atau lebih), kemudian tampilkan hasilnya
secara berurutan mulai dari data terkecil

![lat ss2](https://github.com/annisasaidah06/lab2-3.py/assets/148035766/da27a5ad-c376-46a6-a48a-c6a38dc1e6dd)

# perulangan
<p>LATIHAN 1</p>
buat program dengan perulangan bertingkat(nested) for yang menghasilkan output sebagai berikut:

![SS1](https://github.com/annisasaidah06/lab2-3.py/assets/148035766/33797fd0-81fc-4f62-a17e-84aafc789f4e)


Penjelasan

Pendeklarasian variable
baris = 10
kolom = baris
Untuk perulangan baris dan kolom menggunakan for
for bar in range(baris):
    for col in range(kolom):
        tab = bar+col        
Untuk menampikan hasil dari perulangan
Agar terlihat rapih menggunakan format string rata ke kanan sebanyak 5 karakter
Agar tidak membuat baris baru menggunakan end='' (baris)
<p>LATIHAN 2

tampilkan n bilangan acak yang lebih kecil dari 0,5
nilai n diisi pada saat runtime
anda bisa menggunakan kombinasi while and for untuk menyelesaikannya  

![SS2](https://github.com/annisasaidah06/lab2-3.py/assets/148035766/f32c5875-a0ed-4964-ba11-9e21ea5da0fa)

penjelasan

import random Untuk membuat bilangan acak
jum = int(input("Masukan nilai: ")) Menentukan jumlah input & di konversikan dalam bilangan bulat-dimasukan ke variable jum/jumlah
while i in range(jum) Pengulangan
Menampilkan urutan sesuai inputan dengan hasil di bawah 0.5



