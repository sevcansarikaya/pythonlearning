import subprocess as sp

psw="1234"
kullanıcı_sifre = input("Lütfen şifrenizi giriniz: ")

if kullanıcı_sifre == psw:

    print("Şifre Doğru, Uygulama Açılıyor...")
    while True:
        print("Uygulama Ekranına Hoş Geldiniz")
        print("Aşağıdaki uygulamalardan birini seçebilirsiniz:")
        print("1-NotePad\n2-Safari\n3-Hesap Makinesi")
        secim_yap = input("Seçiminizi yapınız: ")

        if secim_yap == "1":
            sp.call(["open","-a","Notes"])
            input("Notepad uygulaması açıldı. Devam etmek için bir tuşa basın...")
        elif secim_yap == "2":
            sp.call(["open","-a","Safari"])
            input("Safari uygulaması açıldı. Devam etmek için bir tuşa basın...")
        elif secim_yap == "3":
            sp.call(["open","-a","Calculator"])
            input("Hesap Makinesi uygulaması açıldı. Devam etmek için bir tuşa basın...")
        else:
            print("Geçersiz seçim. Lütfen 1, 2 veya 3 girin.")

else:
    print("Şifre Yanlış")