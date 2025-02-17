"""
Function
- Merupakan sekumpulan kode yang bisa kita gunakan beberapa kali
    DRY (Dont Repeat Yourself)
- Definisinya menggunakan keyword 'def'
- Merupakan sebuah object
- Indentasi hal yang sangat penting di function
- Untuk menggunakan-nya si function harus dipanggil/call
- Rekomendasi:
    - Nama fungsi harus menjelaskan isi-nya
    - Kalau bisa hanya menjalankan 1 misi/tujuan
    - Direkomendasikan tidak merubah external object/variabel diluar fungsi itu sendiri
"""

# You're repeating yourself
def show_title():
    print("*" * 35)
print("-" * 35)
print("**", "SAYA SUKA BELAJAR PYTHON", "**")
print("-" * 35)
print("*" * 35)


i = 0
while i <= 10:
    show_title()

    i += 1