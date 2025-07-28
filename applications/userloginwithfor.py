for i in range(3):
    sifre = input("Lütfen şifrenizi  belirleyiniz ")
    if not sifre:
        print("Şifre boş olamaz, lütfen tekrar deneyiniz.")
    elif len(sifre) in range(3,8):
        print("Şifreniz başarıyla belirlendi.",sifre)
        break
    elif i ==2:
        print("3 kez yanlış deneme yaptınız, lütfen şifrenizi unutmayınız.")
    
    else:
        print("Şifreniz 3 ile 8 karakter arasında olmalıdır, lütfen tekrar deneyiniz.")
    
      
