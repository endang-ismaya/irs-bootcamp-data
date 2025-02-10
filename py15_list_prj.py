mo = "GNBCUCPFunction=1,NRCellCU=NRCELLA"
mo_1 = "CarrierAggregation=1,CaCellMeasProfile=Rogers,CaCellMeasProfileUeCfg=Base"

# print(mo.split(','))

mo_list = mo.split('=')
nrcell = mo_list[-1]

print(nrcell)
print(mo.split('=')[-1])