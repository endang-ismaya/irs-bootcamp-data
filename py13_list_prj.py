
# Diberikan list ManagedObject sbb:
mo_list = [
    "GNBCUCPFunction=1,NRCellCU=NRCELLA",
    "GNBCUCPFunction=1,NRCellCU=NRCELLB",
    "GNBCUCPFunction=1,NRCellCU=NRCELLC",
    "GNBCUCPFunction=1,NRCellCU=NRCELLD",
    "GNBCUCPFunction=1,NRCellCU=NRCELLE",
    "GNBCUCPFunction=1,NRCellCU=NRCELLF",
    "GNBCUCPFunction=1,NRCellCU=NRCELLG",
    "GNBCUCPFunction=1,NRCellCU=NRCELLH",
]


# region answer
# print("List NRCellCU:")
# for idx, mo in enumerate(mo_list):
#     print(f"{idx + 1}. {mo.split('=')[-1]}")

nrcellcus = []
for mo in mo_list:
    nrcellcus.append(mo.split('=')[-1])

print("NRCellCU-nya adalah:", " & ".join(nrcellcus))
# endregion answer