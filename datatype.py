#değişken tanımlama ve konsola yazma
isim="sevcan"
dyılı=1998
yıl=2023
yas=yıl-dyılı


print(isim+"'ın doğum yılı"+str(dyılı)+" ve yaşı "+str(yas)+"'dır.")

# Değişkenlerin tipini öğrenme
yas1=int("30")

print(type(yas1))

#yazımı düzenleme
büyükharfler="SEVCAN".lower()#upper() ile büyük harfe çevirir capitalize() ile ilk harfi büyük yapar swapcase() ile büyük harfleri küçük, küçük harfleri büyük yapar    

print(büyükharfler)


#print kullanımı

print("Merhaba", "Dünya", "!", sep=" ", end="\n")  # sep ile araya boşluk koyar, end ile satır sonu karakterini belirler

print("Merhaba", "Dünya", sep="+")  #sep ile araya koymak istediğimiz şeyi belirleyebiliriz

adı="sevcan"
soyadı="yılmaz"
yas=25

print("kişinin adı:{}, soyadı:{}, yaşı:{}".format(adı, soyadı, yas))  # format ile değişkenleri yerleştirir
print(f"{isim}'ın doğum yılı {dyılı} ve yaşı {yas}'dır.")


