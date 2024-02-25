#arry satu dimensi 

from prettytable import PrettyTable
import numpy as np

data_angka = []
while True:
    try:
        angka = int(input("Masukkan angka: "))
        data_angka.append(angka)
    except ValueError:
        print("Masukan harus berupa angka. Silakan coba lagi.")
        continue
    
    tambah_lagi = input("Ingin menambahkan angka lagi? (y/t): ")
    if tambah_lagi.lower() == "t":
        break
print("=======================================")
# Tambahkan array list
list = np.array(data_angka)
print("angka_List:", list)
print("==============table==============")
table = PrettyTable()
table.field_names = ["No", "Angka"]
for i, angka in enumerate(data_angka, start=1):
    table.add_row([i, angka])
print(table)

