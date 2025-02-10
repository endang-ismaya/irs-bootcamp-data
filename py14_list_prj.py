# Gunakan List irst_team dan huruf_vocal untuk menghasilkan output.
irs_team = [
    "twi alfian",
    "satrio pamungkas",
    "guan sinantin",
    "zaenal abidin",
    "faisal riyadi",
    "abdul roji",
    "taufik nugroho",
    "muhammad fikky",
    "rahmat tulloh",
    "mcd nawval",
    "muhammad arsi",
    "endang ismaya",
    "kurnia wijitomo",
    "wisnu pratama",
    "said najib",
    "agus andiyas",
]
huruf_vokal = ['a', 'i', 'u', 'e', 'o']


# region initial
# irs_team.sort()
# for index, eng in enumerate(irs_team):
#     if index % 2 == 0:
#         first_init = eng.split()[0][0]
#         last_init = eng.split()[1][0]
#         print(f"{index + 1}. {eng} mempunyai initial {first_init}.{last_init}".upper())
#     else:
#         first_init = eng.split()[0][0]
#         last_init = eng.split()[1][0]
#         print(f"{index + 1}. {eng} mempunyai initial {first_init}.{last_init}".lower())
# endregion initial


# region vokal
huruf_vokal = ['a', 'i', 'u', 'e', 'o']

for vokal in huruf_vokal:
    count_vokal = 0
    for eng in irs_team:
        count_vokal += eng.count(vokal)
    
    print(f"Huruf vocal {vokal} di IRS Team ada: {count_vokal}")

# endregion vokal