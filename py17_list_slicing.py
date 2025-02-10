# LIST SLICING
rogers_team = ["alfian", "satrio", "guan"]

# Menambahkan taufik di rogers_team
rogers_team.append("taufik")
rogers_team.append("roji")
rogers_team.append("wisnu")
rogers_team.append("arsi")
print(rogers_team)

# ["alfian", "satrio", "guan", "taufik", "roji", "wisnu", arsi]
# rogers_team[start_index:stop_index:step]
rogers_team_copy = rogers_team[-1:-4:-1]
print(rogers_team_copy)

# reverse list
rogers_team_reverse = rogers_team[::-1]

# ambil taufik & roji
taufik_dan_roji = rogers_team[3:5]
print(taufik_dan_roji)