"""
list (array)
- untuk menyimpan multiple variable di dalam 1 variable
- untuk koleksi data (data structure)
- mutable (kita bisa manipulasi data nya setelah kita buat)
- variable yang disimpan itu bisa heterogen atau homogen
- list memperbolehkan elemen-nya untuk duplikat
- symbol: list
- pake pake [] - square bracket/kurung siku, setiap element dipisah dengan comma ,
"""
list_kosong = []
list_kosong_lagi = list()

print(list_kosong, type(list_kosong))
print(list_kosong_lagi, type(list_kosong_lagi))


# list 1 Dimension
list_heterogen = [1, "dua", 3.0, True, "lima", "dua", 1]
# print(list_heterogen)

list_homogen = [1, 2, 3, 4, 5]
list_homogen2 = ["satu", "dua", "tiga", "empat"]

# List 1 Dimensi
list_1d = [1, 2, 3]

# List 2 Dimensions
list_2d = [
    [1, 2, 3],
    [4, 5, 6]
]

# List 3 Dimensions
list_3d = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]

print(list_1d)
print(list_2d)
print(list_3d)