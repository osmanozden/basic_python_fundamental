import random
x = int(random.randrange(5,100))
print(x)
hak = int(input("Kaç Hakkınızın OLmasını İstersiniz :"))
if hak>5:
    print("5 den daha hazla hak a sahip olmazsınız.")
    while hak >5:
        hak = int(input("Kaç Hakkınızın OLmasını İstersiniz :"))
a = 0
while hak >0:
    a = int(input("Lutfen bir sayi giriniz : "))
    if a<x:
        print("Girdiginiz sayidan daha B Ü Y Ü K bir deger giriniz!")
    elif a==x :
        print(f"Tebrikler Buldunuz sayi {x}")
        break
    else:
            print("Girdiginiz sayidan daha K Ü Ç Ü K bir deger giriniz")
    hak-= 1
if hak ==0 and a!=x:
    print("Ne yazık ki oyunu kaybettiniz->")
p =(5-hak)*20
print(f"Tolam Puanınız ({p}")


