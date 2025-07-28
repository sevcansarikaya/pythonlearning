sayi = 1

while sayi <=10:  # sayi 10'dan küçük olduğu sürece döngü devam eder
    print(sayi)  # sayi değerini ekrana yazdırır
    sayi += 1  # sayi değerini 1 artırır

liste = [1, 2, 3, 4, 5]

for i in liste:
    print(i)  # liste elemanlarını tek tek ekrana yazdırır

for i in range(20):
    print(i)  # 0'dan 19'a kadar olan sayıları ekrana yazdırır
for i in range(20):
    if i % 2 == 0:  # i çift ise
        print(i)  # i değerini ekrana yazdırır
    else:
        print(f"{i} tek sayıdır")  # i tek ise mesaj yazdırır


