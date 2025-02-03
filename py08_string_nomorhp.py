# CASE
# Pendataan masukkan nomor HP
# Requirements:
# - input: 08xxx (DONE)
# - rapihkan: +62 8xx (DONE)
# - push si user untuk memasukkan only DIGIT (DONE)
# - check if nomor_hp >= 11 dan tidak lebih besar samadengan 14 (DONE)
# - check if user enter char aneh !@#$%%&^*() (PENDING)

nomor_hp = input("Masukkan Nomor HP (awali dengan 0): ")

# check jika nomor_hp tidak digit
if not nomor_hp.isdigit():
    print("Maaf, Anda hanya boleh memasukkan digit, diawali dengan 0")


else: # check jika nomor hp adalah digit
    panjang_nomor_hp = len(nomor_hp)
    if panjang_nomor_hp >= 11 and panjang_nomor_hp <= 14:
        if nomor_hp[0] == "0":
            nomor_hp_validated = nomor_hp.replace("0", "+62", count=1)
            print(f"Nomor HP yang sudah di validasi: {nomor_hp_validated}")
        else:
            print("Nomor HP harus diawali dengan angka 0")
    else:
        print("Nomor HP harus minimal 11 Digit dan maksimal 14 Digit")
