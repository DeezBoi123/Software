import csv
def admins():
    while True:
        print("\t\t\t\t\t1)Add cars")
        print("\t\t\t\t\t2)Update Rent")
        print("\t\t\t\t\t3)Update Purchase")
        print("\t\t\t\t\t4)Update Vcare")
        print("\t\t\t\t\t5)EXIT")
        ch = int(input("Enter your choice(1-5):"))
        if ch == 1:
            print("\t\t\t\t\t1)add Rent cars")
            print("\t\t\t\t\t2)add Purchase cars")
            print("\t\t\t\t\t3)EXIT")
            ch4 = int(input("Enter your choice[1-4]:"))
            if ch4 == 1:
                while True:
                    print("\t\t\t\t\tWelcome to Rental!!!\nPlease pick one of the following brands")
                    print("\t\t\t\t\t1)SUV\n\t\t\t\t\t2)SEDAN\n\t\t\t\t\t3)OFFROAD\n\t\t\t\t\t4)EXIT")
                    ch5 = int(input("Enter your choice(1-5):"))
                    if ch5 == 1:
                        import lib
                        lib.SUV()
                    elif ch5 == 2:
                        import sedan_se
                        sedan_se.sedan()
                    elif ch5 == 3:
                        import offroad_o
                        offroad_o.offroad()
                    elif ch5 == 4:
                        break
                    else:
                        print("\t\t\t\t\tIVALID CHOICE!!\nPlease pick from given choices[1-4]")
            elif ch4 == 2:
                while True:
                    print("\t\t\t\t\tWelcome to Purchase!!!\nPlease pick one of the following brands")
                    print("\t\t\t\t\t1)SUV\n\t\t\t\t\t2)SEDAN\n\t\t\t\t\t3)Hatchback\n\t\t\t\t\t4)EXIT")
                    ch6 = int(input("Enter your choice(1-5):"))
                    if ch6 == 1:
                        import SUV_Spurchase
                        SUV_Spurchase.PSUV()
                    elif ch6 == 2:
                        import sedan_sepurchase
                        sedan_sepurchase.Psedan()
                    elif ch6 == 3:
                        import Hatckback_hpurchase
                        Hatckback_hpurchase.Phatch()
                    elif ch6 == 4:
                        break
                    else:
                        print("\t\t\t\t\tIVALID CHOICE!!\nPlease pick from given choices[1-4]")
            elif ch4 == 3:
                break
            else:
                print("\t\t\t\t\tIVALID CHOICE!!\nPlease pick from given choices[1-4]")

        elif ch == 2:
            while True:
                print("\t\t\t\t\tWelcome to rental!!!\nPlease pick one of the following brands")
                print("\t\t\t\t\t1)SUV\n\t\t\t\t\t2)SEDAN\n\t\t\t\t\t3)OFFROAD\n\t\t\t\t\t4)EXIT")
                ch1 = int(input("Enter your choice[1-4]:"))
                if ch1 == 1:
                    import adminSUV
                    adminSUV.asuv()
                    break
                elif ch1 == 2:
                    import adminSEDAN
                    adminSEDAN.asedan()
                    break
                elif ch1 == 3:
                    import adminOffroad
                    adminOffroad.aoff()
                    break
                elif ch1 == 4:
                    break
                else:
                    print("\t\t\t\t\tIVALID CHOICE!!\nPlease pick from given choices[1-4]")

        elif ch == 3:
            while True:
                print("\t\t\t\t\tWelcome to Purchase!!!\nPlease pick one of the following brands")
                print("\t\t\t\t\t1)SUV\n\t\t\t\t\t2)SEDAN\n\t\t\t\t\t3)Hatchback\n\t\t\t\t\t4)EXIT")
                ch2 = int(input("Enter your choice[1-4]:"))
                if ch2 == 1:
                    import adminPurSUV
                    adminPurSUV.apsuv()
                    break
                elif ch2 == 2:
                    import adminPurSedan
                    adminPurSedan.apsedan()
                    break
                elif ch2 == 3:
                    import adminPurHatchback
                    adminPurHatchback.aphatchback()
                    break
                elif ch2 == 4:
                    break
                else:
                    print("\t\t\t\t\tIVALID CHOICE!!\nPlease pick from given choices[1-4]")
        elif ch == 4:
            while True:
                print("\t\t\t\t\tWelcome to V-CARE!!!\nPlease pick one of the following brands")
                print("\t\t\t\t\t1)SUV\n\t\t\t\t\t2)SEDAN\n\t\t\t\t\t3)OFFROAD\n\t\t\t\t\t4)PAINT\n\t\t\t\t\t5)EXIT")
                ch3 = int(input("Enter your choice[1-4]:"))
                if ch3 == 1:
                    import adminVSUV
                    adminVSUV.avsuv()
                    break
                elif ch3 == 2:
                    import adminVSEDAN
                    adminVSEDAN.avsedan()
                    break
                elif ch3 == 3:
                    import adminVOFFROADER
                    adminVOFFROADER.avoff()
                    break
                elif ch3 == 4:
                    import adminVPAINT
                    adminVPAINT.avpaint()
                    break
                elif ch3 == 5:
                    break
                else:
                    print("\t\t\t\t\tIVALID CHOICE!!\nPlease pick from given choices[1-5]")
        elif ch == 5:
            return 0
        else:
            print("\t\t\t\t\tIVALID CHOICE!!\nPlease pick from given choices[1-4]")
