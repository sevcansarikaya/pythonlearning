import random
import time

kullanıcılar = list()

def kullanıcı_ekle(x):
    print("*"*30)

    print("Kullanıcı Ekleme Alanı")
    ekle= input("Kullanıcı Adı: ")
    kullanıcılar.append(ekle)
    print(f"{ekle} adlı kullanıcı eklendi.")

    print("*"*30)



def kullanıcı_listele(x):
    print("*"*30)

    say= 1
    for i in x:
        print(str(say)+".Kullanıcı Adı: "+i)
        say+= 1
    print("*"*30)
    

def sec(x):
    print("*"*30)
    say=1
    kisi_sec =int( input("Kaç Kullanıcı Seçilsin:"))
    rastgele_sec= random.sample(x, kisi_sec)

    for i in rastgele_sec:
        print("Kişi Sistemden Çekiliyor...")
        time.sleep(2)
        print(str(say)+".Kullanıcı Adı:",i)
        say+=1
    print("*"*30)
    

def salla(x):
    print("*"*30)

    say=1
    random.shuffle(x)
    for i in x:
        print(str(say)+"kullanıcı adı:",i)
        say+=1
    
    print("*"*30)


while True:
    print("Kullanıcı Ekranına Hoş Geldiniz")
    print("1- Kullanıcı Ekle")
    print("2- Kullanıcı Listele")
    print("3- Rastgele Kullanıcı Seç")
    print("4- Kullanıcıları Karıştır")
    print("5- Çıkış")

    secim = input("Seçiminizi yapınız: ")

    if secim == "1":
        kullanıcı_ekle(kullanıcılar)
    elif secim == "2":
        kullanıcı_listele(kullanıcılar)
    elif secim == "3":
        sec(kullanıcılar)
    elif secim == "4":
        salla(kullanıcılar)
    elif secim == "5":
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
