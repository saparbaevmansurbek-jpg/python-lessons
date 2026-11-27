# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:31:11 2026

@author: Honor
"""

ismlar = ['Diyor', 'Mirjahon', 'Amirxon', 'Bexruz','Jamshid']
for friends in ismlar:
    print(f"Assalomu alaykum, {friends}, Sahifamizga hush kelibsiz!")
print(f"Kod {len(ismlar)} marta takrorlandi")
sonlar = list(range(11,100,2))
for son in sonlar:
    print(son**3)
kinolar = []
print("5 ta eng sevimli kinolaringizni kiriting?")
for n in range(1,6):
    kinolar.append(input(f"{n} Kinolaringizni kiriting."))
print(kinolar)
odamlar = []
for n in range(100):
    odamlar.append(input(f"{n+1} Bugun suhbatlashgan odamlaringizni nomini kiriting."))
print(odamlar)
