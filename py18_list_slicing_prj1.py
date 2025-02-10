rogers_team = ["kurnia", "zaenal", "guan", "alfian",  "satrio", "faisal", "najib"]
voda_team = ["wisnu", "fikky", "taufik", "roji", "rahmat", "agus", "nawval", "arsi"]
att_team = ["kurnia", "zaenal", "roji", "faisal"]

# Quiz 05: (point: 35), (presentasi: 45)
# Bikin variable att_and_voda_skills: roji, faisal, zaenal (urutan beda tidak apa-apa)

# Quiz 06: (point: 45), (presentasi: 50)
# tim_warroom: kurnia, zaenal, wisnu, roji, taufik, faisal

# rogers_and_voda_skills = ["taufik", "roji", "alfian", "satrio", "faisal"]
team1 = voda_team[2:4]
team2 = rogers_team[3:6]

# rogers_and_voda_skills = team1 + team2
rogers_and_voda_skills = team1.copy()

print(hex(id(team1)), hex(id(rogers_and_voda_skills)))
rogers_and_voda_skills.extend(team2)

print(f"Team1: {team1}")
print(f"Team2: {team2}")
print(f"rogers_and_voda_skills: {rogers_and_voda_skills}")
