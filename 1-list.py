ogrenciler=["ali","veli","deli"]
print(ogrenciler)
ogrenciler.append("ahmet")
print(ogrenciler[2])
ogrenciler.remove("ali")
print(ogrenciler)
#list constructor
sehirler= list(("Ankara","İstanbul","Ankara"))
print(sehirler)
print(len(sehirler))
#diğer
#print(sehirler.clear())
print("Ankara sayısı = "+ str(sehirler.count("Ankara")))
print("Ankara sırası = "+ str(sehirler.index("İstanbul")))
sehirler.pop(1) #indekse göre silme
sehirler.insert(0,"Trabzon")
print(sehirler)
sehirler.reverse()#tersten sıralama
print(sehirler)

sehirler2=sehirler.copy()
print("İkinci dizi = "+str(sehirler2))
sehirler2[0]="İzmir"
sehirler.extend(sehirler2)#birleştirme
sehirler.sort()#alfabetik sıralama
print(sehirler)