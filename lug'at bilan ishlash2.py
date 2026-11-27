# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:48:18 2026

@author: Honor
"""

#phython_dictionary = {'int':'butun son','float':'onli kasr','string':'matn','if':'agar','else':'yoki'}
#for kalit, qiymat in sorted(phython_dictionary.items()):
#    print(kalit + ' - ' + qiymat)
    
#davlatlar = {'UK':'london','US':'washington','france':'paris','spain':'madrid'}
#print("Mashhur davlatlar:")
#for davlat, poytaxt in sorted(davlatlar.items()):
#    print(davlat.upper())
#print("Yuqoridagi davlarlar poytaxtlari:")
#for davlat, poytaxt in sorted(davlatlar.items()):
#    print(poytaxt.title())

#istalgan_davlat = input('Istalgan davlatni kiriting!\n>>>').lower()
#poytaxt = davlatlar.get(istalgan_davlat)
#if poytaxt==None:
#    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
#else:
#    print(f"{istalgan_davlat.upper()}ning poytaxti {poytaxt.title()} shahri")

restoran_menu = {'osh':40000,'manti':20000,'kabob':12000,'somsa':7000,'norin':35000,'mosh':25000}
print("3 ta taom buyurtma bering!")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())
for buyurtma in buyurtmalar:
    if buyurtma in restoran_menu:
        print(f"{buyurtma.title()} ning narhi {restoran_menu[buyurtma]} so'm ")
    else:
        print("bizda " + (buyurtma.title()) + " yo'q")