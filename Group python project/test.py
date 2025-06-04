import signup
while True:
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    print("\t\t\t\t\t\t\t\t Welcome To Our Vehicle Dealership",username,"!")
    print("\t\t\t\t\t\t\t\t Please choose either from the options")
    print("\t\t\t\t\t\t\t\t 1) SIGN UP")
    print("\t\t\t\t\t\t\t\t 2) LOG IN")
    print("\t\t\t\t\t\t\t\t 3) EXIT")
    print()
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    ch = int(input("Select any from 1,2 OR 3:"))

    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    if ch == 1:
        register()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Invalid Choice \n Please select from the given options above")
