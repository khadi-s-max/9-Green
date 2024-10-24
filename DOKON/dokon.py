"""21|10|2024|"""
# dastur:necha aylana yugurish kk :
# foydalanvchi:25
# d:Biz yugurishni boshladik!
# d:1-aylana tugadi!
# d:2-aylana tugadi!
# d:3-aylana tugadi!
# ....
# d:25-aylana tugadi !
# d:biz aylanani tugattik!
# d: o'tirsak maylimi

# if 
# f:ha
# d:rahmat

# elif 
# f:yo'q
# d:yana qancha yugurush kk 
"""
s=int(input("Necha krug aylanish kerak ? "))
print("Biz yugurisni boshladik ")

for n in range(s):
    print(f"{n+1}-aylana tugadi!")
print("Biz aylanani tugattik!")


d=input("O;tirsak bo;ladimi ").lower() 
if d=="ha":
    print("rahmat")
            
elif d=="yo'q":
    print("yana qancha yugurish kerak : ")
"""


"""zoo project1 """
yosh=int(input("yoshingizni kiritng : "))
if yosh <0 and yosh<=7:
    print(f"sizga kirish 5.000")
elif yosh>7 and yosh <=18:
    print(f"sizga kirish 10.000")
elif yosh >18 and yosh <=70:
    print(f"Sizga kirish 25.000")
elif yosh>70 and yosh>=100:
    print(f"Sziga kirish bepul ")
elif yosh >100 and yosh <=120:
    print("siz o'liksiz👻")
elif yosh<0:
    print("siz xali tugulmapsiz to'gri son kiriting : ")
    