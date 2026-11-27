# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 14:16:45 2026

@author: Honor
"""

def yosh_hisobla(ism, tugilgan_yili):
    """Foydalanuvchini ismi va tug'ilgan yilini so'rab, yoshini hisoblaydigan funksiya"""
    print(f"{ism.title()} {2026-tugilgan_yili} yoshda")
yosh_hisobla('Mansur', 2008)

def kub_kvadrat(son):
    """Foydalanuvchidan biror son so'rab, o'sha sonning kvadrati va kubini chiqaruvchi funksiya"""
    print(f"{son} ning kvadrati {son**2} ga, {son} ning kubi {son**3} ga teng")
kub_kvadrat(12)

def juft_toq(soon):
    """Foydalanuvchidan biror son so'rab, o'sha sonning juft yoki toqligini chiqaruvchi funksiya"""
    if soon == 0:
        print(f"{soon} juft ham, toq ham emas")
    elif soon % 2 == 1:
        print(f"{soon} toq son ekan")
    elif soon % 2 == 0:
        print(f"{soon} juft son ekan")
juft_toq(11)
juft_toq(14)
juft_toq(0)

def katta_kichik(son1, son2):
    """Foydalanuvchidan biror 2 ta son so'rab, ularning kattasini chiqaruvchi, agar ikkalasi ham teng bo'lsa 'Sonlar teng' degan habar chiqaruvchi dastur"""
    if son1>son2:
        print(f"{son1}")
    elif son2>son1:
        print(f"{son2}")
    elif son1==son2:
        print("Sonlar teng")
katta_kichik(13, 16)
katta_kichik(29, 11)
katta_kichik(20, 20)

def misol(x, y):
    """Foydalanuvchidan biror 2 ta son so'rab, ularni qo'shilmasini chiqaruvchi dastur"""
    print(f"{x+y}")
misol(2, 34)

def qoldiq(son3):
    """Foydalanuvchidan biror son so'rab, o'sha sonning 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshirib chiqaruvchi dastur"""
    for i in range(2, 10):
        if son3 % i == 0:
            print(f"{son3} {i} ga qoldiqsiz bo'linadi")
        else:
            print(f"{son3} 2 dan 10 gacha sonlarga qoldiqsiz bo'linmaydi")
qoldiq(2520)
qoldiq(73)

















