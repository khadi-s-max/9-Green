
class Avto:
    """Avtomobil klassi"""

   

    # def __init__(self,make,model,rang,yil,narh,km=0):
    #     self.make=make 
    #     self.model=model 
    #     self.rang=rang 
    #     self.yil=yil
    #     self.narh=narh
    #     self.km=km

    # def modell(self):
    #     modelll=f"mashina modeli : {self.model} \n mashina yili:  {self.narh}"
    #     return modelll
    # def get_info(self):
    #     """mashinani malumotini beradi """
    #     info=f"mashinani malumotlari \n {self.model} \n {self.model} \n {self.rang} " 
    #     return info 
   

# avto1=Avto("GM","damas","oq",96.000,2024)
# print(avto1.modell())

class Talaba():
    """talaba"""
    def __init__(self,ism,familya,yosh,baxolar:list , friends:list, kusr=2):
         self.ism=ism
         self.familya=familya
         self.yosh=yosh
         self.baxolar=baxolar
         self.kusr=kusr
         self.friends=friends
    
    def get_info(self):
        return f"talabani malumotlari \n {self.ism} \n {self.familya} \n {self.yosh} \n {self.baxolar}"
    def baxola1(self):
        
        return sum(self.baxolar)/len(self.baxolar)
    def get_fullname(self):
        """studentning to'liq ismini chiqarib beradi"""
        return f"{self.ism} {self.familya}"
    def get_age(self,now=2025):
        """studentning yoshini chiqarib beradi"""
        return self.yosh - now
    def get_friends(self):
        """studentning dostlarini chiqarib beradi"""
        info=f"{self.ism} ning do'stlari : "
        for ism in self.friends:
            info+=f" {ism} "
        return info


durbek=Talaba("xadicha","botirova",15, [1,3,5,4,2,3,4],["sarvinoz","naima","moxlaroy","raxima","oydinoy","oytovoq","mubina","abdulaxad","yusufbe","zinnurbe","abdurouf"] ,2)
print(durbek.get_info())
print(durbek.baxola1())

print(durbek.get_fullname())

print(durbek.get_age())

print(durbek.get_friends())
