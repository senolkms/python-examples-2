sayilar = [1,2,3,4,5,6]

sayilarKaresi = list(map(lambda sayi: sayi*sayi,sayilar))

sayilarFiltreli = list(filter(lambda sayi:sayi>3,sayilar))
#for sayi in sayilar:
#    sayilarKaresi.append(sayi*sayi)

print(sayilarKaresi)
print(sayilarFiltreli)