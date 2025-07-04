import json
import requests
# import Django_project.djangoapi_app.views.py from Usergenericview


data = {
    "username": "admin",
    "password": "admin"
}

login_response = requests.post('http://127.0.0.1:8000/api/login/', json=data)
login_json = login_response.json()

access_token = login_json["access_token"]
# print("Access Token:", access_token)


headers = {
    "Authorization": f"Bearer {access_token}"

    #  "Authorization":"Bearer MYREALLYLONGTOKENIGOT"

}

user_response = requests.get('http://127.0.0.1:8000/api/users/1', headers=headers)










def save(file_path, user_response):
    with open(file_path, 'w') as file:
        json.dump(user_response, file, indent=4)


if user_response.status_code == 200:
    users = user_response.json()
    print("Users Data:")
    print(json.dumps(users, indent=2))

    file_path = 'user.json'
    save(file_path, users)

    
else:
    print("Failed to fetch users:", user_response.status_code, user_response.text)