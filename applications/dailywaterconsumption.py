def su_hesapla(kilo):
    e_hesapla = kilo*0.04
    k_hesapla = kilo*0.03

    cinsiyet = input("Cinsiyetinizi giriniz (erkek/kadın): ")
    
    if cinsiyet.lower() == "erkek":
        print("*"*30)
        print(f"Cinsiyetiniz : {cinsiyet} \n Günlük su ihtiyacınız: {e_hesapla} litre")
        print("*"*30)

    elif cinsiyet.lower() == "kadın":
        print("*"*30)
        print(f"Cinsiyetiniz : {cinsiyet} \n Günlük su ihtiyacınız: {k_hesapla} litre")
        print("*"*30)

    elif not cinsiyet:
        print("Lütfen geçerli bir cinsiyet giriniz (erkek/kadın).")



kilo_al = int(input("Lütfen kilonuzu giriniz: "))
su_hesapla(kilo_al)