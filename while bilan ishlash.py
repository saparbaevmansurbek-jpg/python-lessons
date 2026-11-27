# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:00:48 2026

@author: Honor
"""


#sevimli_kitob = "Sevimli kitobingizni kiriting!\n>>>"
#sevimli_kitob += "\n(Dasturni to'xtatish uchun 'exit' deb yozing!): "
#ishora = True
#while ishora:
#    qiymat = input(sevimli_kitob)
#    if qiymat == 'exit':
#        ishora = False
#    else:
#        print("Sevimli kitoblaringiz ro'yxati: " + sevimli_kitob)

#foydalanuvchi = 'Necha yoshdasiz?\n>>>'
#foydalanuvchi += "(so'rovnomani to'xtatish uchun 'exit' yoki 'quit' deb yozing): "
#ishora = True
#while ishora:
#    qiymat = input(foydalanuvchi)
#    if qiymat == 'exit' or qiymat == 'quit':
#        ishora = False
#    else:
#        qiymat2 = int(qiymat)
#        if qiymat2<7:
#            print('Sizga kirish 2000 soum')
#        elif qiymat2>=7 and qiymat2<18:
#            print('Sizga kirish 3000 soum')
#        elif qiymat2>=18 and qiymat2<=65:
#            print('Sizga kirish 10000 soum')
#        elif qiymat2>65:
#            print('Sizga kirish bepul')
            
#foydalanuvchi = 'Necha yoshdasiz?\n>>>'
#foydalanuvchi += "(so'rovnomani to'xtatish uchun 'exit' yoki 'quit' deb yozing): "
#while True:
#    qiymat = input(foydalanuvchi)
#    if qiymat == 'exit':
#        break 
#    else:
#        qiymat2 = int(qiymat)
#        if qiymat2<7:
#            print('Sizga kirish 2000 soum')
#        elif qiymat2>=7 and qiymat2<18:
#            print('Sizga kirish 3000 soum')
#        elif qiymat2>=18 and qiymat2<=65:
#            print('Sizga kirish 10000 soum')
#        elif qiymat2>65:
#            print('Sizga kirish bepul')
                  
#foydalanuvchi = 'Necha yoshdasiz?\n>>>'
#foydalanuvchi += "(so'rovnomani to'xtatish uchun 'exit' yoki 'quit' deb yozing): "
#qiymat = ''
#while qiymat != 'exit':
#    qiymat = input(foydalanuvchi)
#    if qiymat != 'exit':
#        qiymat2 = int(qiymat)
#        if qiymat2<7:
#            print('Sizga kirish 2000 soum')
#        elif qiymat2>=7 and qiymat2<18:
#            print('Sizga kirish 3000 soum')
#        elif qiymat2>=18 and qiymat2<=65:
#            print('Sizga kirish 10000 soum')
#        elif qiymat2>65:
#            print('Sizga kirish bepul')
            
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")






















        