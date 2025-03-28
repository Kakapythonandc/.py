a = int(input("masukan angka pertama: "))
b = int(input("masukan angka kedua: "))

'''
in = format dari for
range= untuk meenghasilkan, dimulai dari angka pertama sampai angka kedua.
'''

for i in range(a, b + 1):
    if i % 2 != 0:
        print(i)
