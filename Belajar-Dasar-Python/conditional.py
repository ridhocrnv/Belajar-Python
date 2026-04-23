# Conditional Statements / Logic Operators

if (5 < 10):
    print("5 lebih kecil dari 10")


nilai = 85
if (nilai >= 90):
    print("Nilai A")
elif (nilai >= 80):
    print("Nilai B")
elif (nilai >= 70):
    print("Nilai C")
else:
    print("Nilai D")

userNumber = input("Masukkan angka: ")
if (userNumber.isdigit()):
    userNumber = int(userNumber)
    if (userNumber % 2 == 0):
        print("Angka", userNumber, "adalah bilangan genap")
    else:
        print("Angka", userNumber, "adalah bilangan ganjil")
else:
    print("Input bukan angka yang valid")