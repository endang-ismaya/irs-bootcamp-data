"""
Loops:
- for in loop
- while loop

continue and break
"""
import cowsay
import random

cowsay.cow("Program Guess Number")
secret_num = random.randint(1, 10) # 9
print(f"cheat code: {secret_num}")

while True:
    num_input = int(input("Coba tebak angka dari 1 - 10: "))

    # jika tebakan benar
    if secret_num == num_input:
        print(f"Selamat! Tebakan anda benar, angkanya adalah: {secret_num}")
        break

    elif num_input > 10:
        cowsay.dragon("Duh Bro... Baca dong! itu diminta 1 sampai 10!!")

    elif num_input > secret_num:
        cowsay.dragon("Aduh bro, angkanya kegedean!")

    elif num_input < secret_num:
        cowsay.dragon("Bro, dikit lagi, kekecilan nih...")


    print("Tebakan anda salah, cobalah lagi. \n\n")
