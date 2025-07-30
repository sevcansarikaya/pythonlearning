import module_import1 #bu kod module.py dosyasındaki topla fonksiyonunu kullanmak için import ediyor
import random # random modülünü içe aktarır, rastgele sayılar üretmek için kullanılabilir
from datetime import datetime # datetime modülünden datetime sınıfını içe aktarır, tarih ve saat işlemleri için kullanılabilir
module_import1.topla() # module_import.py dosyasındaki topla fonksiyonunu çağırır ve çalıştırır

# import module_import as mod # Bu kod, module_import.py dosyasını mod adıyla içe aktarır tekrardan uzun adlar yazmaya gerk duymayız 
# mod.topla() # mod adıyla içe aktarılan module_import.py dosyasındaki topla fonksiyonunu çağırır ve çalıştırır

# from module_import import topla # Bu kod, module_import.py dosyasındaki topla fonksiyonunu doğrudan içe aktarır
# topla() # topla fonksiyonunu çağırır ve çalıştırır

a=random.random() # random modülünden rastgele bir sayı üretir
print(a) # Üretilen rastgele sayıyı ekrana yazdırır

b= random.randint(200,290)
print(b)


liste=["sevcan","sarıkaya","python","modül","import"]

c=random.choice(liste) # liste içinden rastgele bir eleman seçer
print(c) # Seçilen rastgele elemanı ekrana yazdırır

d= datetime.now() # Şu anki tarih ve saati alır
print(d) # Alınan tarih ve saati ekrana yazdırır

#d = d.yaer yazarak sadece yılı yazdırabiliriz

tam_tarih = d.strftime("%d/%m/%Y") # Tarihi belirli bir formatta string olarak alır
print(tam_tarih) # Formatlanmış tarihi ekrana yazdırır

# %a hafta günün kısaltılmış hali
# %A hafta günün tam hali
# %b ayın kısaltılmış hali
# %B ayın tam hali
# %d gün
# %m ay
# %Y yıl
# %c tam tarih ve saat
# %jbelirli bir tarihin yılın kaçınıcı günü olduğunu gösterir
