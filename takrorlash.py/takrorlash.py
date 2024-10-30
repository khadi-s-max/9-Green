"""___________9b001_______________"""

#1-exersice

# ism="hadicha"
# familya="botirova"
# yosh=15
# kitoblar=["garri ","potter","naimaning sarguzashtlari   "]
# kasb="o'quvchi"
# print(type(ism))

# print(type(familya))

# print(type(yosh))

# print(type(kitoblar))

# print(type(kasb))

# #2 exercise
# from math import sqrt
# print(round(sqrt(4364+1233),2))

# #3 exercise

# s1=int(input("birinchi sonni kiriting : "))
# s2=int(input("ikkinchi  sonni kiriting : "))
# print(((s1**2)+(s2**2))/23)

# #4 exercise
# x=input("son kiriting : ")
# x=int(x)
# print(type(x))

# x=float(x)
# print(type(x))

#5 exercise
# kbs=[]
# kbs.append(input("1- kirit "))
# kbs.append(input("2- kirit "))
# kbs.append(input("3- kirit "))
# kbs.append(input("4- kirit "))
# kbs.append(input("5- kirit "))
# print(kbs)

#6 exercise
sudens=["Ali","Maruf","Bahrom"]
#qo'shish
sudens.insert(0,"hadicha")
sudens.insert(2,"hadicha")
sudens.insert(-1,"hadicha")
print(sudens)
#alamshtirish 
sudens[0]="sarvinoz"
print(sudens)
sudens[3]="sarvinoz"
print(sudens)


"""9b004"""
#1 exercise
numbers=[45,-96,0,63.2,1257,-6752.2,42,3,542]
#1
numbers.sort()
print(numbers)
#2
numbers.sort(reverse=True)
print(numbers)
#3
numbers.reverse()
print(numbers)


"""2exercise"""

mevalar=["olma","o'rik","shaftoli","apelsin","malina","xurmo"]
if mevalar=="olma" or  mevalar=="malina":
    print(mevalar.upper())
else:
    print(mevalar.capitalize())


"""3-exercise"""

books={
    "jaxannamga yo'l":"keralayn",
    "xayot":"sarvinozxonim olimjanova"
}
#1 qo'shish

from math import sqrt
"""4-mahshq"""
for s in range(102,2020):
    if s <1000:
        print(s**3)
    elif s>1500:
        print(s-4)
    if s%7==0:
        print(sqrt(s))
    
"""5-mashq"""
ball=int(input("necha %  lik natida ko'rsatdingiz : "))
if ball<=64:
    print("imtihondan o'tmapsiz")
elif ball>=65 and ball<85:
    print("imtixondan o'tibsiz")
elif ball>=85 and ball<=100:
    lvl=int(input("nechinchii o'rinni oldingiz : "))
    if lvl==1:
        print(f"Siz 100 % lik grant oldiz ! ")

    elif lvl==2:
        print(f"Siz 75 % lik grant oldiz ! ")

    elif lvl==3:
        print(f"Siz 50 % lik grant oldiz ! ")

    elif lvl==4:
        print(f"Siz 25 % lik grant oldiz ! ")
elif ball<0 and ball>100:
    print("minusli son kiritmang bizda musbat son ishlamaydi")



    
    
"""___________________9b005__________________"""


