# CASE
# Pendataan masukkan nomor HP
# input: 08xxx
# rapihan: +62 8xx

nomor_hp = input("Masukkan Nomor HP (awali dengan +62): ")

if nomor_hp[0] == "0":
    nomor_hp_validated = nomor_hp.replace("0", "+62", count=1)
    print(f"Nomor HP yang sudah di validasi: {nomor_hp_validated}")
else:
    print(f"Nomor HP tidak perlu divalidasi: {nomor_hp}")
