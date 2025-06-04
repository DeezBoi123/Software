import time
def admin():
    while True:
        db = open("admin.txt",'r')
        l = db.readlines()
        username = input("Enter your username:")
        password = input("Enter your password:")
        r = {}
        if len(username or password) > 1:
            for i in l:
                p = i.strip().split(", ")
                #b = b.strip()
                #r = {}
                #r[a]=b
                username1, password1 = p
                r[username1] = password1
            try:
                if username in r:
                    try:
                        if password == r[username]:
                            print("Login successful")
                            print("\t\t\t\t\tHello",username,"How can we assist you?")
                            #break
                            import adminUPDATE
                            adminUPDATE.admins()
                            s = adminUPDATE.admins()
                            if s == 0:
                                break
                            
                        else:
                            print("password or username incorrect")
                            pass
                                        
                    except:
                        print("incorrect password or username")
                        pass
                                    
                else:
                    print("username doesn't exist")
                    pass

            except:
                print("Login error")
                pass

def register():
    db = open("profile.txt",'r')
    username = input("Create your username:")
    password = input("Create your password:")
    password1 = input("Confirm your password:")
    #d = []
    #f = []
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        r = {}
        r[a]=b
    if password != password1:
        print("User password does not match \n Please try again")
        register()

    else:
        if len(password) <= 4:
            print("Password too short!")
            register()
        elif username in r:
            print("username already exists \n try again")
            register()
        else:
            db = open("profile.txt",'a')
            db.write(username+", "+password+"\n")
            print("Success!!")
            return username
            

def update():
    db = open("profile.txt", 'r')
    lines = db.readlines()
    db.close()

    username = input("Enter your current username: ")
    password = input("Enter your current password: ")

    found = False
    update = []
    for i in lines:
        username1, password1= i.strip().split(", ")
        if username1 == username and password1 == password:
            new_username = input("Enter your new username: ")
            new_password = input("Enter your new password: ")
            if len(new_password) <= 4:
                print("New password is too short. Please try again.")
                return update()
            update.append(f"{new_username}, {new_password}\n")
            found = True
        else:
            update.append(i)

    if not found:
        print("Invalid username or password. Please try again.")
        return update()

    with open("profile.txt", 'w') as db:
        db.writelines(update)

    print("Username and password updated successfully!")
def run1():
    while True:
    
        print("==================================================================================================================================================================================")
        print()
        print("\t\t\t\t\t\tx========================================================x")
        print("\t\t\t\t\t\t||\t Welcome To Our Vehicle Dealership! \t\t||")
        print("\t\t\t\t\t\t||\tPlease choose either from the options\t\t||")
        print("\t\t\t\t\t\t||\t  ________     1) SIGN UP    ________  \t\t||")
        print("\t\t\t\t\t\t||\t / ______ \    2) LOG IN    / ______ \ \t\t||")
        print("\t\t\t\t\t\t||\t| |___|__| |_  3) UPDATE  _| |__|___| |\t\t||")
        print("\t\t\t\t\t\t||\t|____________| 4) ADMIN  |____________|\t\t||")
        print("\t\t\t\t\t\t||\t OO        OO  5) EXIT    OO        OO \t\t||")
        print("\t\t\t\t\t\tx========================================================x")
        print("\t\t\t\t\t\t                  Welcome to Car Tale!\n\t\t\t\t\t\tWhether you're looking to purchase your dream car or rent\n\t\t\t\t\t\t  a vehicle for your next adventure, we’re here to help.\n\t\t\t\t\tExplore our selection and let us assist you in finding the perfect ride!")
        print()
        import loadingscreen
        loadingscreen.carload()
        print("==================================================================================================================================================================================")

        ch = int(input("Select any from 1,2,3 OR 4:"))
        print("==================================================================================================================================================================================")
        if ch == 1:
            register()    
        elif ch == 2:
                db = open("profile.txt",'r')
                l = db.readlines()
                def names():
                    username = input("Enter your username:")
                    password = input("Enter your password:")
                    return username, password
                username, password = names()
                r = {}
                if len(username or password) > 1:
                    for i in l:
                        p = i.strip().split(", ")
                        #b = b.strip()
                        #r = {}
                        #r[a]=b
                        username1, password1 = p
                        r[username1] = password1
                    try:
                        if username in r:
                            try:
                                if password == r[username]:
                                    print("Login successful")
                                    print("\t\t\t\t\tHello",username,"How can we assist you?")
                                    db = open("extracted.txt",'w')
                                    db.write(username+", "+password)
                                    break


    
                                else:
                                    print("password or username incorrect")
                                    pass
                                                
                            except:
                                print("incorrect password or username")
                                pass
                                            
                        else:
                            print("username doesn't exist")
                            pass

                    except:
                        print("Login error")
                        pass
        elif ch == 3:
            update()
        elif ch==5:
            return 0
        
        elif ch ==4:
            admin()   
        else:
            print("Invalid Choice! \n Please choose from the options given below")

                  

