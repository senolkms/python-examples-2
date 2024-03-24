import json
data = '{"ad":"Senol","soyad":"Kumas"}'
a = json.loads(data) #jsona çevirme
print(a["ad"])
print(a["soyad"])

customer = {
    "ad":"marin",
    "email":"senol@gmail.com"
}
customerJson = json.dumps(customer)#sözlüğü jsona çevirme
print(customer)