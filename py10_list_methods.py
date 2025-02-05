"""
List Methods

* append()	Adds an element at the end of the list
* clear()	Removes all the elements from the list
* copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
* extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
* insert()	Adds an element at the specified position
* pop()	Removes the element at the specified position
* remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""
rogers_team = []
voda_team = ["Fikky", "Rahmat"]

# original
print("(PRE) rogers: ", rogers_team)
print("(PRE) voda: ", rogers_team)
print("*" * 55)

# appends
rogers_team.append("Guan")
rogers_team.append("Satrio")

# insert
rogers_team.insert(0, "Alfian")
rogers_team.insert(1, "Abdul Roji")

# clear()
rogers_team.clear()

# 
rogers_team = ["Alfian", "Abdul Roji", "Guan", "Satrio", "Taufik"]

# taufik dibutuhkan di voda
taufik = rogers_team.pop()
voda_team.append(taufik)

# voda butuh lagi buat IX
abdul_roji = rogers_team.remove("Abdul Roji")
print("abdul roji", abdul_roji)
voda_team.append("Abdul Roji")
# ambil posisi
# engineer = rogers_team[0]
# print(f"Siapakah ini: {engineer}")

# liat jumlah rogers_team skr
# print(f"Jumlah rogers team skr: {len(rogers_team)}")

# iterasi 1 per 1
# kita pakai loop, for in loop
# for engineer in rogers_team:
#     print(f"--- {engineer}")

# latest status
print("*" * 55)
print("(POST) rogers: ", rogers_team, " Dengan Jumlah", len(rogers_team))
print("(POST) voda: ", voda_team, "Dengan Jumlah ", len(voda_team))

irs_team = rogers_team.copy()
irs_team.extend(voda_team)
print(f"irs team: {irs_team}")

