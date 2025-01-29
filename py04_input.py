import cowsay

nama = input("Masukkan nama: ")
age = input("Masukkan umur: ")
# print("type age: ", type(age))

# Control Flow / Conditional Statement
if int(age) >= 18:
    cowsay.dragon(f"oh saya baru tau, klo {nama}, itu umurnya {age}, dan udah bisa nyoblos.")
elif int(age) >= 25:
    print("apa")
else:
    cowsay.cow(f"oh saya baru tau klo {nama}, itu masih bocil!")