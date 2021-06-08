"""
08/06/2021

Dasturlash asoslari

#14-dars: DICTIONARY

Muallif: Abdulhay Yaqubov

Web sahifa: https://python.sariq.dev
"""
##############################################################################
# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting 
# (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring:
# Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
###########
# otam = {'ismi':'nasriddin', 't_yili':'1954', 'shahri':'andijon', 'manzili':'andijon viloyati, shaxrihon tumani, segazaqum qfy'}
# print(f"Otamning ismi {otam['ismi'].title()}, {otam['t_yili']} - yilda, {otam['shahri'].title()} viloyatida tug'ilgan")
##############################################################################
# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
# Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
###########
# taomlar = {'ali':'osh', 
#            'vali':"sho'rva", 
#            'botir':"lag'man",
#            'komil':'somsa',
#            'sarvar':'shashlik'}
# print(f"Alinig sevimli taomi {taomlar['ali']}")
# print(f"Valinig sevimli taomi {taomlar['vali']}")
# print(f"Botirnig sevimli taomi {taomlar['botir']}")
##############################################################################
# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, 
# float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. 
# Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
###########
izoh = {'integer':'butun sonlar', 
        'float':"o'nlik sonlar", 
        'string':'matn', 
        'if':"shartli belgi(agar)",
        'else':'shartli belgi(aks holda)'}
# # print(izoh)
# kalitsuz = input("Biror kalit so'z kiriting>>>").lower()
# print(izoh.get(kalitsuz,"Bunday kalit so'z mavjud emas"))
##############################################################################
# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
###########
kalitsuz = input("Biror kalit so'z kiriting>>>").lower()
tarjima = izoh.get(kalitsuz)
if tarjima == None:
    print("Bunday ma'lumot mavjud emas!")
else:
    print(f"'{kalitsuz}' ning tarjimasi '{tarjima}' ga teng")    
