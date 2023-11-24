from tkinter import *
import tkinter.messagebox
from math import floor
from tkinter import ttk

mdl_boneka = 24000
mdl_kereta = 19000
hj_boneka = 27000
hj_kereta = 21000
pft_boneka = hj_boneka - mdl_boneka
pftt_kereta = hj_kereta - mdl_kereta

root = Tk()
root.geometry('865x500')
root.title('Penghitung Keuntungan Maksimum')
root.resizable(width=False, height=False)
root.configure(bg= '#FFB6C1')

f1 = Frame(root, bg='white', width=550, height=550, highlightbackground="green", highlightthickness=2)
f1.grid(column=0, row=0, pady=5, padx=5)

l1 = Label(f1, text="Masukkan Jumlah Kereta", bg='white', font=('Calibri', 14, 'bold'))
l1.grid(column=0, row=0)

entry1 = Entry(f1, width=7)
entry1.grid(column=0, row=1, pady=20, ipadx=30)

l2 = Label(f1, text="Harga Jual Boneka : Rp. 27.000", bg='white', font=('Calibri', 12, 'bold'))
l2.grid(column=0, row=2)
l3 = Label(f1, text="Harga Jual Kereta : Rp. 21.000", bg='white', font=('Calibri', 12, 'bold'))
l3.grid(column=0, row=3)
l3 = Label(f1, text="Modal Boneka: Rp. 24.000", bg='white', font=('Calibri', 12, 'bold'))
l3.grid(column=0, row=4)
l3 = Label(f1, text="Modal Kereta: Rp. 19.000", bg='white', font=('Calibri', 12, 'bold'))
l3.grid(column=0, row=5)
l3 = Label(f1, text="Kendala Batasan Jam Kerja 3X1 + 2X2 = 180", bg='white', font=('Calibri', 12, 'bold'))
l3.grid(column=0, row=6)
l3 = Label(f1, text="Kendala Penjualan Boneka <= 40", bg='white', font=('Calibri', 12, 'bold'))
l3.grid(column=0, row=7)

tree = ttk.Treeview(f1, columns=("Produksi Kereta", "Produksi Boneka", "Total Modal", "Total Pemasukan", "Keuntungan"))
tree.column("#0", width=30, anchor=W)
tree.column("Produksi Kereta", width=100)
tree.column("Produksi Boneka", width=100)
tree.column("Total Modal", width=100)
tree.column("Total Pemasukan", width=100)
tree.column("Keuntungan", width=100)

tree.heading("#0", text="No.", anchor=W)
tree.heading("Produksi Kereta", text="Produksi Kereta", anchor=W)
tree.heading("Produksi Boneka", text="Produksi Boneka", anchor=W)
tree.heading("Total Modal", text="Total Modal", anchor=W)
tree.heading("Total Pemasukan", text="Total Pemasukan", anchor=W)
tree.heading("Keuntungan", text="Keuntungan", anchor=W)
tree.grid(column=1, row=8, padx=10, pady=10, sticky=E+N+W+S)

def klik():
    global x2, x1, K, P, M
    x2 = entry1.get()
    x1 = (180 - (2 * int(x2))) / 3
    x1 = floor(x1)
    if x1 >= 40:
        tkinter.messagebox.showinfo("Peringatan!", "Jumlah produksi boneka maksimal 40")
        x1 = 40

    K = (pft_boneka * int(x1)) + (pftt_kereta * int(x2))
    P = (hj_boneka * int(x1)) + (hj_kereta * int(x2))
    M = (mdl_boneka * int(x1)) + (mdl_kereta * int(x2))

    children = tree.get_children()
    if children:
        last_row = int(tree.index(children[-1]))
    else:
        last_row = -1

    tree.insert("", "end", text=f" {last_row + 2}", values=(x2, x1, M, P, K))
    root.update()

btn1 = Button(f1, text='HITUNG', relief='raised', bg='cyan', font=('Calibri', 12, 'bold'), command=klik)
btn1.grid(column=0, row=8, padx=20, pady=30, sticky=W+E)

root.mainloop()
