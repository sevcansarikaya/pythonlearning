import time


try:
    a = int(input("Birinci sayıyı giriniz: "))
    b = int(input("İkinci sayıyı giriniz: "))
    toplam = a/b
    print(f"Toplam: {toplam}")

except ZeroDivisionError:
    print("Bir sayıyı sıfıra bölemezsiniz!")
except ValueError:
    print("Lütfen geçerli bir sayı giriniz!")

try:
    a = int(input("Birinci sayıyı giriniz: "))
    b = int(input("İkinci sayıyı giriniz: "))
    toplam = a+b
    print(f"Toplam: {toplam}")
except ValueError:
    print("Lütfen geçerli bir sayı giriniz!")
finally:
    sayac = 5
    for i in range(sayac):
        print(f"{sayac-i} saniye sonra işlem tamamlanacak...")
        time.sleep(1)
    print("İşlem tamamlandı.")