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


"""
Thame: Funkcions(Funksiyalar)
"""
"""
Funksiya - Funksiya ma'lum bir vazifani bajarishga mo'ljallangan kodlar yig'indisi.
Biz shu vaqtgacha ko'rib o'tgan funksiyalar: print(), len(), sum(), max(), min()...
"""
""" Funksiya yaratish """
# def salom():
#     """ Ushbu funksiyaning vazifasi Salomlashish """
#     print("Assalom aleykum")

# salom()

""" DOCSTRING """
""" 
    DOCSTRING ---> Defenition
    Docstringni konsolga chiqarish uchun print(funksiya_nomi.__doc__) deb ham yozishimiz mumkin: 
"""
# print(len.__doc__)

# def salom_ber(ism):
#     """ Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya. ism -> Matn kiritish kerak """
#     print(f"Assalomu alaykum, hurmatli {ism}!")

# salom_ber("Ali")
# salom_ber("Vali")
# salom_ber('Umar')

"""
    Funksiyaga nom berishda fe'l, ya'ni harakatni bildiruvchi so'zlar yoki jumlalardan foydalaning. 
    Bu bilan siz o'zgaruvchi va funksiya o'rtasini farqlashingiz oson bo'ladi. 
    Misol uchun, yuqorida biz funksiyamizni salom emas salom_ber deb nomladik.
"""

""" Funksiyaga qiymat uzatish """
# def hisobla(tyil, yil):
#     """
#     Foydalanuvchi yoshini hisoblovchi funksiya. 
#     tyil - Tug'ilgan yilingizni kiriting
#     yil- hozirgi yil
#     """
#     yosh = yil - tyil
#     print(f"Siz {yosh} da ekansiz")

# hisobla(2023, 2000)
# hisobla(2001, 2023)


""" Argumentni kalit so'z bilan uzatish """
# def plus(son1, son2):
#     """ Foydalanuvchi kiritgan sonlarni bir biriga qo'shib beradi. """
#     son3 = son1 + son2
#     print(f"Siz kiritgan {son1} va {son2} larning yig'indisi {son3} ga teng.")
# plus(son2=5, son1=5)


# def full_name(name, surname, father):
#     """
#     full_name - To'liq ism sharifni qaytarish uchun funksiya

#     Arguments:
#         name - str
#         suename - str
#         father - str 
#     """
#     print(f"{surname} {name} {father}")

# full_name(name="Olimjon", surname="Aliyev", father="Baxodirovich")



""" Standar qiymat uzatish """
"""
    Funksiya yaratishda, standart qiymatga ega parametrlar doim oxirida yozilishi kerak. 
    Aks holda xatolik yuzaga keladi.
"""     
# def full_name(familya, ism="Ali"):
#     print(ism, familya)

# full_name(familya = "Olimmov")
# full_name("Asadbek","Mirzanvarov")


# def kv(son=5):
#     """ Kiritilgan sonning kvadratini hisoblovchi funksiya, son - int"""
#     son_kv = son**2
#     print(f"Siz kiritgan {son} ning kvadrati {son_kv} ga teng")
# kv(4)
# kv(5)


"""
Vazifa:
1) Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
2) Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
3) Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
4) Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
    Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
5) Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini 
    tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
6) Foydalanuvchidan uning oila azolari haqidagi malumotlarmni olibn ularni konsulga chiqaruvchi funksiya 
    yozing. M: ismi, yoshi, kasbi...
7) Tog'ri to'rtburchakli uchburchakning katetlarini qabul qilib olib uning gipotenuzsini hisoblovchi funksiya 
    yozing, 2- katetni o'zgarmas parameter sifatida bering.
    f: c**2 = a**2 + b**2 / c ni topish kk / b - o'zgarmas qiymat
Yuqoridagi har bir funksiyaga to'liq tarif(defenition yozing)
"""


"""
Thame: Funkcions(Funksiyalar)
"""

""" Funksiyadan qiymat qaytarish """
def full_name(name, surname):
    """ To'liq ism qaytaradigan funksiya """
    name = f"{name.title()} {surname.title()}"
    return name # qiymat qaytarish uchun return operatorini ishlatamiz

full_name("ALi", "Olimov")

""" Funksiyamiz return operatori yordamida full_name degan o'zgaruvchining qiymatini qaytaradi"""

person1 = full_name("ALi", "Olimov")
person2 = full_name("Husan", "Hasanov")
person3 = full_name("Aziza", "Olimova")

print(person1)
print(person2)


"""
    Qiymat qaytaradigan funksiyaning afzalligi shundaki, biz bu qiymatlardan keyin ham 
    bemalol foydalanishimiz mumkin.Funksiya ichidagi o'zgaruvchilar mahalliy yoki ichki 
    o'zgaruvchilar deyiladi (local variables). Ichki o'zgaruvchilar faqatgina funksiya 
    ichida mavjud bo'ladi, ularga tashqaridan murojat qilib bo'lmaydi. 
    Shuning uchun ham funksiya o'zgaruvchi emas qiymat qaytaradi.
"""

""" Ixtiyoriy qiymat berish """
def full_name(name, surname, father_name=''):
    """ To'liq ism qaytaradigan funksiya """
    full_name = f"{name.title()} {surname.title()} {father_name.title()}"
    return full_name # qiymat qaytarish uchun return operatorini ishlatamiz

person1 = full_name("ALi", "Olimov", "Tolipovich")
person2 = full_name("Husan", "Hasanov")
print(person1)
print(person2)


def taqqoslash(son1, son2, son3):
    x= max(son1, son2, son3)
    return x
a = taqqoslash(4,5,6)
b = taqqoslash(22,43,-6)

print(a)
print(b)

""" Funksiyadan sodda qiymat emas, ro'yxat, lu'gat va boshqa ma'lumot turlarini ham  
    qaytarishimiz mumkin """

""" Funksiyadan lug'at qaytarish """
def person_info(name, surname, birth, gender, age, job=None):
    """ Inson haqidagi malumotlarni qaytaruvchi funksiya """
    person = {
        'name': name,
        'surname': surname,
        "birth": birth,
        "gender": gender,
        "age": age,
        "job": job
    }
    return person

""" 'job' nomli parametrga 'None' standart qiymatini berib ketdik. 
    None Pythonda mavjud emas ma'nosini beradi, va if yordamida tekshirganda 
    False mantiqiy qiymatini qaytardi. 
"""
person1 = person_info("Olimjon", "Vohidov", 1998, "erkak", 25, "quruvchi")
person2 = person_info("Ahmad", "Abbosov", 1987, "erkak", 34)
insonlar = [person1, person2]

print(person1)
print(person2)


""" 1-usul """
print("Insonlar haqida malumotlar: ")
for inson in insonlar:
    print(f"{inson['name']} {inson['surname']}. {inson['birth']}-yilda tug'ilgan,\
hozirda {inson['age']} yoshda. Jinsi {inson['gender']}. \
Kasbi {inson['job']} ")

""" 2-usul """
print("Insonlar haqida malumotlar: ")
for inson in insonlar:
    if inson['job']:
        job = inson['job']
    else:
        job = "nomalum"
    print(f"{inson['name']} {inson['surname']}. {inson['birth']}-yilda tug'ilgan,\
hozirda {inson['age']} yoshda. Jinsi {inson['gender']}. \
Kasbi {job} ")


""" Funksiyadan ro'yhat qaytarish """
def oila(n):
    """ Oila azolaringizning ismini ro'yhat holatida qaytaruvchi funksiya """
    oila = []
    for i in range(n):
        azo = input(f"{i+1}- oila azongizning ismi :")
        oila.append(azo)
    return oila

oila1 = oila(4)
oila2 = oila(7) 
print(oila1)
print(oila2)


""" Funksiyani tsiklda ishlatish """
def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto


print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[]
while True:
    print("\nQuyidagi ma'lumotlarni kiriting",end='')
    kompaniya=input("\nIshlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    korobka=input("Korobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    narhi=input("Narhi: ")

    # Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    # avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))

    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break


print('Onlayn bozordagi mavjud avtomashinalar:')
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['kompaniya']} {avto['rang']} {avto['model']}. Narhi: {narh}")

""" pass operatori """
"""
pass - operatori malum vaqt funksiyani ishlatmaslik kerak bo'lganda kerak bo'ladi
# """
def name(ism):
    pass

name("Abbos")

def name(ism):
    pass

"""
Vazifa:
1) Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va 
    telefon raqamini qabul qilib, lug'at ko'rinishida malumot qaytaruvchi funksiya yozing. 
    Lug'atda foydalanuvchi yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy 
    qiling (masalan, tel.raqam, el.manzil)
2) Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan 
    ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
3) Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
4) Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, 
    perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
5) Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya 
    yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan 
    katta musbat sonlar)
6) Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi 
    sonlar ro'yxatni qaytaruvchi funksiya yozing.  
    Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan 
    ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 
    1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
    
"""