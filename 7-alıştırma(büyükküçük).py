sayi1=int(input("1.Sayıyı giriniz: "))
sayi2=int(input("2.Sayıyı giriniz: "))
sayi3=int(input("3.Sayıyı giriniz: "))

if sayi1>sayi2 and sayi1>sayi3:
    print("1.Sayı en büyüktür.")
elif sayi2>sayi3:
    print("2.Sayı en büyüktür.")
else:
    print("3.Sayı en büyüktür.")