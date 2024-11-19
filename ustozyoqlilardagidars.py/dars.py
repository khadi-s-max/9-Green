ismlar=["Sarvinoz","hadicha",'naima','raxima','moxlaroy',"mubina","oydinoy","yusufbe",'abdulaxad','zinnurbek']
shart=['100 marta tushib chiqadi',"100 marta otirp turish",'shokolad op kelish',"naimani quchoqlash","moxlarni sochini qirqish",]
import random
# print(random.randrange(0,10))
# print(random.randrange(0,5))

print(ismlar[random.randrange(0,len(ismlar))])

print(shart[random.randrange(0,len(shart))])
while True:
    
    yosh = input("Iltimos, yoshingizni kiriting (exit yoki quit deb yozsangiz dastur to'xtaydi): ").lower()
                                                                                                          
   
    if yosh== 'exit' or yosh== 'quit':
        print("Dastur to'xtadi ")
        break 
    
    
    if yosh.isdigit():
        yosh = int(yosh)  
        
        if yosh < 7:
            narh = 2000
        elif 7 <= yosh < 18:
            narh = 3000
        elif 18 <= yosh < 65:
            narh = 10000
        else:
            narh = 0  
        if narh == 0:
            print("Sizga chipta bepul!")
        else:
            print(f"Chipta narhi: {narh} so'm")
    else:
        print("Iltimos, yoshni togri kiriting!")
