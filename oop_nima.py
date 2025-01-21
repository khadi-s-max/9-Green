
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

# class Talaba():
#     """talaba"""
#     def __init__(self,ism,familya,yosh,baxolar:list , friends:list, kurs=2):
#          self.ism=ism
#          self.familya=familya
#          self.yosh=yosh
#          self.baxolar=baxolar
#          self.kusr=kurs
#          self.friends=friends
    
#     def get_info(self):
#         return f"talabani malumotlari \n {self.ism} \n {self.familya} \n {self.yosh} \n {self.baxolar}"
#     def baxola1(self):
        
#         return sum(self.baxolar)/len(self.baxolar)
#     def get_fullname(self):
#         """studentning to'liq ismini chiqarib beradi"""
#         return f"{self.ism} {self.familya}"
#     def get_age(self,now=2025):
#         """studentning yoshini chiqarib beradi"""
#         return now-self.yosh
#     def get_friends(self):
#         """studentning dostlarini chiqarib beradi"""
#         info=f"{self.ism} ning do'stlari : "
#         for ism in self.friends:
#             info+=f" {ism} "
#         return info
#     def set_kurs(self):
#         if self.kurs < 6 : 
#             self.kurs+=1
#         else:
#             return "siz hozirda oxirgi tabaqadasz"
#         return self.kurs

# xadicha=Talaba("xadicha","botirova",15, [1,3,5,4,2,3,4],["sarvinoz","naima","moxlaroy","raxima","oydinoy","oytovoq","mubina","abdulaxad","yusufbe","zinnurbe","abdurouf"] ,2)
# print(xadicha.get_info())
# print(xadicha.baxola1())

# print(xadicha.get_fullname())

# print(xadicha.get_age())

# print(xadicha.get_friends())



"""get_info() kutubxona xaqida umumiy malumot 
add_books(kitob nomi) kitob qo'shadigan funksiya 
get book() - kutubxonadagi kitoblraning nomini chiqarib beruvchi funksiya """

class Library():
    """kutubxona classi """
    def __init__(self, name:str , adress:str):
        self.name=name
        self.adress=adress
        self.books=[]
        self.books_count=0

    def get_info(self):
        """kutubxona xaqida umumiy malumot beruvchi funksiya """
        return f"Bu kutubxona xaqida malumot {self.name}  manzili {self.adress} , {self.books_count} "
    def add_book(self , book ):
        """kitob qo'shadigan funksiya """

        self.books.append(book)
        self.books_count+=1
        return f"{book} kitob qo'shildi"

    def get_books(self):
       " kutubxonadagi kitoblarni nomini chiqarib beruvchi "
       info=f"{self.name} kitoblari nomi :" 
       for book in self.books:
        info+=f" {book} "
       return info


library=Library("Nodirabegim ","5A")


library.add_book("O'zbek tili")
library.add_book("ona tili")
print(library.get_info())
print(library.get_books())


