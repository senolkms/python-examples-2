import json

with open("users.json") as kullanici: #okutma
    data = json.load(kullanici) #veriyi okutma
    print(data[0]["name"])
    print(data[0]["email"])
    print(data[0]["address"])
    print(data[0]["address"]["street"])

for x in range(3): #3 kullanıcının
    print(data[x]["name"])
    print(data[x]["email"])
    print(data[x]["address"])