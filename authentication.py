import uuid
import os
database = "database\\users"

def validation(name, email, password, role  ):
    if(len(password) < 1 or len(email) < 1 or len(name) < 1 or len(role) < 1 or (role != "f" and role != "c")):
        print("❌ | Invalid input")
        return
    return True

def login():
    print("Please enter your name: ")
    name = input()
    print("Please enter your password: ")
    password = input()
    if not os.path.exists(database):
        os.makedirs(database)

    fileName = f"{database}\\{name}\\{name}.txt"
    if not os.path.exists(fileName):
        print("❌ | User not found")
        return login()
    else:
        file = open(fileName, "r")
        user = file.readlines()
        if password == user[3].split("\n")[0]:
            print("✅ | Login successful")
            return [name, user[4]]
        else:
            print("❌ | Wrong password")
            return login()

def register():
    print("Please enter your name: ")
    name = input()
    print("Please enter your email: ")
    email = input()
    print("Please enter your password: ")
    password = input()
    print("Are you freelancer or client? (f/c)")
    role = input()
    if(validation(name, email, password, role)):
        id= uuid.uuid4()
        if not os.path.exists(database):
            os.makedirs(database)
        fileName = f"{database}\\{name}\\{name}.txt"
        if not os.path.exists(fileName):
            os.makedirs(f"{database}\\{name}")
            file = open(fileName, "w")
            file.write(f"{str(id)}\n{name}\n{email}\n{password}\n{role}")
            file.close()
            print("✅ | Registration successful")
            if role == "f":
                if not os.path.exists("database/users/freelancers.txt"):
                    file = open("database/users/freelancers.txt", "w")
                    file.write(name + "\n")
                    file.close()
                else:
                    file = open("database/users/freelancers.txt", "a")
                    file.write(name + "\n")
                    file.close()
            return [name, role]
        else:
            print("❌ | User already exists")
            return register()