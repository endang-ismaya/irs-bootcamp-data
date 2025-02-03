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