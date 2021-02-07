usersCars = ["BMW","MERCEDES","OPEL","MAZDA"] #1

print(len(usersCars)) #2

print(usersCars[0]," ",usersCars[-1]) #3

usersCars[3]="TOYOTA"
print(usersCars)  #4

print(usersCars in "MERCEDES")

print(usersCars[-2]) #5

print(usersCars[:2]) #6

usersCars[-1] = "RENAULT"
usersCars[-2] = "TOYOTA" #7

usersCars += "AUDI","NISSAN"
print(usersCars) #8

usersCars.remove("NISSAN")
print(usersCars)  #9

# usersCars.pop(-1)
# print(usersCars) -->İNDEX TEKİ BİR ELEMANI SİLMEK İÇİN pop() METHODU,BİR ELEMAN SİLMEK İÇİN remove() METHODU KULLANILIR.

print(usersCars[::-1]) #10

s1 =["YİGİT","BİLGİ",2010,[70,60,70]]  #LİSTE İÇİNDE LİSTE SAKLAYABİLİYORUZ.BU ŞEKİLDE








