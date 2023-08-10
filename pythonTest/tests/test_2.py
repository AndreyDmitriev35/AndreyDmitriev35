import json
import requests
base_url='https://petstore.swagger.io/v2'
headers = {'accept': 'application/json', 'Content-Type':'application/json'}
# POST добавляем питомца
data={
"id": 0,
"category": {
"id": 0,
"name": "Tommy"
  },
"name": "doggie",
"photoUrls": [
"string"
  ],
"tags": [
    {
"id": 0,
"name": "string"
    }
  ],
"status": "available"
}
data=json.dumps(data)
res=requests.post(f'{base_url}/pet',headers=headers,data=data)
print(res.text)
print(res.json())
print(res.status_code)
# GET проверяем добавленного питомца
petId=9223372036854775807
params= {'petId':f'{petId}'}
res2 = requests.get(f"{base_url}/pet/{petId}", headers = headers, params=params)
print(res2.text)
print(res2.json())
print(res2.status_code)
# PUT вносим изменения в карточку питомца
data2={
"id": 0,
"category": {
"id": 0,
"name": "Sam"
  },
"name": "doggie",
"photoUrls": [
"string"
  ],
"tags": [
    {
"id": 0,
"name": "string"
    }
  ],
"status": "available"
}
data2=json.dumps(data2)
res3=requests.put(f'{base_url}/pet', data=data2,headers=headers)
print(res3.status_code)
print(res3.text)
print(res3.json())
# DELETE удаляем питомцв
res4 = requests.delete(f"{base_url}/pet/{petId}", headers = headers, params=params)
print(res2.text)
print(res2.json())
print(res2.status_code)