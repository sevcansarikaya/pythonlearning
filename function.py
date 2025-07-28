def topla():
    a=int(input("Birinci sayıyı giriniz: "))
    b=int(input("İkinci sayıyı giriniz: "))
    toplam=a+b
    print(f"Toplam: {toplam}")


topla()

def kullanıcı_bilgileri(ad,soyad,yas,meslek):
    print(f"Kullanıcı Bilgileri:\nAd: {ad}\nSoyad: {soyad}\nYaş: {yas}\nMeslek: {meslek}")

kullanıcı_bilgileri("Ahmet", "Yılmaz", 30, "Mühendis")  # Fonksiyonu çağırır ve bilgileri ekrana yazdırır

ad= input("Adınızı giriniz: ")
soyad= input("Soyadınızı giriniz: ")
yas= int(input("Yaşınızı giriniz: "))
meslek= input("Mesleğinizi giriniz: ")
kullanıcı_bilgileri(ad, soyad, yas, meslek)  # Kullanıcıdan alınan bilgileri fonksiyona gönderir ve ekrana yazdırır


# def toplam(a, b):
#     toplam = a + b
#     print(toplam)

# a= toplam(5,5)
# b=5
# print(a+b)
#bu kodda hata var çünkü a bir değer taşımıyor bunu return ile duzeltebiliriz

def toplama(a, b):
    toplam = a + b  # a ve b'yi toplar
    return a + b  # Fonksiyonun sonucunu döndürür   

a=toplama(5, 5)  # Fonksiyonu çağırır ve sonucu a'ya atar
b=5  # b'ye 5 değerini atar
print(a + b)  # a ve b'yi toplar ve sonucu ekrana yazdırır
# Bu kodda artık a bir değer taşıyor ve toplama işlemi doğru şekilde

#varsayılan deger
def kullanıcı_bilgileri2(ad="boş bırakıldı",soyad="boş bırakıldı",yas="bu alan boş"):
    print(f"Kullanıcı Bilgileri:\nAd: {ad}\nSoyad: {soyad}\nYaş: {yas}\nMeslek: {meslek}")

kullanıcı_bilgileri2("Ahmet", "Yılmaz")  # Yaş bilgisi verilmediği için varsayılan değer kullanılır


