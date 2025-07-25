müsteri=15
if müsteri <18:
    print("maalesef müşterinin yaşı 18 den küçük")
else:
    print("müşteri 18 yaşından büyük")

müsteri_yası=int(input("Lütfen müşterinin yaşını giriniz: "))

kabul_yası=18
if müsteri_yası < kabul_yası:
    print("maalesef müşterinin yaşı 18 den küçük")
else:
    print("müşteri 18 yaşından büyük")

süt_miktarı= int(input("Lütfen süt miktarını giriniz: "))
kasar_peyniri_siniri=11

if süt_miktarı < kasar_peyniri_siniri:
    print("süt miktarınızı kaşar peyniri için uygun değil:",süt_miktarı)
    print("kaşar peyniri üretmek için ihtiyacınız olan süt miktarı:",(kasar_peyniri_siniri - süt_miktarı))
else:
    toplam_üretim=süt_miktarı/kasar_peyniri_siniri
    print(f"toplam üretim:{int(toplam_üretim)} kg kaşar peyniri üretilebilir")
