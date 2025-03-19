
# Buat program ketika umur kurang dari 18:
# Anak-anak
#
# Ketika umur 18 - 25:
# Remaja
#
# Ketika umur di atas 26-30:
# Dewasa
#
# Ketika umur 30 ke atas:
# Tua

umur = int(input("Masukkan umur: "))

if umur < 0:
    print("Umur yang dimasukkan salah")
elif umur < 18:
    print("Anak-anak")
elif umur <= 25:
    print("Remaja")
elif umur <= 30:
    print("dewasa")
else:
    print("tua")
