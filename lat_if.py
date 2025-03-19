"""
Buat sebuah program yang meminta input sebuah angka.

Ketika angka = 1, tampilkan "Indonesia".
Ketika angka = 2, tampilkan "Singapore".
Ketika angka = 3, tampilkan "Malaysia".
Ketika angka = 4, tampilkan "Brunei".
Selain angka tersebut, maka tampilkan "Input salah".
"""

# buat variabel negara menggunakan angka
negara =  int(input("masukan angka negara :"))

if negara == 1:
    print("indonesia")
elif negara == 2:
    print("singapura")
elif negara == 3:
    print("malaysia")
elif negara == 4:
    print("brunei")
else:
    print("input salah")
