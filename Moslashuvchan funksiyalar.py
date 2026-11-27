# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:44:19 2026

@author: Honor
"""
# def kopaytma(*sonlar):
#     """Kiritilgan sonlar ko'paytmasini hisoblaydigan funksiya"""
#     yigindi = 1
#     for son in sonlar:
#         yigindi *= son
#     return yigindi
# kopaytma(1,2,3,4,5)

def talaba_malumot(ismi, familiyasi, **malumotlar):
    """Talaba haqidagi ma'lumotlarni lug'at ko'rinishida chiqaruvchi funksiya"""
    malumotlar['ismi']=ismi
    malumotlar['familiyasi']=familiyasi
    return malumotlar
talaba_malumot('Mansurbek', 'Saporbayev', yoshi='18', kursi='1-kurs', universiteti='WIUT')