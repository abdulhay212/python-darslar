"""
07/06/2021

Dasturlash asoslari

#09-dars: for loops

Muallif: Abdulhay Yaqubov

Web sahifa: https://python.sariq.dev
"""
# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, 
# va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# Yuoqirdagi tsikl tugaganidan so'ng, 
# ekranga "Kod n marta takrorlandi" degan xabar chiqaring 
# (n o'rniga kod necha marta takrorlanganini yozing)
# ismlar = ["Umidjon", "Abdumalik", "Muhammadali", "Qaxramonjon","Fahriddin"]
# for ism in ismlar:
#     print(f"Assalomu alaykum {ism} .Sahifamizga hush kelibsiz!")      
# print(f"Kod {len(ismlar)} marta takrorlandi")        
# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir 
# elementining kubini yangi qatordan konsolga chiqaring.
# for son in list(range(11,100,2)):
#     print(son**3)
# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. 
# Natijani konsolga chiqaring.
# kinolar = []
# print("5 ta eng sevimli filmingizni kiriting:")
# for i in range(5):
#     kinolar.append(input(f"{i+1}-kino:"))
# print(kinolar)    

# Foydalanuvchidan bugun nechta odam bilan 
# uchrashganini (suhbatlashganini) so'rang, 
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.

suhbatdoshlar_soni = int(input("Bugun nechta odam bilan suhbatlashdingiz?>>>"))
suhbatdoshlar = []
for s in range(suhbatdoshlar_soni):
    suhbatdoshlar.append(input(f"{s+1}-suhbatdosh: "))
print(suhbatdoshlar)    
    
