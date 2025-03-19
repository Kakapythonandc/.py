
a = int(input("Masukkan angka pertama: "))
o = input("Masukkan operator: ")
b = int(input("Masukkan angka kedua: "))

hasil = None

if o == "+":
    hasil = a + b
elif o == "-":
    hasil = a - b
elif o == "*":
    hasil = a * b
elif o == "/":
    hasil = a / b
elif o == "//":
    hasil = a // b
elif o == "**":
    hasil = a ** b
elif o == "%":
    hasil = a % b

if hasil == None:
    print("Operator yang dimasukkan salah")
else:
    print("Hasil = " + str(hasil))
