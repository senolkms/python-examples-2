#f=open("musteriler.txt","w")  W dosya oluşturur, yazar
#f=open("musteriler.txt","r")  R okur
#f=open("musteriler.txt","a")  A dosyayı okur,ekleyebilir
#f=open("musteriler2.txt","x") X oluşturur
f = open("musteriler.txt","r")
print(f.read())
print("*********")
for l in f:
    print(l)
