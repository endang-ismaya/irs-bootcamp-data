# Manipulasi String
# Ref: https://www.w3schools.com/python/python_ref_string.asp

# capitalize()
# first_name = input("Enter your first name: ")
# last_name W= input("Enter your last name: ")
# first_name = first_name.capitalize()
# last_name = last_name.capitalize()
# print(f"Your fullname is: {first_name} {last_name}")

# sequence in strings
# name = "Joni Joshua"
# print(name[0:4])

# spill cara untuk nge-loop
# for char in name:
#     print(char)
# cab_nr = "WAVP69"
# cab_lte = "WXLP69"
# cab_gsm = "WXBP69"
# print(cab_nr[1:3])

# upper() & lower()
# print(cab_nr.lower())
# name = "joni joshua"
# print(name.upper())

# replace
# name = "joni joshua joni joni joni"
# print(name.replace("joni", "jono", count=1))

# len() function with strings
# name: str = "joni joshua"
# name_len = len(name)
# print(name_len)
# print(type(name_len))
# print(name_len.upper())


# startswith()
# endswith()
kata = "Selamat Pagi Semua, Kita sekarang belajar Python Strings"

print("startswith()")
print("-" * 40)
print(kata.startswith("Selamat")) # True
print(kata.startswith("Good")) # False
print(kata.startswith("selamat")) # False
print(" " * 40)
print("endswith()")
print("-" * 40)
print(kata.endswith("Strings")) # True
print(kata.endswith("List")) # False

print("*" * 40)
nomor_hp = "0812100100"
print(nomor_hp.startswith("0"))

# comparison string with casefold()
print("*" * 40)
oss_value = "0"
baseline = 0
# Case Sensitive | Case In-Sensitive
hasil = str(oss_value).casefold() == str(baseline).casefold()
print(f"hasil oss_value vs baseline: {hasil}")

# Gold Standard / SRT
# baseline ? oss_value ?