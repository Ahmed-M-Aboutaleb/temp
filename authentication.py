import uuid

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
    fileName = "database/users/" + name + ".txt"
    try:
        file = open(fileName, "r")
    except:
        print("❌ | User not found")
        return login()
    with file:
        user = file.readlines()
        if password+"\n" == user[3]:
            print("✅ | Login successful")
            return [user[0], name, user[4]]
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
        fileName = "database/users/" + name + ".txt"
        try:
            file = open(fileName, "r")
            file.close()
            print("❌ | User already exists")
            return register()
        except:
            file = open(fileName, "w")
            file.write(str(id) + "\n" + name + "\n" + email + "\n" + password + "\n" + role)
            file.close()
            print("✅ | Registration successful")
        if role == "f":
            try:
                file = open("database/users/freelancers.txt", "a")
                file.write(name + "\n")
                file.close()
            except:
                file = open("database/users/freelancers.txt", "w")
                file.write(name + "\n")
                file.close()