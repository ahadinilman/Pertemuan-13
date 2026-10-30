# Pertemuan 13 - Debugging dan Testing

Nama: Ahadin Ilman
NIM: 22252520220
Kelas: 3A

## Kasus
Program memproses data nilai mahasiswa yang mencakup perhitungan rata-rata, penentuan status kelulusan, dan pencarian nilai tertinggi[cite: 9].

## Test Case
| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| T1 | [80, 60, 90, 70] | 75.0 | 60.0 | FAIL |
| T2 | [100, 80] | 90.0 | 36.0 | FAIL |
| T3 | 60 | Lulus | Tidak lulus | FAIL |
| T4 | 59 | Tidak lulus | Tidak lulus | PASS |
| T5 | [80, 60, 90, 70] | 90 | 0 | FAIL |

## Bug Report
* **Bug 1 (Rata-rata):** Pembagi pada fungsi `hitung_rata_rata` menggunakan angka statis `5`, sehingga hasil salah jika jumlah elemen list tidak sama dengan lima. Perbaikan dilakukan dengan membagi total nilai dengan `len(nilai)`.
* **Bug 2 (Status):** Operator perbandingan pada fungsi `status` menggunakan `>` alih-alih `>=`, sehingga nilai tepat 60 dianggap tidak lulus. Perbaikan dilakukan dengan mengubah operator menjadi `>=`.
* **Bug 3 (Nilai Tertinggi):** Inisialisasi variabel `tertinggi` diset ke `0` dan arah perbandingan salah (`<`), sehingga mengabaikan nilai positif dan salah membandingkan. Perbaikan dilakukan dengan menginisialisasi `tertinggi` ke elemen pertama list dan membalik operator menjadi `>`.

## Retest
Seluruh test case (T1 sampai T5) berhasil diuji ulang dan menghasilkan status **PASS** tanpa adanya regresi pada bagian lain.

## Cara Menjalankan
python3 praktik/praktik_4_debugging.py

## Refleksi
Teknik debugging yang paling membantu adalah penggunaan breakpoint dan pengujian dengan test case batas karena memberikan bukti konkret dan langsung menunjuk pada lokasi akar permasalahan logika.