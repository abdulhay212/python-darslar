"""
03/06/2021

Dasturlash asoslari

#07-dars: Lists

Muallif: Abdulhay Yaqubov

Web sahifa: https://python.sariq.dev
"""
#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# ismlar = ["Umid", "Abdumalik", "Fahriddin", "Muhammadali"]

#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
# print(f"{ismlar[0]} ishlar bo'lyaptimi")
# print(f"{ismlar[1]} safarlar yaxshimi, uylar muborak bo'lsin")
# print(f"{ismlar[2]} yaxshi yetib oldizmi")
# print(f"{ismlar[2]} bormisiz, ko'rinmaysiz")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
# sonlar = [15, -20, 20.6, 5, 13_235_201, 2_566]
# print(sonlar)

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning 
# qiymatini o'zgartiring, ba'zilarini esa almashtiring.
# sonlar[0] = 20.56
# sonlar[3] = sonlar[2] + 201
# del sonlar[5]
# print(sonlar)

#t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, 
# ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
# t_shaxslar = ["AbubakirSiddiq", "HazratiUmar", "HazratiUsmon", "HazratiAli"]
# z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doanald Trump']

#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
# print(f"""Men tarixiy shaxslardan {t_shaxslar[0]} bilan,
# zamonaviy shaxslardan esa {z_shaxslar[0]} bilan
# suhbat qilishni istar edim""")    

#friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga 
# chaqirmoqchi bo'lgan do'stlaringizni kiriting.

friends = []
friends.append("Umidjon")
friends.append("Abdumalik")
friends.append("Fahriddin")
friends.append("Muhammadali")
friends.append("Murod")
friends.append("Qahramonjon")
# print(friends)

#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
friends.remove("Abdumalik")
friends.remove("Qahramonjon")
friends.remove("Fahriddin")
# print(friends)

#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.append("Davron")
friends.insert(0, "Kozim")
friends.insert(3, "Shohruh")
print(friends)

#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan 
# do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
yangi_mehmonlar = []
yangi_mehmonlar.append(friends.pop(3))
yangi_mehmonlar.append(friends.pop(-1))
yangi_mehmonlar.append(friends.pop(0))
yangi_mehmonlar.append(friends.pop(1))
print(yangi_mehmonlar)


