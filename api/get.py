import requests
import json

class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url 

    def get_users(self):
        while True:
            apply_filter = input("Do you want to filter data? (yes/no): ").strip().lower()
            if apply_filter in ['yes', 'no']:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")
 
        params = {}
        if apply_filter == 'yes':
            data = input("Enter data(or leave blank): ").strip()
            # last_name = input("Enter last name (or leave blank): ").strip()
            # email = input("Enter email (or leave blank): ").strip()

            if data:
                params['search'] = data
            # elif data:
            #     params['last_name'] = data
            # elif data:
            #     params['email'] = data
        
        
        try:
            response = requests.get(self.base_url, params=params)
            user = response.json()
            print("\nFiltered User Data:")
            print(json.dumps(user, indent=5))
        except Exception as e:
            print(f"An error occurred while fetching users: {e}")

    def create_user(self):
        name = input("Enter name: ")
        first_name=input("enter first name")
        last_name= input("enter last name")
        email = input("Enter email: ")
        password = input("Enter password: ")
        data = {'username': name, 'email': email,'first_name':first_name,'last_name':last_name, 'password': password}
        response = requests.post(self.base_url, json=data)
        user = response.json()
        print(json.dumps(user, indent=5))

    def update_user(self):
        user_id = input("Enter the ID of the user to update: ")
        name = input("Enter name: ")
        first_name=input("enter first name: ")
        last_name=input("enter last name: ")
        email = input("Enter email: ")
        data = {'username': name,'first_name' :first_name,'last_name':last_name,'email': email}
        response = requests.patch(self.base_url + f'{user_id}', json=data)
        print(f"Status Code: {response.status_code}")

        if response.text.strip():
            try:
                update = response.json()
                print(json.dumps(update, indent=5))
            except ValueError:
                print("Response is not valid JSON. Raw response:", response.text)
        else:
            print("Update successful. No content returned.")

    def delete_user(self):
        user_id = input("Enter the ID of the user to delete: ")
        response = requests.delete(self.base_url + f'{user_id}')
        try:
            data = response.json()
            print(json.dumps(data, indent=5))
        except ValueError:
            print("User deleted successfully.")

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
