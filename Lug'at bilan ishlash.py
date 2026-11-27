# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:59:01 2026

@author: Honor
"""

#otam = {'ismi':'Mavlutdin',"tugilgan yili":"1954","tugilgan shahri":"Samarqand viloyati"}
#print(f'otamning ismi {otam["ismi"]}, {otam["tugilgan yili"]} -yilda, {otam["tugilgan shahri"]}da tug"ilgan')

#sevimli_taom = {'Ali':'manti','Vali':'somsa','Akmal':'osh','Tolib':'kabob','Kamron':'xonim'}
#print(f"Alining sevimli taomi {sevimli_taom['Ali']}, Valining sevimli taomi {sevimli_taom['Vali']}, Tolibning sevimli taomi {sevimli_taom['Tolib']}.")

phython_dictionary = {'int':'butun son','float':'onli kasr','string':'matn','if':'agar','else':'yoki'}
kalit_soz = input("Kalit so'z kiriting!\n>>>").lower()
tarjima = phython_dictionary.get(kalit_soz)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(kalit_soz + " so'zi " + tarjima + " deb tarjima qilinadi")