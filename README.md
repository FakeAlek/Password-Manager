# 🔐 Password Manager

A simple Python password manager that securely stores passwords using **Fernet encryption** from the `cryptography` library.  
It allows adding new users/passwords and decrypting stored passwords.

---

## 📦 Features

- Generates secure, random passwords with uppercase/lowercase letters, numbers, and symbols.
- Stores passwords encrypted in a JSON file.
- Decrypts stored passwords when needed.
- Automatically creates a secret key (`key.key`) if not already present.

---

## 🛠 Installation

**Clone the repository**
```bash
   git clone https://github.com/FakeAlek/Password-Manager.git
   cd Password-Manager
```

**Install the requirements**
```bash
    pip install -r requirements.txt
```