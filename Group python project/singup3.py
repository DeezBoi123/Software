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
def run():       
    while True:
        print("===================================================================================================================================================================================")
        print()
        print("\t\t\t\t\t\t\t\t|| Welcome To Our Vehicle Dealership! ||")
        print("\t\t\t\t\t\t\t\t|Please choose either from the options |")
        print("\t\t\t\t\t\t\t\t\t  || 1) SIGN UP ||")
        print("\t\t\t\t\t\t\t\t\t  || 2) LOG IN  ||")
        print("\t\t\t\t\t\t\t\t\t  || 3) UPDATE  ||")
        print("\t\t\t\t\t\t\t\t\t  || 4) EXIT    ||")
        print()
        print("===================================================================================================================================================================================")

        ch = int(input("Select any from 1,2,3 OR 4:"))
        print("===================================================================================================================================================================================")
        if ch == 1:
            register()
            while True:
                print("===================================================================================================================================================================================")
                print()
                print("\t\t\t\t\t\t\t\t|| Welcome To Our Vehicle Dealership! ||")
                print("\t\t\t\t\t\t\t\t|Please choose either from the options |")
                print("\t\t\t\t\t\t\t\t\t  || 1) LOG IN  ||")
                print("\t\t\t\t\t\t\t\t\t  || 2) BACK TO MENU  ||")
                print()
                print("===================================================================================================================================================================================")
                ch1 = int(input("Select any from 1 and 2:"))
                if ch1 == 1:
                    db = open("profile.txt",'r')
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
                                        print("Welcome",username)
                                        import Main123
                                        Main123.menu2()
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
                                
                elif ch1 == 2:
                    break
                else:
                    print("Invalid Choice! \n Please choose from the options given below")
                
        elif ch == 2:
            db = open("profile.txt",'r')
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
                                print("Welcome",username)
                                import Main123
                                Main123.menu2()
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
        elif ch==4:
            break
        else:
            print("Invalid Choice! \n Please choose from the options given below")

                 
