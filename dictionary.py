sözlük={"ad":"Sevcan","soyad":"Sarıkaya","yas":25,"meslek":"Yazılım Mühendisi"}

print(sözlük["ad"])  # Sevcan
print(sözlük["soyad"])  # Sarıkaya
print(sözlük["yas"])  # 25
print(sözlük["meslek"])  # Yazılım Mühendisi
# Bu kod, bir sözlük oluşturur ve sözlükteki anahtarları kullanarak değerleri ekrana yazdırır.

print(len(sözlük))  # Sözlükteki anahtar sayısını ekrana yazdırır

for i in sözlük:  # Sözlükteki her anahtar için döngü başlatır
    print(i, sözlük[i])  # Anahtar ve değerini ekrana yazdırır

for isim,değer in sözlük.items():  # Sözlükteki her anahtar-değer çifti için döngü başlatır
    print(isim,":",değer)  # Anahtar ve değerini ekrana yazdırır




super_lig={"Galatasaray": "60 puan", "Fenerbahçe": "61 puan", "Beşiktaş": "73 puan", "Trabzonspor": "55 puan"}

takım= input("Hangi takımın puanını öğrenmek istersiniz? ").capitalize()
if takım in super_lig:
    print(f"{takım} puanı: {super_lig[takım]}")
else:
    print("Bu takım Süper Lig'de bulunmamaktadır.")

# Bu kod, bir sözlük oluşturur ve kullanıcıdan takım ismi alarak o takımın puanını ekrana yazdırır.

print(takım,":", super_lig.get(takım, "Bu takım Süper Lig'de bulunmamaktadır."))  # get() metodu ile anahtarın değerini alır, eğer anahtar yoksa varsayılan mesajı gösterir burada if bloğu kullanmayabiliriz.


#sözlüğe veri ekleme işlemleri

super_lig["Kasımpaşa"] = "45 puan"  # Sözlüğe yeni bir takım ve puan ekler
super_lig.setdefault("Sivasspor", "50 puan")  # Sözlüğe yeni bir takım ekler, eğer zaten varsa değişiklik yapmaz
print(super_lig)

takım_ekle = input("Hangi takımı eklemek istersiniz? ").capitalize()
puan_ekle = input(f"{takım_ekle} için puanı giriniz: ")
super_lig.setdefault(takım_ekle, puan_ekle)  # Kullanıcıdan alınan takım ve puanı sözlüğe ekler
#burada sonradan eklenenler kalıcı olarak kalmıyor bu sorunu daha sonra çözeceğiz.
print(super_lig)

#burada önceden eklediğimiz takımları ekranda görebiliriz
while True:
    takım_ekle = input("Hangi takımı eklemek istersiniz? ").capitalize()
    puan_ekle = input(f"{takım_ekle} için puanı giriniz: ")
    super_lig.setdefault(takım_ekle, puan_ekle)

    for i,j in super_lig.items():
        print(i,":",j)
    secim= input("Çıkmak ister misiniz? (Evet/Hayır): ").lower()
    if secim == "evet":
        print("Çıkılıyor...")
        break
    else:
        pass  # Kullanıcı çıkmak istemezse döngü devam eder

#sözlükten veri silme işlemleri
super_lig.pop("Kasımpaşa")  # Sözlükten Kasımpaşa takımını siler


