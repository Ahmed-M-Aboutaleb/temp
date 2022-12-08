def main():
    try:
        file = open("database/users/freelancers.txt", "r")
        names = file.readlines()
        print(names)
    except:
        print("❌ | No freelancers found")