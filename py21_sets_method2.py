rogers_team = {
    "kurnia",
    "zaenal",
    "guan",
    "alfian",
    "satrio",
    "faisal",
    "najib",
    "taufik",
    "roji",
}
voda_team = {
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
}
att_team = {"kurnia", "zaenal", "roji", "faisal"}
sw_team = {"faisal", "endang", "wisnu"}

tr_team = {"yusuf", "enes", "osman"}

irs_team = rogers_team.union(voda_team).union(att_team).union(sw_team)
print(irs_team)
print(f"jumlah irs_team: {len(irs_team)}")
print(type(irs_team))

# casting to list
# list(irs_team)
print(voda_team.issubset(irs_team))
print(att_team.issubset(irs_team))
print(rogers_team.issubset(irs_team))
print(tr_team.issubset(irs_team))

print("*" * 40)
print(irs_team.issuperset(rogers_team))
print(irs_team.issuperset(tr_team))

# irisan / intersection
print("*" * 40)
rogers_and_voda_skills = rogers_team.intersection(voda_team)
print(f"rogers_and_voda_skills: {rogers_and_voda_skills}")

# difference
print("*" * 40)
rogers_only = rogers_team.difference(voda_team)
print(f"rogers only skill: {rogers_only}")

voda_only = voda_team.difference(rogers_team)
print(f"voda only skill: {voda_only}")

# symmetric difference
print("*" * 40)
one_man_skill = rogers_team.symmetric_difference(voda_team)
print(f"One man skill: {one_man_skill}")