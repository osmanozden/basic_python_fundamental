isim = 'Osman'
soyisim ='Ozden'
Yas='22'

print('My name is {}'.format(isim))

print("My name is {} {} and I'm {} years old.".format(isim,soyisim,Yas))

#{} sırayla indexler format fonk. 0,1,2.... gibi devam eder ,isteden değiştirebilirsin.

print(f"My name is {isim}{soyisim} and I'm {Yas} years old.") #Güzel ÖZellik 


sonuc = 300/1100

print("sonuc ->{s1:1.2}".format(s1=sonuc)) #s1:yazdırılcak başlanfıç noktası.yazırılcak son karakter
