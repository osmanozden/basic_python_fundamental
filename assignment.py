#bir tıple bilgilerini değişkenlere aktarabiliriz

# tuple1 = 3,5,7

# x , y , z =tuple1
# print(x,y,z)

#eğer tuple daki nesneler yersiz olursa çalışmaz.

#eğer tuple daki nesneler fazla olursa ,onları bir değişkene dizi olarak ATAYABİLRİZ.


tuple1 = 3,5,7,9,11,13,55

x , y , *z =tuple1


print(x,y,z) #dizi olarak atamak istediğimiz değişenin başına yıldız koyarız.
print(x,y,z[-1])