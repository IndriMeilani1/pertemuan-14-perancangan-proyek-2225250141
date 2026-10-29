
# Test Case Program Rekap dan Analisis Nilai

## TC01 - Data Normal

- Kategori: Normal
- Input: A001,85; A002,78; A003,92
- Hasil yang diharapkan:
  - Jumlah data valid = 3
  - Rata-rata = 85.00
  - Nilai minimum = 78
  - Nilai maksimum = 92
  - Jumlah tuntas = 3
- Status: Lulus jika hasil sesuai.

## TC02 - Nilai Batas Bawah

- Kategori: Batas
- Input: A001,0
- Hasil yang diharapkan:
  - Nilai 0 diterima sebagai data valid.
  - Jumlah tuntas = 0
  - Jumlah belum tuntas = 1
- Status: Lulus jika hasil sesuai.

## TC03 - Nilai Batas Atas

- Kategori: Batas
- Input: A001,100
- Hasil yang diharapkan:
  - Nilai 100 diterima sebagai data valid.
  - Jumlah tuntas = 1
- Status: Lulus jika hasil sesuai.

## TC04 - Nilai di Luar Rentang

- Kategori: Invalid
- Input: A001,105
- Hasil yang diharapkan:
  - Data ditolak karena nilai lebih dari 100.
  - Data invalid dilaporkan.
  - Program tetap berjalan.
- Status: Lulus jika hasil sesuai.

## TC05 - Nilai Bukan Angka

- Kategori: Invalid
- Input: A001,abc
- Hasil yang diharapkan:
  - Data ditolak karena nilai bukan angka.
  - Data invalid dilaporkan.
  - Baris lain yang valid tetap diproses.
- Status: Lulus jika hasil sesuai.

## TC06 - File Tidak Ditemukan

- Kategori: Invalid
- Kondisi: File input tidak tersedia.
- Hasil yang diharapkan:
  - Pesan file tidak ditemukan ditampilkan.
  - Program tidak berhenti karena FileNotFoundError.
  - Laporan tetap dapat dibuat.
- Status: Lulus jika hasil sesuai.

## TC07 - Nilai Sama dengan KKM

- Kategori: Batas
- Input: A001,60
- Hasil yang diharapkan:
  - Nilai 60 diterima.
  - Jumlah tuntas = 1.
  - Jumlah belum tuntas = 0.
- Status: Lulus jika hasil sesuai.

## TC08 - File Kosong atau Semua Data Invalid

- Kategori: Batas/Invalid
- Kondisi: Tidak ada data nilai yang valid.
- Hasil yang diharapkan:
  - Program menampilkan pesan tidak ada data valid.
  - Tidak terjadi pembagian dengan nol.
  - Laporan menjelaskan bahwa tidak ada data valid.
- Status: Lulus jika hasil sesuai.
