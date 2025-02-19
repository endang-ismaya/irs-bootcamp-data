"""
DataType: Dictionary
symbol: dict
- Merupakan tipe data untuk mapping key dengan value-nya
- Termasuk tipe data yang mutable (setelah dibuat bisa di-ubah)
- Key dari Dictionary harus bisa di hash (hashability) - umumnya kita pake string
- Key nya tidak berurutan (un-ordered)
"""

from pprint import pprint

# deklarasi empty dict
dt_irsteam = {}
# print(dt_irsteam)
# print(type(dt_irsteam))

# deklarasi dengan isi
arsi = {
    "first_name": "Muhammad",
    "last_name": "Arsi",
    "age": 20,
    "company": "Yupana",
    "divisi": "RAN",
    "team": "Voda",
}
satrio = {
    "first_name": "Satrio",
    "last_name": "Pamungkas",
    "age": 21,
    "company": "Yupana",
    "divisi": "RAN",
    "team": "Rogers",
}
wisnu = {
    "first_name": "Wisnu",
    "last_name": "Pratama",
    "age": 25,
    "company": "Yupana",
    "divisi": "RAN",
    "team": "Software",
}

# getting value
print(arsi["team"])
print(satrio["team"])
print(wisnu["team"])
if wisnu.get("address") is None:
    print("Wisnu address tidak ada dalam data, coba cari yang lain!")

if "country" not in wisnu.keys():
    print("Wisnu country tidak ada dalam data, coba cari yang lain!")

# assign key and value
wisnu["address"] = "Depok"
if wisnu.get("address") is None:
    print("Wisnu address tidak ada dalam data, coba cari yang lain!")
else:
    print(f"Wisnu address adalah: {wisnu.get('address')}")

# modify yang sudah ada
wisnu["age"] = 26
print(f"Usia Wisnu adalah: {wisnu['age']}")

# print(wisnu.get("country"))
usia = wisnu.get("age", 0)

if usia == 0:
    print("usia tidak ada dalam database")
else:
    print(f"wisnu berusia: {usia} tahun")


# pprint(wisnu)
print("ini code dibawahnya.")

# delete key
if "address" in wisnu.keys():
    del wisnu["address"]

# convert keys and values dari dictionary ke list
pprint(list(wisnu.keys()))
pprint(list(wisnu.values()))

# looping dictionary
for k, v in wisnu.items():
    print(f"Key: {k} | Value: {v}")
