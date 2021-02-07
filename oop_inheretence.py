class kisi():
    def __init__(self):
        print('Burası kisi-->')
class ogrenciler(kisi):
    def __init__(self):
        kisi.__init__(self) #Burda kaltım yapıyoruz,   #Aytıca buna yazmasak,kisi class ı çağrılmaz buna override denir.                  
        print('Burası Ögrenciler-->') #yani bir diğer class ın özelliklerinide olaya dahil ediyoruz.

s1 = ogrenciler()
