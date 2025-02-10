"""vorislik klassi yani ota klass"""
class Shaxs():
    """ota klassi va ona klassi  
    men o'lganimdan keyin merosni bola klassiga otkizb berdim 
    imzo:_____________, kun:28,01,2025"""
    
    def __init__(self,ism,familya,sharf,t_yil,passport,friends: list,millat,meros):
        self.ism = ism
        self.familya = familya
        self.sharf = sharf
        self.t_yil = t_yil
        self.passport = passport
        self.millat = millat
        self.meros = meros
        self.friends = friends  




    def __str__(self):
        return f'Ism: {self.ism}, Familya: {self.familya}, Sharf: {self.sharf}, Tugilgan yil: {self.t_yil}, Passport: {self.passport}, Millat: {self.millat}'

    def get_info(self):
        """Get information"""
        return f'Ism: {self.ism}, Familya: {self.familya}, Sharf: {self.sharf}, Tugilgan yil: {self.t_yil}, Passport: {self.passport}, Millat: {self.millat} meros:{self.meros}'

    def get_age(self,h_yil):
        """Get age"""
        return h_yil - self.t_yil

    def get_psprt(self):
        """Get passport"""
        return self.passport

    def get_millat(self):
        """Get citizenship"""
        return self.millat
    def get_meros(self):
        """Get meros"""
        return self.meros
    def get_friends(self):
        """Get friends"""
        return self.friends
# class Bola(Shaxs):
#     """ota ona klassi meros qolgan bolani klasi"""
#     def __init__(self, ism, familya, sharf,meros, t_yil, passport, millat,bola_turi,qachonmerosiolgani):
#         super().__init__(ism, familya, sharf, t_yil, passport, millat,meros)
#         self.bola_turi = bola_turi
#         self.qachonmerosiolgani = qachonmerosiolgani
#     def get_info(self):
#         return super().get_info() + f', Bola turi: {self.bola_turi}, Qachon merosiolgani: {self.qachonmerosiolgani}'
#     def get_bolaturi(self):
#         """Get bola type"""
#         return self.bola_turi
#     def get_qachonmerosiolgani(self):
#         """Get bola losing method"""
#         return self.qachonmerosiolgani

# bola1=Bola("Naima","malikova","murodovna","klassdan klassga o'tish ",2009,"AN12345666","ozbek","qiz ","2028.08.08")

# print(bola1.get_info())

class Talaba(Shaxs):
    """vorislik talabasi """
    def __init__(self, ism, familya, sharf, t_yil, passport, millat, meros, friends:list ,tugilgan_yil,baxolar:list,sinf:str,maktab:str):
        super().__init__(ism, familya, sharf, t_yil, passport, millat, meros,friends)
        # self.kurs = kurs
        self.tugilgan_yil = tugilgan_yil
        self.baxolar = baxolar
        self.sinf = sinf
        self.maktab = maktab
    def get_sinf(self):
        """Get education information"""
        return f'Sinf: {self.sinf}, Maktab: {self.maktab}'
    def set_sinf(self,new_sinf):
        """sinfini o'zgarturivchi funksiya """
        self.sinf = input("Sinfni kiriting: ")
        return self.sinf
    def get_maktab(self):
        """Get educational institution"""
        return self.maktab
    def get_age(self, h_yil):
        return f"{self.ism} ning yoshi {h_yil-self.t_yil}"
    def set_maktab(self,new_maktab):
        """Maktabni o'zgarturivchi funksiya """
        self.maktab = input("Maktabni kiriting: ")
        return self.maktab
    def get_friends(self):
        """studentning dostlarini chiqarib beradi"""
        return f"{self.ism} ning  eng qalin dost {self.friends[0]}"
    def get_info(self):
        """Get information"""
        return super().get_info() + f', Tugilgan yil: {self.tugilgan_yil}, Baxolar: {self.baxolar}, Sinf: {self.sinf}, Maktab: {self.maktab}'
        # return f'Ism: {self.ism}, Familya: {self.familya}, Sharf: {self.sharf}, Tugilgan yil: {self.t_yil}, Passport: {self.passport}, Millat: {self.millat}, Kurs: {self.kurs}'
    def get_average_grade(self):
        """Get average grade"""
        return sum(self.baxolar)/len(self.baxolar)

talaba1=Talaba("Naima","malikova","murodovna",2009,"AN12345666","ozbek","klassdan klassga otish"["sarvinoz","naima","moxlaroy","raxima","oydinoy","oytovoq","mubina","abdulaxad","yusufbe","zinnurbe","abdurouf"],[90,85,95,88,92],"Talabadan talabaga o'tish","O'quv tashkiloti")
# print(talaba1.get_average_grade)
print(talaba1.get_friends())
# print(talaba1.get_info())

# talaba1.set_sinf("Talabadan talabaga o'tish")

# print(talaba1.get_sinf())

# talaba1.set_maktab("O'quv tashkiloti")

# print(talaba1.get_maktab())




"""mashq"""
class Texnik():
    def __init__(self,ism, narx, turi):
        super().__init__(ism, narx)
        self.turi = turi
        self.xarajat = []
        self.fayl = []
        self.xodim = []
    

class noutbuk(Texnik):
    """noubuk xaqida informatsiya beradi texnik klassidan vori qolgan klass"""
    def __init__(self,ism, narx, turi, qiymatlar):
        super().__init__(ism, narx, turi)
        self.qiymatlar = qiymatlar
        self.narx=narx
    def get_info(self):
        return f'Ism: {self.ism}, Narx: {self.narx}, Turi: {self.turi}, Qiymatlar: {self.qiymatlar}'
    def add_narx(self):
        self.narx += input("Qiymatni qo'shing: ")
        return self.narx
    def get_narx(self):
        """narxini chiqarib beradi """
        return self.narx

