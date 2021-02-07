ogrenciler={}
numara =input("ogrenci no->")

ad =input("ogrenci ad->")


soyad =input("ogrenci soyad->")


telefon =input("ogrenci telefon->")

ogrenciler[numara]={
    "ad" :ad,
    "soyad" : soyad,
    "telefon" : telefon,
}

print(ogrenciler)