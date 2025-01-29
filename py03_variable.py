# Variable
"""
Fungsi variable
- Menyimpan atau menampung data
- untuk diproses di kode berikutnya

Peraturan penamaan variable
- variable harus pake snake_case
- huruf pertama letter atau underscore
- huruf selanjutnya letter, number, underscore
- huruf capital boleh digunakan untuk constant value
- nama variable harus mencerminkan value-nya
- tidak boleh menggunakan key di python atau builtin function
"""

first_name = "Joni"
last_name = "Jono"
score = 8.5
class_name = 1

first_name = "Abdul"
# print = "mencetak"
print_ = "mencetak"

print(first_name)
# print(type(first_name))
# print(type(last_name))
# print(type(score))
# print(type(class_name))


# string concatenation
print(first_name + " " + last_name + ", score saya " + str(score))
# f-string
print(f"{first_name} {last_name}, dan saya memiliki score = {score}")


# Casting
ini_nomor = "6"
print(ini_nomor, type(ini_nomor))
ini_nomor = int(ini_nomor) # perubahan/convert
print(ini_nomor + 5, type(ini_nomor))

nama = "Bono"
nama = 3.14
print(type(nama))
nama = True
print(type(nama))