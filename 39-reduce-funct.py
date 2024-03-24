sayilar = [1,2,3,4,5]
from functools import reduce
def buyukkucuk(x,y):
    if x>y:
        return x
    return y
sss= reduce(buyukkucuk,sayilar)
print(sss)

#faktoriyel
#sayilarFaktoriyel = reduce(lambda x,y: x*y,sayilar)

#print(sayilarFaktoriyel)

