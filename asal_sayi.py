sayi =int(input("Lufen bir sayi giriniz->"))


if sayi == 1:
    print("SAYİ ASAL DEĞİLDİR")

for i in range(2,sayi):
    if sayi%i==0 :
        if sayi != i:
            print("SAYİ ASAL DEĞİLDİR")
            break
    else:
        print("sayi asal")
        break