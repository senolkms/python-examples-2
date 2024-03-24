def topla(sayi1,sayi2):
    return sayi1 + sayi2
def cikar(sayi1,sayi2):
    return sayi1 - sayi2
def carp(sayi1,sayi2):
    return sayi1 * sayi2
def bol(sayi1,sayi2):
    return sayi1 / sayi2
print("1 : Topla")
print("2 : Çıkar")
print("3 : Çarp")
print("4 : Böl")
sayi1 = int(input("Birinci Sayı: "))
sayi2 = int(input("İkinci Sayı: "))

secenek = int(input("İşlemi seçiniz: "))

if secenek == 1:
    print("Toplam: "+ str(topla(sayi1,sayi2)))
elif secenek == 2:
    print("Farkı: "+ str(cikar(sayi1,sayi2)))
elif secenek == 3:
    print("Çarpımı: "+ str(carp(sayi1,sayi2)))
elif secenek == 4:
    print("Bölümü: "+ str(bol(sayi1,sayi2)))
else:
    print("Geçersiz seçenek")