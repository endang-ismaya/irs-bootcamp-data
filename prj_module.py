def show_title():
    print("*" * 40)
    print("*" * 6, "IRS MEMBER SKILL DETECTION", "*" * 6)
    print("*" * 40)


def show_menu() -> str:
    print("1. Cari nama untuk mendapatkan skills-nya")
    print("2. Cari skill untuk mendapatkan nama engineer-nya")
    print("3. Keluar dari program")
    choice = input("Silahkan pilih menu (1 - 3): ")
    return choice

def goodbye() -> None:
    print("\n")
    print("*" * 55)
    print("*" * 5, "Terima kasih telah menggunakan program Kami.", "*" * 5)
    print("*" * 55)