print("Selamat datang di aplikasi penghitung volume bangun ruang!")
print("=" * 30)
print("Menu Utama\n")
print("=" * 30)
while True:
    print("\nPilih bangun ruang untuk menghitung volume:")
    print("1. Balok")
    print("2. Prisma")
    print("3. Bola")
    print("4. Keluar")
    pilihan_bangun = int(input("Masukkan pilihan (1/2/3/4): "))
    if pilihan_bangun == 1:
        print("\nMenu Hitung Volume Balok")
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        volume = panjang * lebar * tinggi
        print(f"\nVolume balok adalah {volume}")
    elif pilihan_bangun == 2:
        print("\nMenu Hitung Volume Prisma")
        alas = float(input("Masukkan alas prisma: "))
        tinggi_prisma = float(input("Masukkan tinggi prisma: "))
        volume = 0.5 * alas * tinggi_prisma
        print(f"\nVolume prisma adalah {volume}")
    elif pilihan_bangun == 3:
        print("\nMenu Hitung Volume Bola")
        jari_jari = float(input("Masukkan jari-jari bola: "))
        volume = (4/3) * 3.14 * (jari_jari ** 3)
        print(f"\nVolume bola adalah {volume}")
    elif pilihan_bangun == 4:
        print("\nTerima kasih telah menggunakan program ini. Sampai jumpa lagi!")
        break
    else:
        print("Pilihan tidak valid.")
