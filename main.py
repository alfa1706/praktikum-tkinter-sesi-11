import tkinter as tk
from tkinter import ttk, messagebox

PRODI = [
    "Teknik Informatika",
    "Sistem Informasi",
    "Teknik Elektro",
    "Manajemen",
    "Akuntansi",
    "Pendidikan Bahasa Inggris",
]

KEGIATAN = [
    "Seminar Teknologi",
    "Workshop Python",
    "Lomba Coding",
    "Bakti Sosial",
    "Turnamen Olahraga",
]


class AplikasiPendaftaran:
    def __init__(self, root):
        self.root = root
        self.root.title("Pendaftaran Kegiatan Mahasiswa")
        self.root.geometry("780x640")
        self.root.minsize(740, 600)

        self.var_nama = tk.StringVar()
        self.var_prodi = tk.StringVar()
        self.var_gender = tk.StringVar()          
        self.var_kegiatan = {k: tk.BooleanVar() for k in KEGIATAN}  

        self.buat_menu()
        self.buat_form()
        self.buat_info()

        self.root.bind("<Return>", self.on_enter)
        # Tombol Escape mengosongkan form (fitur tambahan)
        self.root.bind("<Escape>", lambda e: self.reset())

        self.entry_nama.focus_set()

    def buat_menu(self):
        menubar = tk.Menu(self.root)

        # Menu File
        menu_file = tk.Menu(menubar, tearoff=0)
        menu_file.add_command(label="Submit", command=self.submit, accelerator="Enter")
        menu_file.add_command(label="Reset", command=self.reset, accelerator="Esc")
        menu_file.add_separator()
        menu_file.add_command(label="Keluar", command=self.keluar, accelerator="Ctrl+Q")
        menubar.add_cascade(label="File", menu=menu_file)

        # Menu Bantuan -> membuka jendela About
        menu_bantuan = tk.Menu(menubar, tearoff=0)
        menu_bantuan.add_command(label="Tentang Aplikasi", command=self.tampilkan_about)
        menubar.add_cascade(label="Bantuan", menu=menu_bantuan)

        self.root.config(menu=menubar)
        self.root.bind("<Control-q>", lambda e: self.keluar())

    def buat_form(self):
        frame_form = ttk.LabelFrame(self.root, text=" Formulir Pendaftaran ", padding=12)
        frame_form.pack(fill="x", padx=12, pady=(12, 6))
        frame_form.columnconfigure(1, weight=1)

        ttk.Label(frame_form, text="Nama Lengkap").grid(row=0, column=0, sticky="w", pady=4)
        self.entry_nama = ttk.Entry(frame_form, textvariable=self.var_nama)
        self.entry_nama.grid(row=0, column=1, sticky="ew", pady=4, padx=(8, 0))

        ttk.Label(frame_form, text="Program Studi").grid(row=1, column=0, sticky="w", pady=4)
        self.combo_prodi = ttk.Combobox(
            frame_form, textvariable=self.var_prodi, values=PRODI, state="readonly"
        )
        self.combo_prodi.grid(row=1, column=1, sticky="ew", pady=4, padx=(8, 0))
        self.combo_prodi.set("-- Pilih Program Studi --")

        ttk.Label(frame_form, text="Jenis Kelamin").grid(row=2, column=0, sticky="w", pady=4)
        frame_gender = ttk.Frame(frame_form)
        frame_gender.grid(row=2, column=1, sticky="w", pady=4, padx=(8, 0))
        ttk.Radiobutton(frame_gender, text="Laki-laki", value="Laki-laki",
                        variable=self.var_gender).pack(side="left", padx=(0, 16))
        ttk.Radiobutton(frame_gender, text="Perempuan", value="Perempuan",
                        variable=self.var_gender).pack(side="left")

        ttk.Label(frame_form, text="Pilih Kegiatan").grid(row=3, column=0, sticky="nw", pady=4)
        frame_kegiatan = ttk.Frame(frame_form)
        frame_kegiatan.grid(row=3, column=1, sticky="ew", pady=4, padx=(8, 0))
        frame_kegiatan.columnconfigure(1, weight=1)

        frame_cek = ttk.Frame(frame_kegiatan)
        frame_cek.grid(row=0, column=0, sticky="nw")
        for k in KEGIATAN:
            ttk.Checkbutton(
                frame_cek, text=k, variable=self.var_kegiatan[k],
                command=self.update_listbox,          
            ).pack(anchor="w")

        # Kolom kanan: Listbox berisi kegiatan yang dipilih
        frame_lb = ttk.LabelFrame(frame_kegiatan, text=" Kegiatan Terpilih ", padding=4)
        frame_lb.grid(row=0, column=1, sticky="nsew", padx=(16, 0))
        self.listbox = tk.Listbox(frame_lb, height=5, activestyle="none")
        self.listbox.pack(fill="both", expand=True)

        ttk.Label(frame_form, text="Alasan Mengikuti").grid(row=4, column=0, sticky="nw", pady=4)
        frame_alasan = ttk.Frame(frame_form)
        frame_alasan.grid(row=4, column=1, sticky="ew", pady=4, padx=(8, 0))
        frame_alasan.columnconfigure(0, weight=1)
        self.text_alasan = tk.Text(frame_alasan, height=4, wrap="word")
        self.text_alasan.grid(row=0, column=0, sticky="ew")
        scroll = ttk.Scrollbar(frame_alasan, command=self.text_alasan.yview)
        scroll.grid(row=0, column=1, sticky="ns")
        self.text_alasan.config(yscrollcommand=scroll.set)

        frame_tombol = ttk.Frame(frame_form)
        frame_tombol.grid(row=5, column=0, columnspan=2, pady=(10, 0))
        ttk.Button(frame_tombol, text="Submit", width=14, command=self.submit).pack(side="left", padx=6)
        ttk.Button(frame_tombol, text="Reset", width=14, command=self.reset).pack(side="left", padx=6)

    def buat_info(self):
        frame_info = ttk.LabelFrame(self.root, text=" Ringkasan Pendaftaran ", padding=8)
        frame_info.pack(fill="both", expand=True, padx=12, pady=(6, 12))

        self.text_info = tk.Text(frame_info, height=8, wrap="word", state="disabled",
                                 background="#f5f5f5")
        self.text_info.pack(side="left", fill="both", expand=True)
        scroll = ttk.Scrollbar(frame_info, command=self.text_info.yview)
        scroll.pack(side="right", fill="y")
        self.text_info.config(yscrollcommand=scroll.set)

        self.tulis_info("Belum ada data pendaftaran.\nIsi formulir lalu tekan Submit atau Enter.")

    def tulis_info(self, teks):
        """Menulis teks ke area informasi (Text read-only)."""
        self.text_info.config(state="normal")
        self.text_info.delete("1.0", "end")
        self.text_info.insert("1.0", teks)
        self.text_info.config(state="disabled")

    def kegiatan_terpilih(self):
        return [k for k, v in self.var_kegiatan.items() if v.get()]

    def update_listbox(self):
        """Dipanggil setiap Checkbutton berubah -> Listbox ikut diperbarui."""
        self.listbox.delete(0, "end")
        for k in self.kegiatan_terpilih():
            self.listbox.insert("end", k)

    def on_enter(self, event):
        if isinstance(event.widget, tk.Text):
            return
        self.submit()

    def validasi(self):
        """Mengembalikan pesan error (str) atau None bila semua valid."""
        if not self.var_nama.get().strip():
            self.entry_nama.focus_set()
            return "Nama tidak boleh kosong."
        if self.var_prodi.get() not in PRODI:
            self.combo_prodi.focus_set()
            return "Silakan pilih program studi."
        if not self.var_gender.get():
            return "Silakan pilih jenis kelamin."
        if not self.kegiatan_terpilih():
            return "Pilih minimal satu kegiatan."
        if not self.text_alasan.get("1.0", "end").strip():
            self.text_alasan.focus_set()
            return "Alasan mengikuti kegiatan tidak boleh kosong."
        return None

    def submit(self):
        error = self.validasi()
        if error:
            messagebox.showwarning("Validasi Gagal", error)
            return

        nama = self.var_nama.get().strip()
        prodi = self.var_prodi.get()
        gender = self.var_gender.get()
        daftar = self.kegiatan_terpilih()
        alasan = self.text_alasan.get("1.0", "end").strip()

        ringkasan = (
            "=== DATA PENDAFTARAN ===\n"
            f"Nama           : {nama}\n"
            f"Program Studi  : {prodi}\n"
            f"Jenis Kelamin  : {gender}\n"
            f"Kegiatan       : {', '.join(daftar)}\n"
            f"Alasan         : {alasan}\n"
        )
        self.tulis_info(ringkasan)
        messagebox.showinfo("Berhasil", f"Pendaftaran atas nama {nama} berhasil disimpan!")

    def reset(self):
        self.var_nama.set("")
        self.combo_prodi.set("-- Pilih Program Studi --")
        self.var_gender.set("")
        for v in self.var_kegiatan.values():
            v.set(False)
        self.update_listbox()
        self.text_alasan.delete("1.0", "end")
        self.tulis_info("Form telah direset.\nIsi formulir lalu tekan Submit atau Enter.")
        self.entry_nama.focus_set()

    def keluar(self):
        if messagebox.askyesno("Keluar", "Yakin ingin menutup aplikasi?"):
            self.root.destroy()

    def tampilkan_about(self):
        win = tk.Toplevel(self.root)
        win.title("Tentang Aplikasi")
        win.geometry("340x210")
        win.resizable(False, False)
        win.transient(self.root)   
        win.grab_set()             

        ttk.Label(win, text="Pendaftaran Kegiatan Mahasiswa",
                  font=("Segoe UI", 13, "bold")).pack(pady=(20, 4))
        ttk.Label(win, text="Versi 1.0").pack()
        ttk.Label(win, text="Praktikum Tkinter - Sesi 11\nAdvanced Widgets dan Event Handling",
                  justify="center").pack(pady=10)
        ttk.Label(win, text="Dibuat oleh: Muhammad Alfa Dinata Pratama - 2595114029").pack()
        ttk.Button(win, text="Tutup", command=win.destroy).pack(pady=14)


if __name__ == "__main__":
    root = tk.Tk()
    AplikasiPendaftaran(root)
    root.mainloop()