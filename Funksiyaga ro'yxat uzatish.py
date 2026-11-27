# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:12:34 2026

@author: Honor
"""

# def Katta_harf(matnlar):
#     harf = {}
#     while matnlar:
#         matn = matnlar.pop()
#         katta = input(f"{matn.title()}")
#         harf[matn]=katta
#     return harf
# matnlari = ['osh', 'manti', 'xonim', 'shorva']
# harf = Katta_harf(matnlari)
# print(harf)

# def Katta_harf(matnlar):
#     harf = {}
#     while matnlar:
#         matn = matnlar.pop()
#         katta = print(f"{matn.title()}")
#         harf[matn]=katta
#     return harf
# matnlari = ['osh', 'manti', 'xonim', 'shorva']
# harf = Katta_harf(matnlari[:])
# print(harf)
# print(matnlari)

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
            baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
            baholar[ism]=baho
    return baholar
talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)