ates_durumu=float(input("lütfen ateş derecenizi giriniz:"))
oksuruk=input("öksürüğünüz var mı? (evet/hayır): ").strip().lower()
bas_agrisi=input("baş ağrınız var mı? (evet/hayır): ").strip().lower()
gun=int(input("hastalık kaç gündür devam ediyor?: "))

if ates_durumu>=39:
    if gun >=3:
        print("**uyarı hastaneye gidiniz**")
    else:
        print("ateşiniz zyüksek devam ederse hastaneye gidiniz.")

if (ates_durumu>=38) and (oksuruk=="evet") and (bas_agrisi=="evet") and (gun>=3):
    print("**acil uyarı hastaneye gidiniz**")

elif(oksuruk=="evet") or (bas_agrisi=="evet") or (gun>=3):
    print("**hatırlatma böyle devam ederseniz hastaneye gidiniz**")

else:
    print("sağlığınız iyi görünüyor, geçmiş olsun!")
print("lütfen kendinize dikkat edin!")
   