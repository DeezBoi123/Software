def rental():
    while True:
        print("What category vehicle, would you like to rent?")
        cat =input("Press 's' for SUV; type 'se' for SEDAN; press 'o' for OFF-ROADER; press 'e' to return to Home menu >")
        if cat == 'e' :
            return 0
        elif cat == 'o':
            while True:
                print("=========================================================================================================================")
                print("\t\tWhat model do you preffer? ")
                print("=========================================================================================================================")
                '''print("Sr.no\t\tModel Name\t\tFuel Type\tLuggage space\t\tDrive Type\tRental Price\t")
                print("1.\t\tMahindra Thar\t\tDiesel\t\t2\t\t\t4X4\t\t₹38.0/km\n2.\t\tForce Gurkha\t\tDiesel\t\t2\t\t\t4WD\t\t₹38.0/km\n3.\t\tJEEP Wrangler\t\tPetrol\t\t2\t\t\t4WD\t\t₹38.0/km")   
                print(" ")'''
                import offroadread
                offroadread.off()
                ch1 =input("Enter serial  nom. of preffered Company model: ")
                import csv
                with open("Offroad.csv",'r') as f:
                    rec = list(csv.reader(f))
                found = False
                for i in rec:
                    if i[0] == ch1:
                        print("current:",i[5])
                        new = i[5]
                        found = True
                #print(new)
                print("----------------------------------------------------------------------------------------------------------------")
                print("|NOTE:Rent is charged for 120 Km/12-Hours,after that additional rent of ₹30/hr and actuall rent will be charged|")
                print("----------------------------------------------------------------------------------------------------------------")
                print(" ") 
                opt =input("Rent this vehicle?,[type 'y' for YES or 'n' for NO or 'b' to look for other model]: ")
                if opt =='y'or opt=='yes':
                    data1 =input("Enter Pickup DATE in format(DD/MM) :- ")
                    data2 =input("Renting car for how many days:- ")
                    val = int(data2)
                    val1 = (val*24)-12
                    val2 = val1*30 +(120*int(new))
                    print("Total Rent cost(Deducing 12-Hours fee) for ",val," days is ₹",val2)
                    data3 =input("Confirm this Model?: ")
                    if data3 =='y' or data3 =='yes':
                        print("\t\tPlease select Mode of Payment:")
                        print(" ")
                        print("\t\t1.)By Cash\n\t\t2.)Credit Card")
                        data4 = int(input("Enter valid choice nom from above: "))
                        if data4== 1:
                            print("car booked for ",data1,"\nThank You for your Purchace :)")                                       
                            print("Going back to home menu")
                            break
                        elif data4== 2:
                            import details
                            details.detail()
                    elif data3=='n' or data3=='no':
                        pass
                elif opt == 'b' or opt == 'back':
                    break
                break
        elif cat =='se':
            while True:
                    
                print("=========================================================================================================================")
                print("\t\tWhat model do you preffer?")
                print("=========================================================================================================================")
                '''print("Sr.no\t\tModel Name\t\tFuel Type\tLuggage space\tRental Price\t")
                print("1.\t\tHyundai Aura\t\tDiesel\t\t1\t\t₹26.0/km\n2.\t\tHyundai i20\t\tPetrol\t\t1\t\t₹26.0/km\n3.\t\tHyundai Verna\t\tPetrol\t\t1\t\t₹26.0/km")
                print("4.\t\tHonda Accord \t\tPetrol\t\t2\t\t₹27.0/km\n5.\t\tHonda Amaze\t\tPetrol\t\t1\t\t₹27.0/km\n6.\t\tHonda Civic\t\tDiesel\t\t2\t\t₹27.0/km")
                print("7.\t\tMaruti swift D'Tour\tPetrol\t\t1\t\t₹25.0/km\n8.\t\tMaruti Ciaz \t\tPetrol\t\t1\t\t₹25.0/km\n9.\t\tMaruti Dzire \t\tPetrol\t\t1\t\t₹25.0/km")'''
                import sedanread
                sedanread.sedan()
                print(" ")
                ch1 =input("Enter serial  nom. of preffered Company model: ")
                import csv
                with open("SEDAN.csv",'r') as f:
                    rec = list(csv.reader(f))
                found = False
                for i in rec:
                    if i[0] == ch1:
                        print("current:",i[4])
                        new = i[4]
                        found = True
                print("----------------------------------------------------------------------------------------------------------------")
                print("|NOTE:Rent is charged for 120 Km/12-Hours,after that additional rent of ₹30/hr and actuall rent will be charged|")
                print("----------------------------------------------------------------------------------------------------------------")
                print("---------------------------------------------")
                print("|NOTE:Carrier cost additional charge of ₹25 |")
                print("---------------------------------------------")
                opt =input("Rent this vehicle?,[type 'y' for YES or 'n' for NO or 'b' to look for other model]: ")
                if opt =='y'or opt=='yes':
                    data1 =input("Enter Pickup DATE in format(DD/MM) :- ")
                    data2 =input("Renting car for how many days:- ")
                    val = int(data2)
                    val1 = (val*24)-12
                    val2 = val1*30 +(120*int(new))
                    print("Total Rent cost(Deducing 12-Hours fee) for ",val," days is ₹",val2)
                    data3 =input("Confirm this Model?: ")
                    if data3 =='y' or data3 =='yes':
                        data4 =input("Add Carrier to your vehicle? : ")
                        if data4 =='yes'or data4 =='y':
                            val2+= 25
                            print("Total cost of Rent:=  ₹",val2)
                            data5 =input("Confirm purchase: ")
                            if data5 =='y' or data5 =='yes':
                                    print("\t\tPlease select Mode of Payment:")
                                    print("\t\t1.)By Cash\n\t\t2.)Credit Card")
                                    data6 = int(input("Enter valid choice nom from above: "))
                                    if data6== 1:
                                        print("car booked for ",data1,"\nThank You for your Purchace :)")                                       
                                        print("Going back to home menu")
                                        break
                                    elif data6== 2:
                                        import details
                                        details.detail()
                    else:
                        pass
                elif opt == 'b' or opt == 'back':
                    break
                else:
                    break
                break
        elif cat == 's':
            while True:
                print("=========================================================================================================================")
                print("\t\tWhat model do you preffer?")
                print("=========================================================================================================================")
                '''print("Sr.no\t\tModel Name\t\tFuel Type\tLuggage space\tRental Price\t")
                print("1.\t\tHyundai Creta\t\tPetrol\t\t2\t\t₹33.0/km\n2.\t\tHyundai veneu\t\tPetrol\t\t2\t\t₹33.0/km\n3.\t\tHyundai Exter\t\tpetrol\t\t2\t\t₹33.0/km")
                print("4.\t\tKIA Seltos\t\tDiesel\t\t2\t\t₹35.0/km\n5.\t\tKIA Sonet\t\tPetrol\t\t2\t\t₹35.0/km\n6.\t\tKIA Carnival\t\tDiesel\t\t2\t\t₹35.0/km")
                print("7.\t\tMahindra Scorpio\t\tDiesel\t\t2\t\t₹30.0/km\n8.\t\tMahindra XUV300\t\tPetrol\t\t2\t\t₹30.0/km\n9.\t\tMahindra XUV700\t\tPetrol\t\t2\t\t₹30.0/km")'''
                import suvread
                suvread.suv()
                print(" ")
                ch1 =input("Enter serial  nom. of preffered Company model: ")
                import csv
                with open("SUV.csv",'r') as f:
                    rec = list(csv.reader(f))
                found = False
                for i in rec:
                    if i[0] == ch1:
                        print("current:",i[4])
                        new = i[4]
                        found = True
                print("----------------------------------------------------------------------------------------------------------------")
                print("|NOTE:Rent is charged for 120 Km/12-Hours,after that additional rent of ₹30/hr and actuall rent will be charged|")
                print("----------------------------------------------------------------------------------------------------------------")
                opt =input("Rent this vehicle?,[type 'y' for YES or 'n' for NO or 'b' to look for other model]: ")
                if opt =='y'or opt=='yes':
                    data1 =input("Enter Pickup DATE in format(DD/MM) :- ")
                    data2 =input("Renting car for how many days:- ")
                    val = int(data2)
                    val1 = (val*24)-12
                    val2 = val1*30 +(120*int(new))
                    print("Total Rent cost(Deducing 12-Hours fee) for ",val," days is ₹",val2)
                    data3 =input("Confirm this Model?: ")
                    if data3 =='y' or data3 =='yes':
                        print("\t\tPlease select Mode of Payment:")
                        print(" ")
                        print("\t\t1.)By Cash\n\t\t2.)Credit Card")
                        data4 = int(input("Enter valid choice nom from above: "))
                        if data4== 1:
                            print("car booked for ",data1,"\nThank You for your Purchace :)")                                       
                            print("Going back to home menu")
                            break
                        elif data4== 2:
                            import details
                            details.detail()
                    elif data3=='n' or data3=='no':
                        pass
                elif opt == 'b' or opt == 'back':
                    break
                break  
#rental()