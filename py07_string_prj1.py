"""
Program: Check Cabinet Technology
Desc:
Author: Agus Andiyas
Date: Feb 03, 2025
Requirements:
- User enter the name of the cabinet (DONE)
- Tool get the 1:3 suffix from the cabinet name (DONE)
- Check if suffix "AV" then print NR (DONE)
- Check if suffix "XL" then print LTE (DONE)
- Check if suffix "XB" then print GSM (DONE)
- use cowsay cow, dragon (DONE)
- Check the len of the cabinet name (PENDING)
"""
import cowsay

cowsay.cow("Aplikasi Cabinet NR/LTE/GSM")

cab_name = input("Enter your cabinet name: ")
suffix_cab = cab_name[1:3]

if suffix_cab == "AV":
    cowsay.dragon("Your cabinet is NR Cabinet")
elif suffix_cab == "XL":
    cowsay.dragon("Your cabinet is LTE Cabinet")
elif suffix_cab == "XB":
    cowsay.dragon("Your cabinet is GSM Cabinet")
else:
    cowsay.dragon("Your cabinet is Undetect-able")