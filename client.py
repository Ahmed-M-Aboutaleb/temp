def createJobPost(id):
    print("Title: ")
    title = input()
    print("Description: ")
    description = input()
    print("Required skills: (skill1, skill2, ...)")
    skills = input()
    fileName = "database/jobs/" + title + ".txt"
    try:
        file = open(fileName, "r")
        file.close()
        print("❌ | Job post already exists")
        return createJobPost(id)
    except:
        file = open(fileName, "w")
        file.write(str(id[0]) + "\n" + title + "\n" + description + "\n" + skills)
    try:
        file = open("database/jobs/jobs.txt", "a")
        file.write(title + "\n")
        file.close()
        print("✅ | Job post created")
    except:
        file = open("database/jobs/jobs.txt", "w")
        file.write(title + "\n")
        file.close()
        print("✅ | Job post created")

def getOwnerByTitle(title):
    try:
        fileName = "database/jobs/" + title + ".txt"
        file = open(fileName, "r")
        job = file.readlines()
        return job[0]
    except:
        return False

def findJobs():
    try:
        file = open("database/jobs/jobs.txt", "r")
        jobs = file.readlines()
        for job in jobs:
            job = job.split("\n")
            if getOwnerByTitle(job[0]):
                print(job[0])
    except:
        print("❌ | No jobs found")

def main(name):
    try:
        file = open("database/users/freelancers.txt", "r")
        names = file.readlines()
        print("List of the available freelancers: ")
        for name in names:
            name = name.split("\n")
            print(name[0])
        print("1. For your job posts")
        print("2. For create new job post")
        option = input()
        if(option == "1"):
            findJobs()
        elif (option == "2"):
            createJobPost(name)
        else:
            print("❌ | Invalid option")
    except:
        print("❌ | No freelancers found")