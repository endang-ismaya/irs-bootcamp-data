rogers_team = ["alfian", "satrio", "guan", "taufik"]
voda_team = ["fikky", "rahmat", "nawval", "taufik"]

# rogers_team_str = " & ".join(rogers_team)
# print(rogers_team)
# print(rogers_team_str)

# print("alfian" in rogers_team) # True
# print("alfian" in voda_team) # False
# print("alfian" in rogers_team_str)
# print("alfian" not in voda_team) # True
# print("taufik" in rogers_team or "taufik" in voda_team)
# print("taufik" in voda_team or "taufik" not in rogers_team)
case_1 = "taufik" in voda_team # True
case_2 = "TAUFIK" not in rogers_team # True
print(case_1)
print(case_2)
print(case_1 or case_2)
