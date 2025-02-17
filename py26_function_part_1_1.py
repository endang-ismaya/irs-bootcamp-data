"""
Function:
- void : tidak kembalian -> None
- return: ada kembalian
"""
from typing import List


def selamat_pagi() -> None:
    print("Selamat Pagi")


def selamat_pagi_2() -> str:
    return "Selamat Pagi"


sp1 = selamat_pagi()
sp2 = selamat_pagi_2()

# print(sp1) # None
print(f"{sp2.upper()} Ngab!")