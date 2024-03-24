import sys

liste = [7,'senol',0,3,"6"]

for x in liste:
    try:
        print("Sayı: "+str(x))
        sonuc = 1/int(x)
        print("Sonuç : "+ str(sonuc))
    #except ValueError:
    #    print(str(x)+ " bir sayı değil")
    #except ZeroDivisionError:
    #    print(str(x)+ " için 0 a bölme hatası")
    except:
        print(str(x)+" hesaplanamadı")
        print("Sistem diyor ki ... " + str(sys.exc_info()[0]))
    finally:
        print("İşlem bitti")