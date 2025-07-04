import requests
import json
user='http://127.0.0.1:8000/api/users/'
# user_id='http://127.0.0.1:8000/api/users/<id>'

user_input=input("enter the function you want to perfrom(get/post/delete/patch):").strip().lower()


def get_users():
    response = requests.get(user)
    print("Users:")
    print(response.json())

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    data = {'username': name, 'email': email,'password':password}
    response = requests.post(user, json=data)
    print(response.json())

def update_user(full=False):
    user_id = input("Enter the ID of the user to update: ")
    name = input("Enter name: ")
    email = input("Enter email: ")
    data = {'username': name, 'email': email}
    # if full:
        # response = requests.put(user + f'{user_id}/', json=data)
    # else:
    response = requests.patch(user+f'{user_id}' , json=data)
    print(f"Status Code: {response.status_code}")


    if response.text.strip():  # if there's any response body
        try:
            print(response.json())
        except ValueError:
            print("Response is not valid JSON. Raw response:", response.text)
    else:
        print("Update successful. No content returned.")


def delete_user():
    user_id = input("Enter the ID of the user to delete: ")
    response = requests.delete(user + f'{user_id}')
    print(response.json())


if user_input == 'get':
    get_users()
if user_input == 'patch':
    update_user()
if user_input == 'post':
    create_user()
if user_input == 'delete':
    delete_user()

# print("Status Code:", response.status_code)
# print("Response JSON:", response.json())

