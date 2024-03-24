sayi=int(input("Sayı giriniz : "))
fak=1

if sayi<0:
    print("Negatif sayıların faktoriyeli olmaz")
elif sayi==0:
    print("Sonuç : 1")
else:
    for x in range(1,sayi+1):
        fak = fak * x
    print(fak)