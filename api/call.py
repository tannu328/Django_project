import json
import requests
data={
    "username":"admin",
    "password":"admin"
    
}
x= requests.post('http://127.0.0.1:8000/api/login/',json=data)
response=json.loads(x.text)
print(response["access_token"])