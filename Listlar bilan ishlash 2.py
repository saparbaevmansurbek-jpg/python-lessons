# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:28:39 2026

@author: Honor
"""

davlatlar = ['USA', 'UK', 'Russia', 'Japan', 'Italy', 'Germany', 'France']
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse = True))
print(davlatlar)
davlatlar.reverse()
davlatlar.sort()
davlatlar.sort(reverse = True)
sonlar = range(120,1200)
print(sum(sonlar))
print(sonlar[-1] - sonlar[0])
len(sonlar)
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[550:530])
taomlar = ['Manti', 'Gumma', 'Shashlik', 'Palov', 'Somsa']
nonushta = taomlar[:]
nonushta.remove('Shashlik')
nonushta.append('Smetana')
nonushta.append('Salad')
print(taomlar)
print(nonushta)
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"