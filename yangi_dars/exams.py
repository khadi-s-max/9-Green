"""otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan

Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing."""
# 1-mashq
# otam={
#     "ism":"Baxrom",
#     "yosh":"40",
#     "t_yil":"1984",
#     "t_city":"namangan viloyati",
# }
# print(f"otam haqida qisqacha ma'lumot: ism  {otam['ism']} ,{otam['yosh']} yosh, {otam['t_yil']} yilda {otam['t_city']} da tug'ilganlar")
 

"""10.09.2024 """

# 1) otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta 
#     m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida 
  
#   2) Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
    # Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

# 3) Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z(atamani) kiriting 
    # (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.

    # 4) Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
    # Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

    # 6) Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va 
    # qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 


"""1-mashq"""
otam={
    "ism":"Baxrom",
    "yosh":"40",
    "t_yil":"1984",
    "t_city":"namangan viloyati",
}
print(f"otam haqida qisqacha ma'lumot: ism  {otam['ism']} ,{otam['yosh']} yosh, {otam['t_yil']} yilda {otam['t_city']} da tug'ilganlar")
 
ukam={
    "ism1":"yasin",
    "yosh1":"13",
    "t_yil1":"2011",
    "t_city1":"namangan viloyati",
}
print(f"ukam haqida qisqacha ma'lumot: ism  {ukam['ism1']} ,{ukam['yosh1']} yosh, {ukam['t_yil1']} yilda {ukam['t_city1']} da tug'ilganlar")
 
onam={
    "ism2":"Mo'tabar",
    "yosh2":"35",
    "t_yil2":"1989",
    "t_city2":"namangan viloyati",
}
print(f"onam haqida qisqacha ma'lumot: ism  {onam['ism2']} ,{onam['yosh2']} yosh, {onam['t_yil2']} yilda {onam['t_city2']} da tug'ilganlar")
 



"""2-mashq"""
taomlar = {
    'ali':'osh',
    "oydina":"manti",
    "madaminova":"tobboki"

}
print(f"Alining sevimli taomi {taomlar['ali']}")
print(f"oydinaning sevimli taomi {taomlar['oydina']}")
print(f"Madaminovaning sevimli taomi {taomlar['madaminova']}")

