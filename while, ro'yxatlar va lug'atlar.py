# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 13:31:46 2026

@author: Honor
"""

buyurtmalar = []
print("Buyurtmalar ro'yxati")
n = 1
while True:
    savol = f"{n}-buyurtmani kiriting:\n>>>"
    buyurtma = input(savol)
    buyurtmalar.append(buyurtma)
    javob = input("Yana buyurtma qo'shasizmi? (ha/yo'q)\n>>>")
    if javob == 'ha':
        n += 1
        continue
    else:
        break
print("Buyurtmalaringiz:")
for buyurtma in buyurtmalar:
    print(buyurtma.title())


ebozor_mahsulotlari = {}
print("ebozor uchun mahsulotlar")
while True:
    savol = "Mahsulot nomini kiriting:"
    mahsulot = input(savol)
    narx = input(f"{mahsulot.title()}ning narxini kiriting:")
    ebozor_mahsulotlari[mahsulot] = int(narx)
    javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q)\n>>>")
    if javob == "ha":
        continue
    else:
        break
print("Mahsulotlar va ularning narxlari:")
for mahsulot,narx in ebozor_mahsulotlari.items():
    print(f"{mahsulot.title()}ning narxi {narx} so'm")


while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in ebozor_mahsulotlari.keys():
        narh = ebozor_mahsulotlari[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")























        