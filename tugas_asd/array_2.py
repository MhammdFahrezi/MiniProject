import numpy as np

data_angka = []
while True:
    try:
        angka = int(input("Masukkan angka: "))
        data_angka.insert(0, angka)  # Memasukkan angka di awal list
    except ValueError:
        print("Masukan harus berupa angka. Silakan coba lagi.")
        continue
    
    while True:
        pilihan = input("Ingin menambahkan angka lagi? (y/t): ")
        if pilihan.lower() == "y" or pilihan.lower() == "t":                
            break
        else:
            print("Pilihan tidak valid. Masukkan 'y' atau 't'.")
    if pilihan.lower() != "y":
        break

# Memasukkan lebih dari satu angka lagi di akhir
while True:
    angka_tambahan = input("Masukkan satu angka lagi atau ketik 'selesai' jika sudah selesai: ")
    if angka_tambahan.lower() == "selesai":
        break
    try:
        angka_tambahan = int(angka_tambahan)
        data_angka.insert(0, angka_tambahan)  # Memasukkan angka di awal list
    except ValueError:
        print("Masukan harus berupa angka. Silakan coba lagi.")

print("=======================================")
# Tambahkan array dua dimensi
array_2d = np.array(data_angka).reshape(-1, 1)  # Bentuk array dengan dimensi dinamis untuk baris dan satu kolom
print("Array 2D:")
print(array_2d)
