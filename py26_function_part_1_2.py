"""
Function
- positional argument
- keyword argumen
"""
# void - tidak return
def selamat_pagi(nama: str, usia: int) -> None:
    """Ini Fungsi untuk mengucapkan selamat Pagi
    
    :param nama: str
    :param usia: int
    """
    usia += 1
    print(f"Selamat Pagi, {nama}. Kamu berusia: {usia} tahun.")

# positional argument
# selamat_pagi("Jojon", 45)
# selamat_pagi(45, "Jojon")

# keyword argument
usia = input("masukkan usia")
selamat_pagi(nama="Jojon", usia=int(usia))
# selamat_pagi(usia=45, nama="Jojon")
