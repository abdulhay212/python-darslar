"""
04/06/2021

Dasturlash asoslari

#08-dars: Ro'yxatlar bilan ishlash

Muallif: Abdulhay Yaqubov

Web sahifa: https://python.sariq.dev
"""
#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# davlatlar = ["Uzbekiston","'iston","Qirg'iziston","Tojikiston","Turkmaniston","AQSH","Rossiya","Xitoy"]
# print(davlatlar)

#Ro'yxatning uzunligini konsolga chiqaring
# print(len(davlatlar))

#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# print(sorted(davlatlar))

#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# print(sorted(davlatlar, reverse=True))

#Asl ro'yxatni qaytadan konsolga chiqaring
# print(davlatlar)

#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# davlatlar.reverse()
# print(davlatlar)

#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# juft_sonlar = list(range(120,1200,2))
# print(juft_sonlar)

#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# print(sum(juft_sonlar))

#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# print(max(juft_sonlar) - min(juft_sonlar))

#Ro'yxatdagi elementlar sonini hisoblang
# print(len(juft_sonlar))

#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# print(juft_sonlar[0:20])
# print(juft_sonlar[-20:])
# print(juft_sonlar[270:290])
# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ["kasha", "sho'rva", "mastava","manti","dimlama"]
# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]
#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove("manti")
nonushta.remove("dimlama")
nonushta.append("lag'man")
nonushta.append("osh")
#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print("bu ruyhat taomlar", taomlar)
print("bu ruyhat nonushta", nonushta)
#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"