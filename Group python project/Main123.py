import signup

while True:
    a=signup.run1()
    if a==0:
         print("Thanks for Visiting US \nDo visit us again :)")
         break
    while True:
        print("=========================================================================================================================")
        print("\t\t\t\t\t1>>> Rent a vehicle")
        print("\t\t\t\t\t2>>> Purchase Vehicle")
        print("\t\t\t\t\t3>>> V-care")
        print("\t\t\t\t\t4>>> About-US")
        print("\t\t\t\t\t5>>> User account info")
        print("\t\t\t\t\t6>>> Back to log/sign in page")
        print("=========================================================================================================================")
        ch =int(input("Input a valid choice number:- "))
        print("=========================================================================================================================")
        if ch > 6:
            print("Input Valid choice nom. from above please!")
        elif ch == 6  :
            break
        elif ch==2:
            while True:
                import deal
                #deal.dealership()
                c = deal.dealership()
                if c == 0:
                    break           
        elif ch==1 :
            while True:
                import rent
                b = rent.rental()
                if b == 0:
                    break
        elif ch==3:
            while True:
                import vcare
                d = vcare.vcare()
                if d == 0:
                    break
        elif ch == 4:
            import aboutus
            aboutus.aboutus()
            pass
        elif ch == 5:
            import userprofile
            userprofile.userprofile()
            pass
