def dikUcgenAlaniHesapla(a,b):
    return a*b/2
alan = dikUcgenAlaniHesapla(4,5)
print(alan)

#lambda: tek satırlık fonksiyonlardır
dikUcgenAlaniHesapla2 = lambda a,b : a*b/2
print(dikUcgenAlaniHesapla2(4,2))

toplama = lambda a,b : a+b
print(toplama(10,20))
print(type(toplama))