"""
07/06/2021

Dasturlash asoslari

#10-dars: IF-ELSE

Muallif: Abdulhay Yaqubov

Web sahifa: https://python.sariq.dev
"""
# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining 
# birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car.lower() == "gm":
#         print(car.upper())
#     else:
#         print(car.title())
# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.         
# for car in cars:
#     if car.lower() != "gm":
#         print(car.title())
#     else:
#         print(car.upper())

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar 
# ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  
# matnini konsolga chiqaring.
# login = input("loginni kiriting:>>> ")
# if login.lower() == "admin":
#     print(f"Xush kelibsiz, Admin")
# else:    
#     print(f"Xush kelibsiz, {login}")

# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, 
# "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# print("Ikkita son kiritng:")
# son1 = input("1-sonni kiriting>>>")
# son2 = input("2-sonni kiriting>>>")
# if son1 == son2:
#     print("Sonlar teng")
# else:
#     print("Sonlar teng emas")    

# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", 
# agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
# son = float(input("Istalgan sonni kiritng:"))
# if son > 0:
#     print("Musbat son")
# else:
#     print("Manfiy son")    

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. 
# Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
son = float(input("Son kiritng:"))
if son > 0:
    print(f"{son} ning ildizi {son**0.5} ga teng")
else:
    print("Musbat sonni kiriting")
