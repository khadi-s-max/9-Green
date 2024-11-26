# """funksiyalar"""
# print("hello world!")

# def salom_ber():
#     print("Assalomu aleykum!")
# salom_ber()

# def yosh_top():
#     ism= input("ismingizni kiriting : ")
#     t_yil= int(input(f"{ism} yoshingizni kiriting : "))

#     print(f"{ism} siz {t_yil-2024} yilida tugulgansz")
# yosh_top()

"""parametr"""

def yosh_top(t_yil):
    """tugulgan yilni qabul qiluvchi dastur
    va yoslarni xam xisoblaydi """
    print(f"sizni9ng yoshingiz {2024-t_yil} da ")

yosh_top(2009)
yosh_top(int(input("tugulgan yilizni kiriting : ")))

x=int(input("tugulgan yilizni kiriting : "))
yosh_top(x)