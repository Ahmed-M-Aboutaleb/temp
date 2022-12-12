import authentication
import client
print("Welcome to our freelancer system 👋")
def main():
    print("Please select an option: ")
    print("1. Login")
    print("2. Register")
    option = input()
    if(option == "1"):
        [name,role] = authentication.login()
        authed(name, role)
    elif (option == "2"):
        [name, role] = authentication.register()
        authed(name, role)
    else:
        print("❌ | Invalid option")

def authed(name, role):
    if(role == "c"):
        client.main(name)
    else:
        print("Welcome freelancer " + name)

if __name__ == "__main__":
    main()