x=5
y=5

x+=y
print(x)  
x**=y
print(x)  
x-=y
print(x)  

deneme= 5==5
print(deneme)  # deneme now equals True

db=1234

kullanıcı_sifre = int(input("Lütfen şifrenizi giriniz: "))

if kullanıcı_sifre == db:
    print("Şifre doğru, giriş başarılı!")
else:
    print("Şifre yanlış, lütfen tekrar deneyiniz.")

kontrol= db==kullanıcı_sifre
print(kontrol)  # kontrol now equals True if the password matches, otherwise False

deneme1= 5!=5
print(deneme)

deneme2= 5>5
print(deneme)

deneme3= 5<5
print(deneme)

deneme4= 9>7 and 7<9
print(deneme4)  # deneme4 now equals True

db_ps="1234" 
db_kullanıcı_adı="admin"
kullanıcı_adı = input("Lütfen kullanıcı adınızı giriniz: ")
kullanıcı_sifre = input("Lütfen şifrenizi giriniz: ")

kontrol=db_ps==kullanıcı_sifre and db_kullanıcı_adı==kullanıcı_adı
print(kontrol)  # kontrol now equals True if both username and password match
