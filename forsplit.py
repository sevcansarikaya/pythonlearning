deneme = "sevcan sarıkaya beşiktaş"
deneme = deneme.split()  # deneme stringini boşluklardan ayırarak listeye çevirir
print(deneme)  # ['sevcan', 'sarıkaya', 'beşiktaş']
print(deneme[0])  # sevcan

deneme1=input("Lütfen bir cümle giriniz: ")
deneme1 = deneme1.split("a")  # deneme1 stringini boşluklardan

print(deneme1) 


veri_al=input("Lütfen bir cümle giriniz: ")

for i in veri_al.split():
    print(i[0],end="")  # Her kelimenin ilk harfini yazdırır, aralarında boşluk bırakmaz
