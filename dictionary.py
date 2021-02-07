#Bir key birde volue bilgisi ile çaışmasını istedğimiz ifadeler {} ile kullanılır -->

# sozluk1 ={"ADAPAZAR":54,"İSTANBUL":34,"SAMSUN":55}



# print(sozluk1["ADAPAZAR"]) #BU SEKİLDE CALISIRLAR.

# sozluk1["ADAPAZAR"] =99 #SONRADAN BU SEİLDE ATAMA YAPILABİLİR.


# print(sozluk1)


#İç İçe SÖZLÜKLER EKLEYEBİLİYORUZ.

kullanicilar={
    "osmanozden":{
        "roller":["yonetici","misafirKullanici"],
        "email":"ozden.osman@hotmail.com",
        "telefon":"53662",
        "dogumYili":1998,
        #"yas":2020-int(kullanicilar["osmanozden"]["dogumYili"])
        
    }
}

print(kullanicilar["osmanozden"]["yas"])