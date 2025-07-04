import requests
import json

class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url 

    def get_users(self):
        response = requests.get(self.base_url)
        user=response.json()
        print(json.dumps(user,indent=5))

    def create_user(self):
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        data = {'username': name, 'email': email, 'password': password}
        response = requests.post(self.base_url, json=data)
        user=response.json()
        print(json.dumps(user,indent=5))

    def update_user(self):
        user_id = input("Enter the ID of the user to update: ")
        name = input("Enter name: ")
        email = input("Enter email: ")
        data = {'username': name, 'email': email}
        response = requests.patch(self.base_url + f'{user_id}', json=data)
        print(f"Status Code: {response.status_code}")

        if response.text.strip():
            try:
                update=response.json()
                print(json.dumps(update,indent=5))
            except ValueError:
                print("Response is not valid JSON. Raw response:", response.text)
        else:
            print("Update successful. No content returned.")

    def delete_user(self):
        user_id = input("Enter the ID of the user to delete: ")
        response = requests.delete(self.base_url + f'{user_id}')
        data=response.json()
        print(json.dumps(data,indent=5))


def main():
    user_api = UserAPI("http://127.0.0.1:8000/api/users/")
    
    while True:
        user_input = input("\nEnter the function you want to perform (get/post/patch/delete): ").strip().lower()
        
        if user_input == 'get':
            user_api.get_users()
        elif user_input == 'post':
            user_api.create_user()
        elif user_input in ['update', 'patch']:
            user_api.update_user()
        elif user_input == 'delete':
            user_api.delete_user()
        else:
            print("Invalid option. Choose from get, post, patch, or delete.")

        while True:
            continue_input = input("\nDo you want to continue? (yes/no): ").strip().lower()
            if continue_input == 'yes':
                break
            elif continue_input == 'no':
                print("Exiting the program. Goodbye!")
                return


if __name__ == "__main__":
    main()
