"""
Sets

Karakteristik dari Set:
- Unordered
- Unique elements
- Mutable
- Biasanya object element sama (homogen)
"""

rogers_team = [
    "kurnia",
    "zaenal",
    "guan",
    "alfian",
    "satrio",
    "faisal",
    "najib",
    "taufik",
    "roji",
]
voda_team = [
    "wisnu",
    "fikky",
    "taufik",
    "roji",
    "rahmat",
    "agus",
    "nawval",
    "arsi",
    "alfian",
    "satrio",
    "faisal",
]
# att_team = ["kurnia", "zaenal", "roji", "faisal"]
# print(rogers_team)
# print(voda_team)
# rogers_voda = rogers_team.copy()
# rogers_voda.extend(voda_team)
# rogers_voda.sort()
# print(rogers_voda)
# print(len(rogers_voda))

# print()
# print("*" * 30)
# print()
# rogers_voda_set = set(rogers_voda)
# print(rogers_voda_set)
# print(len(rogers_voda_set))
# print(type(rogers_voda_set))

# initial set (kosong)
# rogers_team = set()
# print(type(rogers_team))

rogers_team = {"alfian", "guan", "satrio", "roji"}
print(f"original: {rogers_team}")

# tambah element add()
rogers_team.add("taufik")
print(f"rogers_team_2: {rogers_team}")

# remove semua elemen clear()
# rogers_team.clear()
# print(f"rogers_clear: {rogers_team}")

# discard() and remove()
rogers_team.discard("fikky")
# rogers_team.remove("fikky") --> ini akan error jika 'fikky' tidak ada element-nya
print(f"roji removed: {rogers_team}")

try:
    rogers_team.remove("Satrio")
except KeyError:
    print("Maaf, Om Satrio memang sudah tidak ada dari awal!")

