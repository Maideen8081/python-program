def register():
    username=input("Enter the user name")
    passwor=input("Enter the password")

    with open('testfile.txt','a') as f:
        f.write(f"{username},{passwor}\n")


    print("Register successfully")    

def login():
    username=input("Enter the user name")
    password=input("Enter the passord")

    with open('testfile.txt','r')as f:
        user=f.readline()

        for i in user:
            stored_username,stored_password=user.strip().split(",")
        if stored_username==username and stored_password==password:
            print(f,"login success fullu {username}")
        else:
            print("invalid user name and password")
                

register()
login()                

