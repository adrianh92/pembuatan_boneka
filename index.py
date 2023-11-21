import os

if __name__ == "__main__":
    sistem_operasi= os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
        


print("Program Optimasi Pembuatan Boneka")
print("==================================")

# x = jumlah boneka yang diproduksi setiap minggu

print("input jumlah boneka:")
x = int(input())
x2 = x * 2
p = (27000 * x - (10000+14000) * x)

# z = total pemasukan
z = 3000 * x - (10000 + 14000) * x

if x2 <= 100 :
    if x <= 80 :
        if x <= 40 :
            if x >= 0 :
                print (p)
            else:
                print("jumlah boneka tidak dapat negatif")
        else:
            print("jumlah penjualan boneka terlalu banyak. Kurangi jumlah boneka")
    else:
        print("jam pekerjaan kayu terlalu banyak. Kurangi jumlah boneka")
else:
    print("jam pemolesan terlalu banyak. Kurangi jumlah boneka")

print(f"pemasukan {z} dan keuntungan {p}")

