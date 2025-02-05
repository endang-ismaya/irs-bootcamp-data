team = input("Masukkan nama team, pisahkan dengan comma: ")

l_team = team.split(',')
for index, eng in enumerate(l_team):
    print(f"Welcome {eng}, kamu menjadi anggota ke-{index + 1}")


