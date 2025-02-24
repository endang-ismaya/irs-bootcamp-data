# sequence unpacking
# list
fruits = [
    "apple",
    "banana",
    "coconut",
    "melon",
    "avocado",
    "rambutan",
]
apple, banana, coconut, *others = fruits
print(apple, banana, coconut)
print(others)


# tuple
person = ("abang", 12, "SMP-12", "Tangerang")
nama, usia, sekolah, alamat, *data_lain = person
print(nama, usia, sekolah, alamat)
print(data_lain)
