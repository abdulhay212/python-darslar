"""
03/06/2021

Dasturlash asoslari

#05-dars: STRING (MATN)

Muallif: Abdulhay Yaqubov

Web sahifa: https://python.sariq.dev
"""

# kocha = "Mustaqillik"
# mahalla = "Tuman"
# tuman = "Shaxrixon"
# viloyat = "Andijon"

# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Diqqat uzun kodlarni \ belgisi yordamida keyingi qatorga
# ko'chirish mumkin

# print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
#       tuman + " tumani, " + viloyat + " viloyati")


#Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang.

kocha = input("kochani kiriting:>>>")
mahalla = input("mahallani kiriting:>>>")
tuman = input("tumanni kiriting:>>>")
viloyat = input("viloyatni kiriting:>>>")

# print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
#       tuman + " tumani, " + viloyat + " viloyati")

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatorga yozing    
# print(kocha + "ko'chasi,\n" + mahalla + "mahallasi,\n" + \
#       tuman + "tumani,\n" + viloyat + " viloyati")
    
# Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi manzil deb nomlangan o'zgaruvchiga yuklang
manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"    
print(manzil)

#manzil ga biz yuqorida o'rgangan metodlarni qo'llab ko'ring.
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())
