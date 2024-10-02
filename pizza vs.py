print("------------------------{Selamat Datang Di Pizzalicious!!!}------------------------")
x = print("Halo " + input ("Nama Pemesan:") + "!!")
y = int(input("-------------{Silahkan melakukan pemesanan}-------------\nKetik 1 untuk lanjut ke daftar menu\nKetik 2 untuk batal\n: "))

#Daftar Menu dan Harga
Meat_Lovers_Pizza = 41000
Veggie_Garden = 41000
Super_Supreme = 54000
Pepperoni = 50000
Creamy_Chicken = 62000

#Tampilan Menu
if y == 1:
    print("Daftar Menu:")
    print(f"1. Meat_Lovers_Pizza.........: Rp {Meat_Lovers_Pizza}")
    print(f"2. Veggie_Garden.............: Rp {Veggie_Garden}")
    print(f"3. Super_Supreme.............: Rp {Super_Supreme}")
    print(f"4. Pepperoni.................: Rp {Pepperoni}")
    print(f"5. Creamy_Chicken............: Rp {Creamy_Chicken}")

    z = int(input("Pilih pizza yang anda inginkan: "))

    #Pizza yang Dipilih
    if z == 1:
        harga = Meat_Lovers_Pizza
        print(f"Meat_Lovers_Pizza : Rp {harga}")
    elif z == 2:
        harga = Veggie_Garden
        print(f"Veggie_Garden : Rp {harga}")
    elif z == 3:
        harga = Super_Supreme
        print(f"Super_Supreme : Rp {harga}")
    elif z == 4:
        harga = Pepperoni
        print(f"Pepperoni : Rp {harga}")
    elif z == 5:
        harga = Creamy_Chicken
        print(f"Creamy_Chicken : Rp {harga}")
    else:
        print("MAAF KEYWORD YANG ANDA MASUKKAN TIDAK ADA DI DAFTAR MENU")
        exit()

elif y == 2:
    print("Pemesanan anda dibatalkan... Semoga ada kesempatan di lain waktu!!")
    exit()
else:
    print("MAAF KEYWORD YANG ANDA MASUKKAN SALAH")
    exit()

d = int(input("----------------{Pilih Topping Tambahan}----------------\nKetik 1 untuk lanjut ke daftar topping\nKetik 2 untuk batal\n: "))

#Daftar Topping
Sosis_Sapi = 12000
Pepperoni_Topping = 14000
Paprika = 7000
Jamur = 10000
Bawang_Bombay = 8000
Daging_Sapi = 15000
Daging_Ayam = 13000
Lewati = 0

#Topping Pilihan
if d == 1:
    print("Daftar Topping:")
    print(f"1. Sosis_Sapi..................: Rp {Sosis_Sapi}")
    print(f"2. Pepperoni_Topping...........: Rp {Pepperoni_Topping}")
    print(f"3. Paprika.....................: Rp {Paprika}")
    print(f"4. Jamur.......................: Rp {Jamur}")
    print(f"5. Bawang_Bombay...............: Rp {Bawang_Bombay}")
    print(f"6. Daging_Sapi.................: Rp {Daging_Sapi}")
    print(f"7. Daging_Ayam.................: Rp {Daging_Ayam}")
    print(f"8. Lewati......................: Rp {Lewati}")

    b = int(input("Pilih topping yang anda inginkan: "))

    #Topping yang Dipilih
    if b == 1:
        harga2 = Sosis_Sapi
        print(f"Sosis_Sapi : Rp {harga2}")
    elif b == 2:
        harga2 = Pepperoni_Topping 
        print(f"Pepperoni_Topping : Rp {harga2}")
    elif b == 3:
        harga2 = Paprika
        print(f"Paprika : Rp {harga2}")
    elif b == 4:
        harga2 = Jamur
        print(f"Jamur : Rp {harga2}")
    elif b == 5:
        harga2 = Bawang_Bombay
        print(f"Bawang_Bombay : Rp {harga2}")
    elif b == 6:
        harga2 = Daging_Sapi
        print(f"Daging_Sapi : Rp {harga2}")
    elif b == 7:
        harga2 = Daging_Ayam
        print(f"Daging_Ayam : Rp {harga2}")
    elif b == 8:
        harga2 = Lewati
        print(f"Lewati : Rp {harga2}")
    else:
        print("MAAF KEYWORD YANG ANDA MASUKKAN TIDAK ADA DI DAFTAR MENU")

elif d == 2:
    print("Pemesanan anda dibatalkan... Semoga ada kesempatan di lain waktu!!")
    exit()
else:
    print("MAAF KEYWORD YANG ANDA MASUKKAN SALAH")
    exit()

s = int(input("---------------{Pilih Jenis Crust Pizza}---------------\nKetik 1 untuk lanjut ke pilihan jenis crust pizza\nKetik 2 untuk batal\n: "))

#Jenis Crust Pizza
Thin_Crust = 50000
Thick_Crust = 60000
Stuffed_Crust = 80000
Neapolitan_Crust = 70000

#Crust Pilihan
if s == 1:
    print("Jenis Crust Pizza:")
    print(f"1. Thin_Crust.................: Rp {Thin_Crust}")
    print(f"2. Thick_Crust................: Rp {Thick_Crust}")
    print(f"3. Stuffed_Crust..............: Rp {Stuffed_Crust}")
    print(f"4. Neapolitan_Crust...........: Rp {Neapolitan_Crust}")

    f = int(input("Pilih jenis crust yang anda inginkan: "))

    #Jenis Crust yang Dipilih
    if f == 1:
        harga3 = Thin_Crust
        print(f"Thin_Crust : Rp {harga3}")
    elif f == 2:
        harga3 = Thick_Crust
        print(f"Thick_Crust : Rp {harga3}")
    elif f == 3:
        harga3 = Stuffed_Crust 
        print(f"Stuffed_Crust : Rp {harga3}")
    elif f == 4:
        harga3 = Neapolitan_Crust
        print(f"Neapolitan_Crust : Rp {harga3}")
    else:
        print("MAAF KEYWORD YANG ANDA MASUKKAN TIDAK ADA DI DAFTAR MENU")

elif s == 2:
    print("Pemesanan anda dibatalkan... Semoga ada kesempatan di lain waktu!!")
    exit()
else:
    print("MAAF KEYWORD YANG ANDA MASUKKAN SALAH")
    exit()

j = int(input("-----------------{Ingin Menambah Keju?}-----------------\nKetik 1 jika anda setuju\nKetik 2 untuk melewati\n: "))

#Tambah keju
Ya = 13000
Tidak = 0

#Keputusan
if j == 1:
    print("Apakah anda ingin melanjutkan?")
    print(f"1. Ya    : Rp {Ya}")
    print(f"2. Tidak : Rp {Tidak}")

    k = int(input("Pilihan Anda: "))

    #Tambahan keju
    if k == 1:
        harga4 = Ya
        print(f"Ya : Rp {harga4}")
    elif k == 2:
        harga4 = Tidak
        print(f"Tidak : Rp {harga4}")
    else:
        print("MAAF INPUT TIDAK VALID")
        exit()

elif j == 2:
    harga4 = 0
else:
    print("MAAF KEYWORD YANG ANDA MASUKKAN SALAH")
    exit()

# Total Harga
total_harga = harga + harga2 + harga3 + harga4 
print(f"\nTotal Harga: Rp {total_harga}\nKami sangat menghargai pesanan Anda!\nJangan ragu untuk kembali dan mencoba menu lainnya di Pizzalicious.\nSelamat menikmati!!")