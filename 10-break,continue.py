sehirler= ["Ankara","İstanbul","İzmir"]

for sehir in sehirler:
    if sehir=="İstanbul":
        #continue:sadece belirtilen şartı çalıştırma
        break#belirtilen şart gerçekleşince döngüden çık
    print(sehir + " için kod = "+sehir[0:3])
    print("*********")
print("Break çalıştı...")