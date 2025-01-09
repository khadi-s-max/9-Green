# """1-	Mashq | 5 Ball
# Bir vaqtni o"zida 4 ta o"zgaruvchi yarating(Bu ishni bir qatorda bajarish zarur !). Hamda o"zgaruvchilarni konsulga chiqaring.
# 2-	Mashq | 5 Ball |  Ushbu matinni konsulga chiqaring:
# “Ahmadning “yuvvosh” mushugi meni ko"rsa, doim yugurib keladi.”
# 3-	Mashq | 5 Ball | Misolni pyhtonda bajaring:
# 93434 ga 94903 ni qoshing, hosil bo"lgan natijadaan 22344 ni ayring va unga 7363 ni qo"shing
# 4-	Mashq | 10 Ball
# Ism, yosh, manzil, maktab, sinf deb nomlangan o"zgaruvchilar yarating va ularni konsulga f”” yordamida chiqaring.
# 5-	Mashq | 10 Ball
# Name, surname deb nomlangan o"zgaruvchilar yarating va ularni yangi full_name deb nomlangan o"zgaruvida jamlang. Hamda full_name deb nomlangan o"
# 6-	Mashq | 15 Ball
# Quidagi o"zgaruvchini   --->    gul = “	   BoyCHeCHak	   ” 
# 1)	Chap tomonidagi bo"shliqni olib tashlab;
# 2)	Har ikki tomonidagi bo"shliqni olib tashlab;
# 3)	Birinchi harifni katta qilib;
# 4)	Barcha hariflarini katta qilib;
# 5)	Barcha hariflarini kichik qilib  konsulga chiqaring.
# """
# """1-mashq"""
# a, b, c, d = 1, 2, 3, 4
# print(a, b, c, d)

# """2-mashq"""
# print('Ahmadning "yuvvosh" mushugi meni ko\'\rsa, doim yugurib keladi.')

# """3-mashq"""
# result = 93434 + 94903 - 22344 + 7363
# print(result)
# """4-mashq"""
# ism = "Ali"
# yosh = 15
# manzil = "Toshkent"
# maktab = "bm-maktab"
# sinf = "9-sinf"

# print(f"Ism: {ism}, Yosh: {yosh}, Manzil: {manzil}, Maktab: {maktab}, Sinf: {sinf}")

# """5-mashq"""
# name = "Ahmad"
# surname = "Aliyev"
# full_name = name + " " + surname

# print(full_name.lower())

# """6-mashq"""
# gul = "   BoyCHeCHak   "
# print(gul.lower())
# print(gul.lstrip())
# print(gul.strip())
# print(gul.capitalize)
# print(gul.title())





# """==============================9g002=========================="""
# # 1 Mashq 

# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))



# print(f"Yig'indi: {a+b}")
# print(f"Ayirma: {a-b}")
# print(f"Ko'paytma: {a*b}")
# print(f"Bo'linma: {a/b}")
# print(f"O'rta arifmetigi: {(a + b) / 2}")
# print(f"{a} ning kvadrati: {a ** 2}, {b} ning kvadrati: {b ** 2}")
# print(f"{a} ning kubi: {a ** 3}, {b} ning kubi: {b ** 3}")

# # 2 Mashq 

# yosh = int(input("Yoshingizni kiriting: "))
# tugilgan_yil = 2023 - yosh
# print(f"Sizning tug'ilgan yilingiz: {tugilgan_yil}")

# # 3 Mashq 
# matn1 = "bu mashq uchun berilgan matn"
# matn2 = "aliSHeR nAvOIy"
# matn3 = "boborahim mashrab"
# matn4 = "aLIYEV vALI"
# matn5 = "SolijoNOv JoniBEK"
# matn6 = "       Assalomu Aleykum"
# matn7 = "Assalomu Aleykum       "
# matn8 = "       Assalomu Aleykum    "
# matn9 = "assalomu aleykum"
# matn10 = "BOBORAHIM MASHRAB"


# print(matn1.capitalize())
# print(matn2.lower())
# print(matn3.upper())
# print(matn4.title())
# print(matn5.lower())
# print(matn6.lstrip())
# print(matn7.rstrip())
# print(matn8.strip())
# print(matn9.title())
# print(matn10.lower())


# # 4) Mashq 
# #1
# result1 = round((231 / 4.7) * 5)
# print(result1)
# # 2

# result2 = (3 ** 4) + (35345 ** 0.5)
# result2 = result2 / 8
# print(result2)
# # 3

# import random
# random_number = random.randrange(20, 80)
# print(random_number)
# # 4

# radius = float(input("Aylananing radiusini kiriting: "))
# S = 3.14 * radius ** 2
# print(f"Aylananing yuzi: {S}")
# # 5

# a = float(input("Kvadratning tomonini kiriting: "))
# S_kvadrat = a ** 2
# P_kvadrat = a * 4
# print(f"Kvadratning yuzi: {S_kvadrat}, Perimetri: {P_kvadrat}")
# # 5 Mashq 

# uy_raqami = input("Uy raqamini kiriting: ")
# kocha = input("Ko'cha nomini kiriting: ")
# mahalla = input("Mahalla nomini kiriting: ")
# tuman = input("Tuman nomini kiriting: ")
# viloyat = input("Viloyat nomini kiriting: ")

# print(f"Siz {viloyat} viloyati, {tuman} tumani, {mahalla} MFY, {kocha} {uy_raqami}-uyda yashaysiz.")


# """_______________________________9g005_______________________"""
# """4 dan 873 gacha bo’lgan toq sonli ro’yhat yarating va ro’yhatdagi har bir sonning ildizini chiqaring.
# 2-mashq | 10 Ball
# Foydalanuvchidan uning ismini so’rang va unga quida keltirilgan javoblardan mosini qaytaring.
# Dasturni tuzishda or operatoridan foydalanig !
# Muslima  – Salom Muslima. Davramizda hush ko’rdik.
# Zilola/Sevara  – Assalomu aleykum. Zilola/Sevara sizga qanday yordam berishim mumkin?
# Anvar/Aziz  – Salom Anvar/Aziz . Bugun Qayerga boramiz ?
# 3-mashq | 10 Ball | 102 dan 2020 gacha bo’lgan sonladan iborat ro’yhat yarating va ro’yhatdagi:
# 1000 gacha bo’lgan sonning 3-darajasini toping.
# 1500 dan katta barcha sonlarning o’zidan 4 taga kichik sonni toping.
# Ro’yhatdagi 7 ga qoldiqsiz bo’linadigan sonlarning ildizini toping.
# 4-mashq | 10 Ball  | -322 dan -2 gacha bo’lgan barcha toq sonlarning:
# 1) 5 chi va 7 chi darajasini toping;
# 2) Ro’yhatdagi har bir sondan 4 taga kichik sonni konsulga chiqaring;
# 3) Ro’yhatning uzunligini o’lchang;
# 4) Ro’yhatdagi har bir sonning ildizini toping;
# 5) Ro’yhatni avval o’sish tartibida keyin esa kamayish tartibida tartiblab konsulga chiqaring;
# 5-mashq | 10 Ball | Kodni huddi shu ko’rinishda ko’chirib oling va undagi xatolarni topib to’g’irlang
# a = float(input("1-sonni kirirting:"))
# b = int(input("2-sonni kirirting:"))
# if a<b:
# print(f"{a}>{b}")
# elif a<b:
# print(f"{a}<{b}")
# elif a != :
# print(f"{a}={b}")
# """

# """1-mashq"""
# from math import sqrt


# toq_sonlar = []
# for i in range(4, 874):
#     if i % 2 != 0:
#         toq_sonlar.append(i)

# ildizlar = []
# for son in toq_sonlar:
#     ildizlar.append(sqrt(son))

# print(ildizlar)

# """2-mashq"""

# ism = input("Ismingizni kiriting: ")

# if ism == "Muslima":
#     print("Salom Muslima. Davramizda hush ko'rdik.")
# elif ism == "Zilola" or ism == "Sevara":
#     print("Assalomu aleykum. Zilola/Sevara sizga qanday yordam berishim mumkin?")
# elif ism == "Anvar" or ism == "Aziz":
#     print("Salom Anvar/Aziz. Bugun qayerga boramiz?")
# else:
#     print("Salom!")

"""3-mashq"""

import math

sonlar = list(range(102, 2021))
kubi = []
for son in sonlar:
    if son <= 1000:
        kubi.append(son ** 3)

son1= []
for son in sonlar:
    if son > 1500:
        son1.append(son - 4)

ildiz = []
for son in sonlar:
    if son % 7 == 0:
        ildiz.append(round((son**0.5),2))

print("3-darajalar:", kubi        )
print("4 taga kichik sonlar:", son1)
print("7 ga qoldiqsiz bo'linadigan sonlarning ildizi:", ildiz)


# """4-mashq"""

# import math


# toq_sonlar_range = []
# for i in range(-322, -1):
#     if i % 2 != 0:
#         toq_sonlar_range.append(i)


# beshinchi_daraja = [son ** 5 for son in toq_sonlar_range]
# yettinchi_daraja = [son ** 7 for son in toq_sonlar_range]

# kichik_sonlar_range = [son - 4 for son in toq_sonlar_range]

# uzunlik = len(toq_sonlar_range)

# ildizlar_range = [math.sqrt(abs(son)) for son in toq_sonlar_range]

# sort_o_sish = sorted(toq_sonlar_range)
# sort_kamayish = sorted(toq_sonlar_range, reverse=True)

# print("5 chi darajalar:", beshinchi_daraja)
# print("7 chi darajalar:", yettinchi_daraja)
# print("4 taga kichik sonlar:", kichik_sonlar_range)
# print("Ro'yhat uzunligi:", uzunlik)
# print("Ildizlar:", ildizlar_range)
# print("O'sish tartibida:", sort_o_sish)
# print("Kamayish tartibida:", sort_kamayish)


