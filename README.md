# Praktikum Tkinter Sesi 11 – Pendaftaran Kegiatan Mahasiswa

Nama  : Muhammad Alfa Dinata Pratama
NIM   : 2595114029
Kelas : Teknik Informatika B

## Tujuan
Membangun aplikasi GUI dengan Python Tkinter yang memanfaatkan berbagai widget,
event handling, validasi input, menu, dan dialog (Messagebox dan Toplevel).

## Fitur
- **Entry** untuk nama, **Combobox** untuk program studi, **Radiobutton** untuk jenis kelamin.
- **Checkbutton** untuk memilih kegiatan, dengan **Listbox** yang menampilkan kegiatan terpilih secara langsung.
- **Text** untuk alasan mengikuti kegiatan.
- Tombol **Submit** dan **Reset**.
- **Validasi**: nama, program studi, jenis kelamin, kegiatan, dan alasan tidak boleh kosong.
- **Ringkasan pendaftaran** pada area informasi.
- **Messagebox** untuk notifikasi (berhasil, peringatan validasi, konfirmasi keluar).
- Menu **File** (Submit, Reset, Keluar) dan menu **Bantuan** (Tentang Aplikasi).
- Jendela **About** menggunakan **Toplevel**.
- Event keyboard: **Enter** = Submit, **Esc** = Reset, **Ctrl+Q** = Keluar.
- Tata letak menggunakan **Frame/LabelFrame** dengan **grid** dan **pack**.

## Cara Menjalankan
1. Pastikan Python 3.8+ terpasang (Tkinter sudah termasuk pada instalasi standar Python).
   Pada Linux: `sudo apt install python3-tk`.
2. Jalankan:
   ```
   python main.py
   ```
