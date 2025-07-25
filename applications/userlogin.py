db_ka="admin"
db_ps=123456

while True:
    kullanici_adi=input("lütfen kullanıcı adını giriniz:")
    kullanici_ps=int(input("lütfen şifrenizi giriniz:"))

    if db_ka==kullanici_adi and db_ps==kullanici_ps:
        print("Hoşgeldiniz",kullanici_adi)
        break  # Doğru giriş yapıldığında döngüden çıkılır
        
    elif db_ka!=kullanici_adi and db_ps==kullanici_ps:
        print("Kullanıcı adınız lütfen tekrar deneyiniz.")

    elif db_ka==kullanici_adi and db_ps!=kullanici_ps:
        print("Şifreniz yanlış lütfen tekrar deneyiniz.")
        print("şifreniz değiştirilsin mi? (E/H):")
        cevap=input().strip().upper()
        if cevap == "E":
            print("şifreniz değiştiriliyor")
            yeni_sifre=int(input("lütfen yeni şifrenizi giriniz:"))
            if yeni_sifre != db_ps:
                db_ps = yeni_sifre
                print("Şifreniz başarıyla değiştirildi.")
            elif yeni_sifre == db_ps:
                print("Yeni şifreniz eski şifrenizle aynı, lütfen farklı bir şifre giriniz.")
    else:
        print("Kullanıcı adınız ve şifreniz yanlış lütfen tekrar deneyiniz.")
       

       