sayi=int(input("Sayı Giriniz: "))
if sayi>1:
    for i in range(2,sayi):
       if(sayi%i)==0:
           print(sayi,"Asal sayı değildir")
           break
    else:
        print(sayi,"Asal sayıdır")
else:
    print(sayi,"Asal sayı değildir")
#bool kullanım
sayi=int(input("Sayı Giriniz: "))
asalMi= True
for i in range(2,sayi):
    if (sayi%i)==0:
        asalMi= False
        break
if asalMi:
    print("Asal")
else:
    print("Asal değil")