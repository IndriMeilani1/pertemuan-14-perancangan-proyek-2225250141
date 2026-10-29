# pertemuan-14-perancangan-proyek-2225250141

Nama: Indri Meilani
NIM: 2225250141
Kelas: 3A

## Kasus
Program yang diuji adalah Program Rekap dan Analisis Nilai Matematika Kelas berbasis Python. Program ini digunakan untuk membaca data siswa dari file data/nilai_contoh.txt, memvalidasi nilai dalam rentang 0–100, menghitung rata-rata, nilai minimum dan maksimum, menentukan status ketuntasan berdasarkan KKM 60, serta menyimpan hasil analisis ke file output/hasil_analisis.txt. Pengujian dilakukan untuk memastikan program dapat memproses data valid dan menangani data yang tidak valid dengan benar.

## Test Case
Pengujian menggunakan delapan test case, yaitu TC01 menggunakan seluruh data pada nilai_contoh.txt dengan hasil yang diharapkan berupa 7 data valid, rata-rata 76,00, nilai minimum 55, maksimum 92, 6 siswa tuntas, 1 siswa belum tuntas, dan 2 data tidak valid; TC02 memasukkan nilai 0 yang seharusnya diterima tetapi berstatus belum tuntas; TC03 memasukkan nilai 100 yang seharusnya diterima dan berstatus tuntas; TC04 memasukkan nilai 105 yang seharusnya ditolak karena melebihi batas; TC05 memasukkan nilai abc yang seharusnya ditolak karena bukan angka; TC06 memasukkan nilai 60 yang seharusnya berstatus tuntas; TC07 menggunakan file yang tidak ditemukan dan mengharapkan program menampilkan pesan kesalahan; serta TC08 menggunakan file kosong atau seluruh data tidak valid dan mengharapkan program menampilkan pesan bahwa tidak ada data valid tanpa mengalami pembagian dengan nol. Actual Awal dan Status harus diisi berdasarkan hasil pengujian pertama yang benar-benar dijalankan; jika belum diuji, keduanya ditulis Belum diuji dan tidak langsung dinyatakan berhasil.

## Bug Report
Salah satu bug yang perlu diperiksa pada program adalah kesalahan ketika nilai tepat 60 tidak dianggap tuntas. Gejalanya adalah siswa dengan nilai 60 mendapatkan status belum tuntas, padahal nilai tersebut sudah memenuhi KKM. Lokasi bug berada pada fungsi tentukan_status() di file src/utilitas.py. Akar penyebabnya adalah penggunaan operator perbandingan > yang hanya menerima nilai di atas 60, bukan nilai yang sama dengan 60. Perbaikannya adalah mengganti operator tersebut menjadi >=, sehingga nilai yang sama dengan atau lebih besar dari KKM dinyatakan tuntas. Selain itu, program perlu diuji untuk memastikan nilai di luar rentang 0–100, nilai bukan angka, dan file yang tidak ditemukan ditangani dengan benar.

## Retest
Setelah perbaikan dilakukan, pengujian ulang dilakukan dengan memasukkan nilai 59, 60, dan 61. Hasil yang diharapkan adalah nilai 59 berstatus belum tuntas, sedangkan nilai 60 dan 61 berstatus tuntas. Program juga perlu dijalankan kembali menggunakan file data/nilai_contoh.txt untuk memastikan hasil analisis tetap menunjukkan 7 data valid, rata-rata 76,00, nilai minimum 55, nilai maksimum 92, 6 siswa tuntas, dan 1 siswa belum tuntas. Hasil aktual retest dicatat setelah program dijalankan. Jika seluruh hasil aktual sesuai dengan hasil yang diharapkan, status pengujian dapat dinyatakan Lulus.

## Cara Menjalankan
python3 praktik/main.py

## Refleksi
Teknik debugging yang paling membantu adalah pengujian dengan beberapa test case, terutama nilai batas (boundary testing). Teknik ini membantu menemukan kesalahan yang mungkin tidak terlihat ketika program hanya diuji menggunakan nilai biasa. Contohnya, nilai 60 merupakan batas KKM sehingga perlu diuji secara khusus untuk memastikan operator perbandingan yang digunakan sudah tepat. Selain itu, membaca pesan kesalahan dan memeriksa bagian kode yang berkaitan dengan masalah juga membantu menemukan penyebab bug. Dengan melakukan pengujian sebelum dan sesudah perbaikan, saya dapat memastikan bahwa perubahan kode benar-benar memperbaiki masalah tanpa mengganggu fungsi program lainnya.
