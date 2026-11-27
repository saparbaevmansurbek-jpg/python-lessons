# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:32:02 2026

@author: Honor
"""
ismlar = ['Diyorbek', 'Mirjahon', 'Jamshidjon', 'Amirxon']
#print("Salom " + ismlar[1] + ", bugun choyxona bormi?")
#print(ismlar[2] + ", choyxonaga boramizmi?")
#print(ismlar[0] + ", darsing qachon?")
#print(ismlar[3] + ", bugun nima qilamiz?")
sonlar = [3, -15, 8.5, 19]
#print(sonlar[2] - sonlar[1])
#print(sonlar[3] + sonlar[0])
#print(sonlar[0] * sonlar[2])
#print(sonlar[1] / sonlar[3])
sonlar[2] = -77
sonlar.append(99)
sonlar.insert(1, 0.54)
t_shaxslar = ['Alisher Navoiy', 'Amir Temur', 'Jaloliddin Manguberdi', 'Abu Ali Ibn Sino']
z_shaxslar = ['Elon Mask', 'Jeff Bezos', 'Cristiano Ronaldo', 'Bill Gates']
shoir = t_shaxslar.pop(0)
sarkarda = t_shaxslar.pop(1)
trilioner = z_shaxslar.pop(0)
goat = z_shaxslar.pop(1)
#print("Men tarixiy shaxslardan " + shoir + " bilan, zamonaviy shaxslardan esa " + trilioner + " bilan suhbat qilishni istar edim")
#print(sarkarda + " Xorazm tarixidagi buyuk sarkardadir!")
#print("Tarixdagi eng buyuk futbolchi bu " + goat + "dir!")
friends = []
friends.append('Diyorbek')
friends.append('Bexruz')
friends.append('Javohir')
friends.append('Amirxon')
friends.remove('Javohir')
friends.insert(0, 'Dilmurod')
friends.insert(-1, 'Giyos')
mehmonlar = []
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(1))


