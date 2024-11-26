# """
# Thame: While tsikli
# """
# sonlar = [1,2,3,4,5,6,7,8,9,10]
# for son in sonlar:
#     print(son)

# """ 1 """
# son = 1
# while son < 100:
#     print(son)
#     son = son + 1 
    


# """ 3 """
# while True: # abadiy tsikl
#     savol = input("son kiriting: ")
#     if savol.isdigit():
#         print(int(savol)**2)
#     elif savol == 'exit':
#         break # tsiklni to'xtatish uchun 
#     else:
#         print("son kiriting!!!")


# """ Tug'ilgan yil """
# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         if int(yosh) >= 10 and int(yosh) <= 110:
#             print(f"Siz {2024-int(yosh)}-yilda tug'ilgansiz")
#         else:
#             print("Siz noto'g'ri yosh oralig'ini kiritingiz")
#     elif yosh == "exit":
#         print("Dastur tugadi")
#         break
#     else:
#         print("Siz son kiritmadingiz !!!")


# """tugilgan yili automoy"""

# """while true abadiy tsikil"""
# while True:
#     savol=input("biror son kiriting: (dasturdan chiqmoqchi bo'lsangiz \'exit\' deb yozing ): ")
#     if savol=='exit':
#         print("Dastur tugadi ")
#         break
#     else:
#         print(f"{savol} ning kvadrati {int(savol**2)} ga teng ")


# """2-shart"""
# while True:
#     savol=input("biror son kiriting: (dasturdan chiqmoqchi bo'lsangiz \'exit\' deb yozing ): ")
#     if savol=='exit':
#         print("Dastur tugadi ")
#         break
#     elif savol.isdigit():
#         print(f"{savol} ning kvadrati {int(savol)**2} ga teng ")
        

# """parol"""
# parol=input("oz parolingizni kiriting: ")
# while True:
#     parol1=input("parolni kiriting: ")
#     if parol==parol1:
#         print("Parol muvaffaqiyatli kiritildi")
#         print("dasturga xush kelibsiz")
#         break
#     else:
#         print("parol xato")
            
# """parol o'rnatish"""



# while True:
#     prl=input("dastur uchun parol kiriting: ")
#     if len(prl)>=8:
#         prl1=input("parolni boshidan kiriting: ")
#         if prl==prl1:
#             print("kod muvaffaqiyatli o'rnatildi")
#             break
#         elif prl!=prl1:
#             print("Parol xato takrorlandi qayta kiriting ")
#     else:
#         print("parol 8 belgidan kam qayta parol kiriting  ")

# while True:
#     parol1=input("parolni kiriting: ")
#     if prl==parol1:
#         print("Parol muvaffaqiyatli kiritildi")
#         print("dasturga xush kelibsiz")
#         break
#     else:
#         print("parol xato")



# """yoshi va yilini hisoblash"""
# while True:
#     yosh=input("yoshingizni kiriting: \"Chiqish uchun exit deb yozing\"")
#     if yosh!="exit":
#         yosh1=int(yosh)
#         if yosh>=0 or yosh<=110:
#             print(f"Siz {yosh} dasiz va {2024-yosh} yilda tug'ulgansiz")
#         else:
#             print("Siz xato son kiritdingiz!!!!!")
#     elif yosh=="exit":
#         print("dastur tugatildi")
#         break
#     else:
#         print("Siz son kiritmadingiz!!!")
# ismlar=[]

# while True:
#     ismlar.append(input("ism kiriting : "))
#     savol=input("dasturdann  chiqishni xoxlaysanmi:  (xa\yo'q)  ").lower()
#     if savol=="xa" or savol=="ha":
#         print("dastur tugatildi")
#         break
#     elif savol=="yo'q":
#         print("davom etamiz")


# while True:
#     son=int(input("son kiriting : "))
#     print(f"Siz kiritgan {son} ning kvadrati {son**2} ga teng  ")
#     savol1=input("dasturdann  chiqishni xoxlaysanmi:  (xa\yo'q)  ").lower()
#     if savol1=="xa" or savol1=="ha":
#         print("dastur tugatildi")
#         break
#     elif savol1=="yo'q":
#         print("davom etamiz")


    
"""yoshi va yilini hisoblash"""
# while True:
#     yosh=input("yoshingizni kiriting: \"Chiqish uchun exit yoki quit deb yozing\"").lower()
#     if yosh!="exit":
#         yosh1=int(yosh)
#         if yosh1>=0 or yosh1<=110:
#             print(f"Siz {yosh1} dasiz va {2024-yosh1} yilda tug'ulgansiz")
#         else:
#             print("Siz xato son kiritdingiz!!!!!")
#     elif yosh=="exit" or yosh=="quit":
#         print("dastur tugatildi")

""" 
Vazifa
1) Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. 
    Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating.

    
2) Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va 
chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur 
to'xtasin (ikkita shartni ham tekshiring). Yuqoridagi dasturni turli usullarda
yozib ko'ring (break, ishora)


3) Quyidagi dasturda bir nechta mantiqiy xatolar bor. 
Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True:
    qiymat = input(savol)
    if qiymat<0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
4) Foydalanuvchidan tizimga kirishi uchun parol so'rang, foydalanuvchi to'gri javob 
kiritsa unga 'hush keib siz' degan habar chiqsinva dastur to'xtasim. 
Agar foydalanuvchi 3 marta xato parol kiritsa uni abadiy tsiklga tushurib qo'ying.  
5) Online bozor loyihasini qiling. Avvaliga foydalanuvchiga do'koningizdagi mahsulotlarni nomi va narxini ko'rsating,
song foydalanuvchidan nima olishini so'rang, keyin xaridni davom etirasizmi yoki yo'q deb so'rang
agar ha desa yana mahsulot nomini so'rang, agar yoq dasa jarayoni tugatib, sotib olgan mahsulotlari va 
ularning narxini ko'rsating. 
6) 1 dan 100 gacha bo'lgan toq sonlar yig'indisini toping.
"""

""" 
2) Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va 
chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur 
to'xtasin (ikkita shartni ham tekshiring). Yuqoridagi dasturni turli usullarda
yozib ko'ring (break, ishora)
"""



"""5-mashq"""
# while True:
#     son=input("son kiriting \'chiqish deb yozing \' : ")
#     if son=="chiqish":
#         print("dastur tugadi!")
#         break

#     if son.isdigit():
#         son1=int(son)
#         if son%2==0:
#             print(f"bu son juft : {son1}")
#         elif son%3==1:
#             print(f"bu son toq : {son1}")
#     else:
#         print(f"faqat son yoki 'chiqish' deb kiriting ")

x=0
parol= 1012
while True:
    prl=input("dastur uchun parol kiriting: ")
    
    if prl==parol:
        print("xush kebsiz")
        break
    x+=1
    if x>=3:
        while True:
             print(f"{x} parol xato siz bloklandiz")
        








            
