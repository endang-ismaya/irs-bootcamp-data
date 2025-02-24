"""
## Falsy Value
- int 0
- float 0.0
- complex 0j
- bool False
- NoneType None
- dict {}
- list []
- tuple ()
- set set()
- range range(0)
- str ""
"""

print(bool([]))
print(bool([1]))

print(bool(""))
print(bool("a"))

print(bool(None))
print(bool(dict()))
print(bool(set()))
print(bool(tuple()))

nama = input("Masukkan nama anda?")
# Ternary Operator
print("Nama anda adalah:", nama) if nama else print("Tolong masukkan nama!")
