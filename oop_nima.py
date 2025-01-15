
class Avto:
    """Avtomobil klassi"""

   

    def __init__(self,make,model,rang,yil,narh,km=0):
        self.make=make 
        self.model=model 
        self.rang=rang 
        self.yil=yil
        self.narh=narh
        self.km=km

    def modell(self):
        modelll=f"mashina modeli : {self.model} \n mashina yili:  {self.narh}"
        return modelll
    # def get_info(self):
    #     """mashinani malumotini beradi """
    #     info=f"mashinani malumotlari \n {self.model} \n {self.model} \n {self.rang} " 
    #     return info 
   

avto1=Avto("GM","damas","oq",96.000,2024)
print(avto1.modell())


