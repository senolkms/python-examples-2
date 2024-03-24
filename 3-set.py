#liste türüdür hızlı olduğu için kullanılır, indekxsiz ve sırasızdır veri tekrarı söz konusu olamaz
studentSet = {"gülse","marin","ırmak"}
studentSet2 = set(["şenol","kumaş","love"])

print(studentSet)
print(studentSet2)

for student in studentSet:
    print(student)

print("gülse" in studentSet)

if "gülse" in studentSet:
    print("Listede var")

studentSet.add("love")
print(studentSet)

studentSet.update(["şenol","love"])#birden fazla eleman eklemek için kullanılabilir.
print(studentSet)
print(len(studentSet))

studentSet.remove("şenol")
print(studentSet)

studentSet.discard("şenol")#discar: silineni tekrar silmeye kalkıştığında hata vermemesi için
print(len(studentSet))

setA={1,2,3,4,5}
setB={1,3,4,6,7,8}
#Union: ikisinde de olan elemanları verir
print(setA | setB)
print(setA.union(setB))
#intersection: aynı elemanları verir
print(setA & setB)
print(setA.intersection(setB))
#difference: birbirinden farkları
print(setA - setB)
print(setB.difference(setA))
#symmetric_difference: ikisinin birbirinden farkı kesişim hariç
print(setA ^ setB)
print(setA.symmetric_difference(setB))