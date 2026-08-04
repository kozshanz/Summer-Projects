import json

FILE_PATH = "C:\\Users\\LAPTOP\\Desktop\\pass.json"

passwords = {}


def load_data():
    global passwords
    try:
        with open(FILE_PATH, "r") as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}
    except json.JSONDecodeError:
        passwords = {}


def save_data():
    with open(FILE_PATH, "w") as file:
        json.dump(passwords, file, indent=4)


def add_account():
    acc = input("Enter account name: ").strip()

    if acc in passwords:
        print("Account already exists.")
        return

    password = input("Enter password: ")

    passwords[acc] = password
    save_data()

    print("Account added successfully.")


def view_accounts():
    if not passwords:
        print("No accounts saved.")
        return

    print("\nSaved Accounts:")
    print("-" * 30)

    for acc, password in passwords.items():
        print(f"{acc} : {password}")


def search_account():
    acc = input("Enter account name: ").strip()

    if acc in passwords:
        print(f"Password: {passwords[acc]}")
    else:
        print("Account not found.")


def delete_account():
    acc = input("Enter account name: ").strip()

    if acc in passwords:
        del passwords[acc]
        save_data()
        print("Account deleted.")
    else:
        print("Account not found.")


def menu():
    while True:
        print("\n------ Password Manager ------")
        print("1. Add account")
        print("2. View accounts")
        print("3. Search account")
        print("4. Delete account")
        print("5. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            add_account()

        elif choice == 2:
            view_accounts()

        elif choice == 3:
            search_account()

        elif choice == 4:
            delete_account()

        elif choice == 5:
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")


load_data()
menu()
