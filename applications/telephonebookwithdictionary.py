tel_rehberi = dict()  # Telefon rehberi için boş bir sözlük oluşturur

def rehbere_kaydet(x):
    print("Numara Ekleme Alanına Hoşgeldiniz")
    numara_isim_al=input("Lütfen Kayıt Edilecek Kişinin Adını Giriniz: ")
    numara_tel_al=input("Lütfen Kayıt Edilecek Kişinin Telefon Numarasını Giriniz: ")

    x = tel_rehberi.setdefault(numara_isim_al, numara_tel_al)  # Kullanıcının girdiği isim ve telefon numarasını sözlüğe ekler
    print(f"{numara_isim_al} isimli kişi rehbere kaydedildi.")

def tel_rehberi_goruntule(x):
    print("Rehberdeki Kişiler:")
    for isim, numara in x.items():  # Sözlükteki her anahtar-değer çifti için döngü başlatır
        print(f"{isim}: {numara}")  # İsim ve telefon numarasını ekrana yazdırır

def tel_no_sil(x):
    isim_sil = input("Silmek istediğiniz kişinin adını giriniz: ")
    if isim_sil in x:
        del x[isim_sil]  # Sözlükten istenen kişiyi siler
        print(f"{isim_sil} rehberden silindi.")
    else:
        print(f"{isim_sil} rehberde bulunamadı.")

while True:
    print("Telefon Rehberi Uygulamasına Hoşgeldiniz")
    print("1. Rehbere Kişi Ekle")
    print("2. Rehberi Görüntüle")
    print("3. Rehberden Kişi Sil")
    print("4. Çıkış")

    secim = input("Lütfen bir seçenek giriniz (1/2/3/4): ")

    if secim == "1":
        rehbere_kaydet(tel_rehberi)  # Rehbere yeni bir kişi ekler
    elif secim == "2":
        tel_rehberi_goruntule(tel_rehberi)  # Rehberdeki kişileri görüntüler
    elif secim == "3":
        tel_no_sil(tel_rehberi)  # Rehberden bir kişiyi siler
    elif secim == "4":
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")  # Geçersiz seçim yapıldığında kullanıcıyı bilgilendirir






#silmek için başka bir seçenek
# def no_sil(x):
#     silinecek_kisi= input("Silmek istediğiniz kişinin adını giriniz: ")
#     x=tel_rehberi.pop(silinecek_kisi, None)  # Sözlükten istenen kişiyi siler, eğer kişi yoksa hata vermez


