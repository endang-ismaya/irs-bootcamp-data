"""
String & List
"""

# split()
rogers_team = "Alfian,Guan,Satrio,Taufik,Roji"
print(rogers_team, type(rogers_team)) # str

l_rogers_team = rogers_team.split(',')
print(l_rogers_team, type(l_rogers_team)) # list
l_rogers_team.append("Agus")
print(l_rogers_team)

# join()
print("#".join(l_rogers_team))