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
        

"""parol"""
# parol=input("oz parolingizni kiriting: ")
# while True:
#     parol1=input("parolni kiriting: ")
#     if parol==parol1:
#         print("Parol muvaffaqiyatli kiritildi")
#         print("dasturga xush kelibsiz")
#         break
#     else:
#         print("parol xato")
            
"""parol o'rnatish"""



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



"""yoshi va yilini hisoblash"""
while True:
    yosh=input("yoshingizni kiriting: \"Chiqish uchun exit deb yozing\"")
    if yosh!="exit":
        yosh1=int(yosh)
        if yosh>=0 or yosh<=110:
            print(f"Siz {yosh} dasiz va {2024-yosh} yilda tug'ulgansiz")
        else:
            print("Siz xato son kiritdingiz!!!!!")
    elif yosh=="exit":
        print("dastur tugatildi")
        break
    else:
        print("Siz son kiritmadingiz!!!")


            
