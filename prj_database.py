from pprint import pprint


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

# irs_team = {"rogers": rogers_team, "voda": voda_team, "att": att_team, "sw": sw_team}

dt_eng_skills = dict()

# 1. rogers
for eng in rogers_team:
    dt_eng_skills[eng] = ["Rogers"]

# print(dt_eng_skills)

# 2. voda
for eng in voda_team:
    # print(eng)

    # kita cek si engineer ada apa ngga di dict key vs skills (dt_eng_skills)
    if eng in dt_eng_skills.keys():
        # mengambil skill dari dt_eng_skills berdasarkan engineer
        # skills merupakan list
        # skills = dt_eng_skills[eng]  # ["Rogers"]

        # kita tambahkan skill si engineer dengan voda
        # dengan metode append langsung
        dt_eng_skills[eng].append("Voda")
        # kita tambahkan skillnya dengan voda
        # skills += ", Voda"

        # kita assign si engineer dengan skill yang baru di dt_eng_skills
        # dt_eng_skills[eng] = skills

    # # klo engineernya blum ada di dt_eng_skills
    else:
        dt_eng_skills[eng] = ["Voda"]


# 3. att
# 4. sw
# 5. tr ix
