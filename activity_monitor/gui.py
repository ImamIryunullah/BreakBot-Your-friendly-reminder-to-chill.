import tkinter as tk
from tkinter import messagebox

def get_user_setting():
    def on_submit():
        try:
            minutes = int(entry.get())
            if minutes <= 0:
                raise ValueError
            root.quit()
            root.destroy()
            callback(minutes * 60)
        except ValueError:
            messagebox.showerror("Input Salah Ngabss", "Masukkan angka menit yang valid dongsss!")

    def callback(seconds):
        global user_setting
        user_setting = seconds

    root = tk.Tk()
    root.title("Pengaturan Waktu Istirahat")

    tk.Label(root, text="Masukkan waktu aktif (menit):").pack(padx=10, pady=5)
    entry = tk.Entry(root)
    entry.insert(0, "45")
    entry.pack(padx=10, pady=5)

    tk.Button(root, text="Mulai", command=on_submit).pack(pady=10)
    root.mainloop()

    return user_setting
