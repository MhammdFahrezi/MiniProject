
# class Mobil:
#     def __init__(self,warna1="putih", kecepatan=0):
#         # print("ini adalah konstruktor")
#         self.warna = warna1
#         self.kecepatan = kecepatan

#     def getwarna(self): 
#         return self.warna 

    
# mobil1 = Mobil() 
# mobil2 = Mobil("hijau")
# class Bioma:
#     def __init__(self, flora1="anggrek", fauna1="dugong"):
#         self.flora = flora1 
#         self.fauna = fauna1

#     def getFlora(self):
#         return self.flora

#     def getFauna(self):
#         return self.fauna

# bioma1 = Bioma()
# bioma2 = Bioma("mawar")
# print ("bioma")

class Bioma:
    def __init__(self, flora1="anggrek", fauna1="dugong"):
        self.flora = flora1 
        self.fauna = fauna1

    def getFlora(self):
        return self.flora

    def getFauna(self):
        return self.fauna

bioma1 = Bioma()
bioma2 = Bioma("mawar","kucing")

print("Bioma 1:")
print("Flora:", bioma1.getFlora())
print("Fauna:", bioma1.getFauna())

print("\nBioma 2:")
print("Flora:", bioma2.getFlora())
print("Fauna:", bioma2.getFauna())
