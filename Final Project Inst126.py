
### main.py:

import requests
import re

def get_user_info(user_id):
    api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch user information. Status Code: {response.status_code}")

def extract_user_details(user_data):
    name = user_data["name"]
    email = user_data["email"]
    phone = user_data["phone"]

    return f"Name: {name}\nEmail: {email}\nPhone: {phone}\n"

if __name__ == "__main__":
    user_id = input("Enter the user ID: ")

    # Validate user input using regular expression
    if not re.match(r"^\d+$", user_id):
        print("Invalid user ID. Please enter a numeric value.")
        exit(1)

    try:
        user_data = get_user_info(user_id)
        user_details = extract_user_details(user_data)
        print(user_details)
    except Exception as e:
        print(f"Error: {e}")
