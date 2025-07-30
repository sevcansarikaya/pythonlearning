import random

kullanıcılar = list()

def kullanıcı_ekle(x):
    print("Kullanıcı Ekleme Alanı")
    ekle= input("Kullanıcı Adı: ")
    kullanıcılar.append(ekle)
    print(f"{ekle} adlı kullanıcı eklendi.")


def kullanıcı_listele(x):
    say= 1
    for i in x:
        print(str(say+"kullanıcı adı: "+i))
        say+= 1


kullanıcı_ekle("kullanıcılar")
for i in kullanıcılar:
    print(i)