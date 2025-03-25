a = int(input("masukan angka pertama: "))
b = int(input("masukan angka kedua: "))

i = a
while i <= b:
    if i % 2 == 0:
        print(i)
    i += 1
