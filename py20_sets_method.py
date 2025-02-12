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
att_team = ["kurnia", "zaenal", "roji", "faisal"]
sw_team = ["faisal", "endang", "wisnu"]

irs_team = rogers_team.copy()
irs_team.extend(voda_team)
irs_team.extend(att_team)
irs_team.extend(sw_team)
irs_team.sort()

irs_team = set(irs_team)
print(irs_team)

