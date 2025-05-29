# HR Management Payroll System

Sistem HR management payroll sederhana untuk Indonesia (2024). Project ini
menyediakan contoh perhitungan payroll dasar dan penyimpanan data karyawan
menggunakan Python.

## Struktur Project

- `hr_system/` - Paket Python berisi modul karyawan, payroll, database, dan CLI.
- `hr_system/main.py` - Contoh program minimal untuk menghitung payroll satu karyawan.
- `hr_system/cli.py` - Antarmuka baris perintah untuk menambah karyawan, menampilkan
  daftar karyawan, dan memproses payroll.

## Persyaratan

- Python 3.8 atau lebih baru.

## Menjalankan Contoh

Aktifkan environment Python Anda lalu jalankan contoh sederhana:

```bash
python -m hr_system.main
```

## Menggunakan CLI

Untuk menambah karyawan ke basis data JSON dan memproses payroll, gunakan
skrip CLI berikut:

```bash
python -m hr_system.cli add 1 "John Doe" 10000000 1000000 S 0
python -m hr_system.cli list
python -m hr_system.cli payroll
```

Perintah `add` menambahkan karyawan baru, `list` menampilkan seluruh karyawan
yang tersimpan, sedangkan `payroll` menghitung payroll untuk setiap karyawan
pada basis data.

Data karyawan akan disimpan pada berkas `employees.json` di direktori kerja
Anda, sehingga informasi tersebut dapat diproses ulang pada eksekusi berikutnya.
