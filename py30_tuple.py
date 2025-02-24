"""
Tuple

- immutable (setelah di buat tidak bisa di modify)
- symbol: tuple
- pakai kurung () -> bracket
- bisa duplicate
- elementnya berurutan
- elementnya bisa heterogen atau homogen
"""

# membuat tuple kosong
rogers = ("faisal", "alfian", "satrio", "guan", "satrio")
voda = ("fikky",)
print(rogers)
print(rogers.count("satrio"))
print(rogers.index("guan"))

# slicing
print(rogers[0:2])

# loop
for eng in rogers:
    print(eng)

# len dari tuple
print(len(rogers))

# list of tuple
irs_team = [
    ("alfian", "rogers", 1),
    ("fikky", "voda", 1),
    ("faisal", "software", 1),
    ("taufik", "rogers", 1),
    ("roji", "voda", 1),
    ("jono", "voda", 0),
]

# sequence unpacking
# list, tuple

for team in irs_team:
    name, team_in, status = team

    # Ternary operator
    status_in = "Available" if status else "Not Available"
    print(f"{name.title()} ada di team {team_in.upper()} statusnya {status_in}")


# casting
# ke list
l_rogers = list(rogers)
print(l_rogers)

# ke set
s_rogers = set(rogers)
print(s_rogers)

# ke dict
irs_team = [
    ("alfian", "rogers"),
    ("fikky", "voda"),
    ("faisal", "software"),
    ("taufik", "rogers"),
    ("taufik", "voda"),
    ("roji", "voda"),
    ("jono", "voda"),
]
d_irs_team = dict(irs_team)
print(d_irs_team)

#
arsi = dict([("arsi", "voda")])
print(arsi)
