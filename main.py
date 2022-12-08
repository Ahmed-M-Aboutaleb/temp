import authentication
import client
print("Welcome to our freelancer system 👋")
def main():
    print("Please select an option: ")
    print("1. Login")
    print("2. Register")
    option = input()
    if(option == "1"):
        [id, name,role] = authentication.login()
        if(role == "c"):
            print("Welcome freelancer " + name)
        else:
            client.main()
    elif (option == "2"):
        authentication.register()
    else:
        print("❌ | Invalid option")

main()