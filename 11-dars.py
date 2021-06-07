"""
07/06/2021

Dasturlash asoslari

#11-dars: if-elif-else

Muallif: Abdulhay Yaqubov

Web sahifa: https://python.sariq.dev
"""
#################################################################################################################
# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", 
# agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
# son = int(input("Juft son kiriting: "))
# if son%2 == 0:
#     print("Rahmat!")
# else:    
#     print("Bu son juft emas")
#################################################################################################################
# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

# yosh = int(input("Yoshingizni kiriting: "))

# if yosh < 4 or yosh > 60:
#     print("Siz uchun chipta narhi bepul")
# elif yosh < 18:
#     print("Siz uchun chipta narhi 10_000 so'm")
# elif yosh >= 18:
#     print("Siz uchun chipta narhi 20_000 so'm")    
#################################################################################################################    
# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki 
# katta/kichikligi haqida xabarni chiqaring

# print("Ikkita son kiriting")
# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))
# if son1 == son2:
#     print(f"{son1} = {son2}")
# else:
#     print(f"{son1} <> {son2}")    
#################################################################################################################
# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat 
# yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, 
# mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, 
# "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar = ["Olma", "Anor", "Shaftoli","Anjir","Uzim", "Pomidor","Kartshka", "Piyoz", "Sabzi", "Behi"]
# savat = []
# print("Hurmatli foydalanuvchi 5 ta mahsulotni kiriting:")
# for i in range(5):
#     savat.append(input(f"{i+1}-chi mahsulotni kiriting>>>"))
# for sav in savat:
#     if sav.title() in mahsulotlar:
#         print(f"{sav}-bu mahsulot do'konimizda bor")
#     else:    
#         print(f"{sav}-bu mahsulot do'konimizda yuq")
#################################################################################################################
# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
# Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, 
# do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, 
# "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar 
# do'konimizda yo'q: ....." degan xabarni chiqaring.
# dokonda_bor = []
# dokonda_yuq = []
# for sav in savat:
#     if sav.title() in mahsulotlar:
#         dokonda_bor.append(sav)
#     else:    
#         dokonda_yuq.append(sav)
# if len(dokonda_bor) > 0:
#     print("Do'konimizda quyidagi mahsulotlar bor:")
#     for mah in dokonda_bor:
#         print(mah)
# if len(dokonda_yuq) > 0:
#     print("Do'konimizda quyidagi mahsulotlar yuq:")
#     for mah in dokonda_yuq:
#         print(mah)            
#################################################################################################################
# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni 
# so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. 
# Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, 
# foydalanuvchi!" xabarini chiqaring.

# foydalanuvchilar = ["Ali","Vali","Sanjar","Murod","kozim",]
# if input("Yangi loginni kiriting:").title() in foydalanuvchilar:
#     print("Bu login band, yangi login tanlang")
# else:    
#     print("Hush kelibsiz")
#################################################################################################################
# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan 
# sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 

son = int(input("Istalgan butun son kiriting:"))
for i in range(2, 11):
    if son % i == 0:
        print(f"{son} soni {i} ga qoldiqsiz bo'linadi")