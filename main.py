import string, secrets, json, os
from cryptography.fernet import Fernet

symbols = ['*', '%', '?', '$', '=', '!', '&', '_', '.']

def load_key():
    if not os.path.exists("key.key"):
        with open("key.key", "wb") as key_file:
            key_file.write(Fernet.generate_key())
    with open("key.key", "rb") as key_file:
        return key_file.read()
key = load_key()
fernet = Fernet(key)

def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        # Load existing data into a dictionary
        file_data = json.load(file)
        
        # Append new data to the 'emp_details' list
        file_data["user_list"].append(new_data)
        
        # Move the cursor to the beginning of the file
        file.seek(0)
        
        # Write the updated data back to the file
        json.dump(file_data, file, indent=4)

def add_user():
    userPlatform = input("Which platform is it?: ")
    userEmail = input("What is the email address?: ")
    userPwQuestion = input("Would you like to create your own password or generate one? (c/g): ")

    if userPwQuestion == "e":
        userPw = input("Wie lautet das Passwort?: ")
    else:
        userPw = ""
        for _ in range(9):
            userPw += secrets.choice(string.ascii_lowercase)
            userPw += secrets.choice(string.ascii_uppercase)
            userPw += secrets.choice(string.digits)
            userPw += secrets.choice(symbols)
    
    encPw = fernet.encrypt(userPw.encode()).decode()
    userPw = ''
    newUser = {
        "Platform": userPlatform,
        "Email": userEmail,
        "Password": encPw
    }
    write_json(newUser)
    print("User added!")
    main()

def dec_password():
    decPW = fernet.decrypt(input("What is the key?: ")).decode()
    print(">>" + decPW + "<<")
    main()

def main():
    pathOption = input("Add user [1] | Decrypt password [2] | Close program [3]: ")

    match pathOption:
        case "1":
            add_user()
        case "2":
            dec_password()
        case "3":
            quit()
main()