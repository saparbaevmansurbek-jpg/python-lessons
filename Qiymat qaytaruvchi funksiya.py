# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 12:30:23 2026

@author: Honor
"""

# def malumotnoma(ismi, familiyasi, tugilgan_yili, email_manzili="", tel_raqami=""):
#     malumot = {'Ism' : ismi,
#                'familiya' : familiyasi,
#                'tugilgan yili' : tugilgan_yili,
#                'yoshi' : 2026-tugilgan_yili,
#                'email manzili' : email_manzili,
#                'telefon raqami' : tel_raqami}
#     return malumot

# def malumotnoma(ismi, familiyasi, tugilgan_yili, email_manzili="", tel_raqami=""):
#     malumot = {'Ism' : ismi,
#                'familiya' : familiyasi,
#                'tugilgan yili' : tugilgan_yili,
#                'yoshi' : 2026-tugilgan_yili,
#                'email manzili' : email_manzili,
#                'telefon raqami' : tel_raqami}
#     return malumot
# malumotlar = []
# print("Mijozlar ro'yxati:")
# while True:
#     print("\nQuyidagi malumotlarni kiriting:", end=" ")
#     ismi=input("Ismingiz:\n")
#     familiyasi=input("Familiyangiz:\n")
#     tugilgan_yili=int(input("Tug'ilgan yilingiz:\n"))
#     email_manzili=input("Email manzilingiz:\n")
#     tel_raqami=input("Telefon raqamingiz:\n")
#     malumotlar.append(malumotnoma(ismi, familiyasi, tugilgan_yili, email_manzili="", tel_raqami=""))
#     javob = input("Yana malumot qo'shasizmi? (yes/no): ")
#     if javob=='no' :
#         break
# print("Mijozlar ro'yxati:")
# print(malumotlar)

# def katta_son(son1, son2, son3):
#     if son1>son2 and son1>son3:
#         print(son1)
#     elif son2>son1 and son2>son3:
#         print(son2)
#     elif son3>son1 and son3>son2:
#         print (son3)
#     else:
#         print("Sonlar teng!")
# katta_son(2, 3, 4)

# def aylana_ustida_amallar(radius):
#     amallar = {'Radiusi' : radius,
#                'diametri' : radius*2,
#                'perimetri' : 2*radius*3.14,
#                'yuzi' : 3.14*radius**2}
#     return amallar
# aylana_ustida_amallar(20)

# def tub_sonlar(min, max):
#     sonlar = []
#     for n in range(min, max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif (n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             sonlar.append(n)
#     return sonlar
# tub_sonlar(1, 30)

# def Fibonachchi(max):
#     son = [1, 1]
#     for n in range(max-2):
#         fib = son[n]+son[n+1]
#         son.append(fib)
#     return son
# Fibonachchi(9)
            

