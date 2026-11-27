# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:03:26 2026

@author: Honor
"""

#adib0 = {
#    'ism' : 'alisher',
#    "familiya" : "navoiy",
#    "tugilgan joyi" : 'hirot',
#    "tugilgan sana" : '1441',
#    'asarlari' : ['Layli va Majnun', 'Saddi Iskandariy', 'Farxod va Shirin', 'Favoluq ul Mafolug']
#    }
#adib1 = {
#    'ism' : 'amir',
#    "familiya" : "temur",
#    "tugilgan joyi" : 'kesh',
#    "tugilgan sana" : '1336',
#    'asarlari' : ['Temur tuzuklari']
#    }
#adib2 = {
#    'ism' : 'jaloliddin',
#    "familiya" : "manguberdi",
#    "tugilgan joyi" : 'gurganch',
#    "tugilgan sana" : '1198',
#    'asarlari' : ['Buyuk sarkarda']
#    }
#adib3 = {
#    'ism' : 'abu rayhon',
#    "familiya" : "beruniy",
#    "tugilgan joyi" : 'beruniy',
#    "tugilgan sana" : '973',
#    'asarlari' : ["O'simliklar olami", "Tirik mavjudodlar"]
#    }
#adiblar = [adib0, adib1, adib2, adib3]
#for adib in adiblar:
#    print(f"{adib['ism'].title()} {adib['familiya'].title()} {adib["tugilgan sana"]} - yil {adib["tugilgan joyi"].title()} da tuvallud topgan.")


#for adib in adiblar :
#    print(f"{adib['ism'].title()} {adib['familiya'].title()} ning asarlaridan namuna: {adib['asarlari']}")

#friends = {
#    'Jamshid' : ['fast and furious', 'social network', 'genshin impact'],
#    'Diyor' : ['Mentalist', 'The pirates of the caribbean', 'John Wick'],
#    'Mirjahon' : ['Cars', 'Dumb and dumber', 'Harry potter']
#    }
#for ism, kinolar in friends.items():
#    print(f"\n{ism} ning sevimli kino-seriallari:")
#    for kino in kinolar:
#        print(kino)

davlatlar = {
    'rossiya' : {'poytaxti' : 'Moskva',
                 'prezidenti' : 'Vladimir Putin'},
    'aqsh' : {'poytaxti' : 'Washington DC',
              'prezidenti' : 'Donald Trump'},
    'ukraina' : {'poytaxti' : 'Varshava',
                 'prezidenti' : 'Vladimir Zelinski'},
    'xitoy' : {'poytaxti' : 'Pekin',
               'prezidenti':'Si Tzi Sin Pin'}
    }
for davlat, info in davlatlar.items():
    print(f"\n{davlat} haqida malumot:   "
          f"poytaxti: {info['poytaxti'] }"
          f" \nprezidenti: {info['prezidenti']}")
    
requested_countries = input('Qiziqqan davlatingizni kiriting!\n>>>').lower()
if requested_countries in davlatlar:
    info = davlatlar[requested_countries]
    print(f"\n{requested_countries.capitalize()} ning poytaxti: {info['poytaxti']}"
          f"\nprezidenti: {info['prezidenti']}")
else:
    print('Kechirasiz bizda bu davlat haqida malumot yoq')





























