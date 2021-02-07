class cember :
    pi = 3.14
    def __init__(self,yaricap=1):
        self.yariCap = yaricap

    def cevreHesapla(self):
        return 2*self.pi*self.yariCap
    def alanHesapla(self):
        return self.pi*self.yariCap*self.yariCap 
c1=cember(5)
print(int(c1.cevreHesapla()))
print(float(c1.alanHesapla()))

