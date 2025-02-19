from prj_module import show_menu, show_title, goodbye
from prj_database import att_team, rogers_team, sw_team, tr_team, voda_team

# convert list into string
rogers_team_str = ",".join(rogers_team)
voda_team_str = ",".join(voda_team)
att_team_str = ",".join(att_team)
sw_team_str = ",".join(sw_team)
tr_team_str = ",".join(tr_team)

show_title()

while True:
    choice = show_menu()

    if choice.casefold() == "3".casefold():
        goodbye()
        break

    if choice.casefold() == "1":
        name = input("Masukan nama engineer yang ingin diketahui skillnya (x untuk kembali ke menu): ")

        skills  = []
        # exit
        if name.casefold() == "X".casefold():
            print("\n\n\n")
            continue
        # check rogers
        if name.casefold() in rogers_team_str.casefold():
            skills.append("Rogers")
        # check voda
        if name.casefold() in voda_team_str.casefold():
            skills.append("Voda")
        # check att
        if name.casefold() in att_team_str.casefold():
            skills.append("AT&T")
        # check sw
        if name.casefold() in sw_team_str.casefold():
            skills.append("SW")
        # check tr
        if name.casefold() in tr_team_str.casefold():
            skills.append("Bahasa Turki")
        
        if skills:
            skills_join = ', '.join(skills)
            print(f"{name.capitalize()} memiliki {len(skills)} skills: {skills_join}")
            print("\n")
        else:
            print(f"{name} tidak dikenal, mohon masukkan nama lain.")
            print("\n")
    elif choice.casefold() == "2".casefold():
        print("Maaf program masih belum ready :D ")
        print("\n")










