from tkinter import *
from math import floor
import matplotlib.pyplot as plt
#x1 = Jumlah produksi boneka
#x2 = Jumlah produksi kereta
#P = Total pemasukan
#M = Total modal
#K = Keuntungan
#
#Modal boneka = 24000
#Modal kereta = 19000
#Harga jual boneka = 27000
#Harga jual kereta = 21000
#Biaya material boneka = 10000
#Biaya material kereta = 9000
#Biaya tenaga kerja = 14000

root = Tk()
root.geometry ('600x310')
root.title('Penghitung Keuntungan Maksimum')
root.resizable(width = False, height = False)
root.configure(bg='blue')

f1 = Frame(root, bg='white', width=550, height=550,highlightbackground="green", highlightthickness=2)
f1.grid(column=0, row=0, pady=5, padx=5)

c1 = Canvas(root, width = 400, height=300, bg='red')
c1.grid(column = 1, row=0, padx =10, pady=10, sticky=E+N+W+S)

t1 = Text(c1, bg='yellow', height = 5, width = 40, font=('Times', 12))
t1.grid(column=0, row=0, padx=5, pady=5, sticky =E+N+S+W)



l1= Label(f1, text="Masukkan Jumlah Kereta", bg='purple')
l1.grid(column=0, row=0)

entry1 = Entry(f1, width=7)
entry1.grid(column =0, row=1,pady=20, ipadx=30)


l2= Label(f1, text="Harga Jual Boneka : Rp. 27.000", bg='yellow')
l2.grid(column=0, row=2)
l3= Label(f1, text="Harga Jual Kereta : Rp. 21.000", bg='white')
l3.grid(column=0, row=3)
l3= Label(f1, text="Modal Boneka: Rp. 24.000", bg='green')
l3.grid(column=0, row=4)
l3= Label(f1, text="Modal Kereta: Rp. 19.000", bg='blue')
l3.grid(column=0, row=5)
l3= Label(f1, text="Kendala Batasan Jam Kerja 3X1 + 2X2 = 180", bg='brown')
l3.grid(column=0, row=6)
l3= Label(f1, text="Kendala Penjualan Boneka <= 40", bg='cyan')
l3.grid(column=0, row=7)



def klik():
    global x2, x1, K, P, M, fig,y
    x2 = entry1.get()
    t1.delete("1.0","end")
    # t1.insert("1.0", x2)
    #batasan 
    x1 = (180 - (2 * int(x2))) / 3
    x1 = floor(x1)
    if (x1 >= 40):
        x1 = 40
    K = (3000 * int(x1)) + (2000 * int(x2) ) 
    P =(27000 * int(x1)) + (24000*int(x2))
    M = (24000 * int(x1)) + (19000*int(x2))
    t1.insert(END, "Jumlah Produksi Kereta : "+str(x2)+"\n")
    t1.insert(END, "Jumlah Produksi Boneka : "+str(x1)+"\n")
    t1.insert(END, "Total Modal: "+str(M)+"\n")
    t1.insert(END, "Total Pemasukan: "+str(P)+"\n")
    t1.insert(END, "Dengan Keuntungan: "+str(K)+"\n")

    x = (K - int(x2) * 2000) / 3000
    y = (K - int(x1)* 3000) / 2000

    plt.clf()
    x, y = [x, 0], [0 , y]
    plt.plot(x, y, marker = 'o')
    plt.xlabel("Boneka")
    plt.ylabel("Kereta")
    plt.show()

    # t1.insert('1.0',str(entry1)+'\n')
    root.update()

btn1= Button(f1, text='HITUNG', relief= 'raised',bg='red', command=klik)
btn1.grid(column =0, row=8, padx=20, pady=30,  sticky =W+E )

          
root.mainloop()