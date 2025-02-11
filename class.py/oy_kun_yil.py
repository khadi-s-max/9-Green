# """bz datetimedan foydalanib foydalanuvchii t_kuni yilini sorab uni necha yil u 
# necha kun yashaganini chiqarib beradigan dastur yaratishhmz kerak"""

# import datetime
# # 1-ish foydalanuvchini qachon tugilganini yili oyi kunini soraymz

# t_kuni = datetime.datetime.now()
# t_yil = t_kuni.year
# t_oy = t_kuni.month
# t_kun = t_kuni.day

# # 2-ish foydalanuvchini yashagan yilni, yoshni, kunni va yilga qarshi moslug'ini chiqarib berish

# yashagan_yil = t_yil - int(input("Yashagan yilni kiriting: "))
# yash = t_yil - yashagan_yil
# yashagan_kun = t_kun - int(input(f"{yashagan_yil}-yilning {yash}-yillikda yashagan kunni kiriting: "))
# yashagan_moslug = yash * 365 + yashagan_kun

# print(f"{yashagan_yil}-yilning {yash}-yil {yashagan_kun}-kunning yashagan  {yashagan_moslug} ga teng.")



# import datetime


# # foydalanuvchiini kunini olish 
# tugilgan_sana = input("Tug'ilgan sanangizni '2009 8 24 formatida kiriting: ")

# tugilgan_sana = datetime.datetime.strptime(tugilgan_sana, "%Y %m %d")

# hozir = datetime.datetime.now()


# farq = hozir - tugilgan_sana


# yil = farq.days // 365
# kun = farq.days % 365


# print(f"Siz {yil} yil va {kun} kun yashagansiz.")

import datetime
def tk(yil, oy, kun)-> str:
    """________
    _______
    _________"""
    t_yil=yil
    t_oy=oy
    t_kun=kun
    t_sana = datetime.date(yil , oy, kun)
    bugun = datetime.date.today()
    if (bugun-t_sana).days <=365:
        return f"siz tugilganizga {(bugun-t_sana).days} kun bo'ldi "

    elif bugun.month > t_oy:
        yil=bugun.year-t_yil
        kun=bugun-datetime.date(bugun.year-1,t_oy,t_kun)
        return f"siz tugilganizga {yil} yil va {kun.days} kun bo'ldi "
    elif bugun.month == t_oy :
        if bugun.day < t_kun:
            yil=bugun.year-t_yil-1
            kun=bugun-datetime.date(bugun.year-1,t_oy,t_kun)
            return f"siz tugilganizga {yil} yil va {kun.days} kun bo'ldi "
        elif bugun.day==t_kun:
            yil=bugun.year-t_yil
            return f"siz tugilganizga {yil} yoshga to'ldiz  "
        else:
            yil=bugun.year-t_yil
            kun=bugun-datetime.date(bugun.year-1,t_oy,t_kun)
            return f"siz tugilganizga {yil} yil va {kun.days} kun bo'ldi "
    else:
        yil=bugun.year-t_yil-1
        kun=bugun-datetime.date(bugun.year-1,t_oy,t_kun)
        return f"siz tugilganizga {yil} yil va {kun.days} kun bo'ldi "

print(tk(2000,1,1)) # 1999 yil yashagan


