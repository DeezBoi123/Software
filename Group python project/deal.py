def dealership():
    while True:
        cat =input("Type 's' for SUV; type 'se' for SEDAN; type 'h' for HATCHBACK; type 'e' to return to Home menu >")
        if cat == 'e' :
            return 0
        elif cat =='h':
            while True:
                '''print("=========================================================================================================================")
                print("\t\tWhat model do you preffer?\n\t\t(N/F)--> Not Functioning\n\t\tMOD.--> Modified\n\t\t(Fr)--> Front\n\t\t(Rr)--> Rear")
                print("=========================================================================================================================")
                print("Sr.no\t\tModel Name\t\tEngine Config.\t\tTransmisson\tDamage History\t\tPrice")
                print("1.\t\tHyundai i20\t\t1.2l ERA MT-Petrol\t6-speed Manual\tReplaced E.C.U\t\t₹8.05L\n2.\t\tHyundai Grand i10\t1.2l U2 CRDi-Petrol\t5-speed Manual\tChanged ( Rr ) Rims\t₹6.8L\n3.\t\tMaruti Swift\t\t1.2l VXi-Petrol\t\t5-speed Manual\tRadio(N/F)\t\t₹8.5L")
                print("4.\t\tRenault KWiD\t\t1.0l RXL(O)-Petrol\t5-speed AUTO\tMOD. Exhaust\t\t₹6.22L\n5.\t\tFord Figo\t\t1.5l TDCi-Diesel\t5-speed Manual\t\t\t\t₹1.63L\n6.\t\tVolkswagen GTi\t\t2.0l TSI-Petrol\t\t6-speed Manual\t\t\t\t₹7.5L")'''
                import PurHatchbackread
                PurHatchbackread.Phatch()
                print(" ")
                ch1 =input("Enter serial  nom. of preffered Company model: ")
                if ch1 in ('1','2','3','4','5','6'):
                    print(" ")
                    opt =input("Buy this vehicle?,[type 'y' for YES or 'n' for NO or 'b' to look for other model]: ")
                    if opt=='n' or opt=='no':
                        pass
                    elif opt =='y'or opt=='yes':
                        data1 =input("Purchase Car Insurance for your Vehicle @ ₹3000? :")
                        if data1=='yes' or data1=='y':
                            print("Vehicle insurance added in Main Price!")
                            data2 =input("Confirm this Purchase(Type 'y' for yes or  'n' for no)?: ")
                            if data2 =='y' or data2=='yes':
                                print("Congratulations! Your purchase was successful!")
                                print("Returning Back to home screen")
                                break
                            elif data2 =='n' or data2=='no':
                                pass
                        elif data1=='no' or data1=='n':
                            data2=input("Are you sure ?: ")
                            if data2=='n' or data2=='no':
                                data1 =input("Purchase Car Insurance for your Vehicle @ ₹3000? :")
                                if data1=='yes' or data1=='y':
                                    print("Vehicle insurance added in Main Price!")
                                    data2 =input("Confirm this Purchase(Type 'y' for yes or  'n' for no)?: ")
                                    if data2 =='y' or data2=='yes':
                                        print("Congratulations! Your purchase was successful!")
                                        print("Returning Back to home screen")
                                        break
                            elif data2=='yes' or data2=='y':
                                data3 = input("Confirm Purchase?: ")
                                if data3=='yes' or data3=='y':
                                    print("Congratulations! Your Purchase was successful!")
                                    print("Returning Back to home screen")
                                    break      
                                elif data3=='no' or data3=='n':
                                    data4=input("Add Insurance Amount?: ")
                                    if data4=='yes' or data4=='y':
                                        print("Vehicle insurance added in Main Price!")
                                        print("Congratulations! Your Purchase was successful!")
                                        print("Returning Back to home screen")
                                        break
                                    elif data4=='no' or data4=='n':                               
                                        pass
                                                            
                                                
        elif cat == 's':
                while True:
                    '''print("=========================================================================================================================")
                    print("\t\tWhat model do you preffer? \n\t\t(N/F)--> Not Functioning\n\t\tMOD.--> Modified\n\t\t(Fr)--> Front\n\t\t(Rr)--> Rear")
                    print("=========================================================================================================================")
                    print("Sr.no\t\tModel Name\t\tEngine Config.\t\tTransmisson\tDamage History\t\tPrice")
                    print("1.\t\tHyundai Creta\t\t1.5l MPi-Petrol\t\t6-speed Manual\t\t\t\t₹5.8L\n2.\t\tHyundai veneu\t\t1.0l TurboGDi-Petrol\t6-speed Manual\t\t\t\t₹7.25L\n3.\t\tHyundai Exter\t\t1.2l Kappa-petrol\t5-speed Manual\tMinor Paint Defect\t₹3.3L")
                    print("4.\t\tKIA Seltos\t\t1.4l TurboGDi-Petrol\t6-speed Manual\t\t\t\t₹6.5L\n5.\t\tKIA Sonet\t\t1.2l SS-Petrol\t\t7-speed DCT\t\t\t\t₹4.0L\n6.\t\tKIA Carnival\t\t2.2l CRDi-Diesel\t8-speed AUTO.\tReplaced Battery\t₹14.1L")
                    print("7.\t\tMahindra Scorpio\t2.2l mHAWK-Diesel\t6-speed Manual\tReplaced Headlights(Fr)\t₹3.0L\n8.\t\tMahindra XUV300\t\t2.2l mStalionPetrol\t6-speed Manual\t\t\t\t₹7.3L\n9.\t\tMahindra XUV700\t\t2.0l mstalionPetrol\t6-speed AUTO.\t\t\t\t₹15.2L")'''
                    import PurSUVread
                    PurSUVread.Psuv()
                    print(" ")
                    ch1 =input("Enter serial  nom. of preffered Company model: ")
                    if ch1 in ('1','2','3','4','5','6','7','8','9'):
                            print(" ") 
                            opt =input("Buy this vehicle?,[type 'y' for YES or 'n' for NO or 'b' to look for other model]: ")
                            if opt=='n' or opt=='no':
                                    pass
                            elif opt =='y'or opt=='yes':
                                data1 =input("Purchase Car Insurance for your Vehicle @ ₹3000? :")
                                if data1=='yes' or data1=='y':
                                    print("Vehicle insurance added in Main Price!")
                                    data2 =input("Confirm this Purchase(Type 'y' for yes or  'n' for no)?: ")
                                    if data2 =='y' or data2=='yes':
                                            print("Congratulations! Your purchase was successful!")
                                            print("Returning to HOME Menu")
                                            break
                                    elif data2 =='n' or data2=='no':
                                            pass
                                elif data1=='no' or data1=='n':
                                            data2=input("Are you sure you don't want this insurance?: ")
                                            if data2=='yes' or data2=='y':
                                                    print("Congratulations! Your purchase was successful!")
                                                    print("Returning to HOME Menu")
                                                    break
                                            elif data2=='no' or data2=='n':
                                                    print("Vehicle insurance added in Main Price!")
                                                    data2 =input("Confirm this Purchase(Type 'y' for yes or  'n' for no)?: ")
                                                    if data2 =='y' or data2=='yes':
                                                                print("Congratulations! Your purchase was successful!")
                                                                print("Returning to HOME Menu")
                                                                break
        elif cat == 'se':
                while True:
                    '''print("=========================================================================================================================")
                    print("\t\tWhat model do you preffer? \n\t\t(N/F)--> Not Functioning\n\t\tMOD.--> Modified\n\t\t(Fr)--> Front\n\t\t(Rr)--> Rear")
                    print("=========================================================================================================================")
                    print("Sr.no\t\tModel Name\t\tEngine Config.\t\tTransmisson\tDamage History\t\tPrice")
                    print("1.\t\tHyundai Aura\t\t1.2l U2 CRDi-Diesel\t5-speed Manual\tBlinkers(N/F)\t\t₹3.5L\n2.\t\tMercedes Benz E-Class\t2.0l E300-Petrol\t9-speed AUTO.\t\t\t\t₹8.5L\n3.\t\tSkoda Slavia\t\t1.0l TSI-Petrol\t\t6-speed AUTO.\tScrathed Paint(Rear)\t₹8.0L")
                    print("4.\t\tToyota Yaris\t\t1.3l i4-Petrol\t\t6-speed Manual\t\t\t\t₹6.3L\n5.\t\tHonda Amaze\t\t1.2l i-VTEC-Petrol\t5-speed Manual\t\t\t\t₹4.9L\n6.\t\tHonda Civic\t\t2.0l i4-Petrol\t\t6-speed CVT\t\t\t\t₹3.28L")
                    print("7.\t\tAudi A6\t\t\t2.0l TFSI-Petrol\t7-speed DC-AUTO\tReplaced E.C.U.\t\t₹6.0L\n8.\t\tMaruti Ciaz\t\t1.5l K15B-Petrol\t4-speed AUTO.\tReplaced Rear Bumper\t₹7.15L")'''
                    import PurSedanread
                    PurSedanread.Psedan()
                    print(" ")
                    ch1 =input("Enter serial  nom. of preffered Company model: ")
                    if ch1 in ('1','2','3','4','5','6','7','8'):
                            
                            print(" ")
                            opt =input("Buy this vehicle?,[type 'y' for YES or 'n' for NO or 'b' to look for other model]: ")
                            if opt=='n' or opt=='no':
                                pass
                            elif opt =='y'or opt=='yes':
                                data1 =input("Purchase Car Insurance for your Vehicle @ ₹3000? :")
                                if data1=='yes' or data1=='y':
                                            print("Vehicle insurance added in Main Price!")
                                            data2 =input("Confirm this Purchase(Type 'y' for yes or  'n' for no)?: ")
                                            if data2 =='y' or data2=='yes':
                                                print("Congratulations! Your purchase was successful!")
                                                print("Returning to HOME Menu")
                                                break
                                            elif data2 =='n' or data2=='no':
                                                pass
                                elif data1=='no' or data1=='n':
                                                data3=input("Are you sure you don't want this insurance?: ")
                                                if data3=='yes' or data3=='y':                                      
                                                        data4 = input("Confirm purchase? ")
                                                        if data4 =='yes' or data4=='y':
                                                                print("Congratulations! Your purchase was successful!")
                                                                print("Returning to HOME Menu")
                                                                break
                                                        elif data4=='no' or data4=='n':
                                                                pass                                                              
                                                elif data3=='no' or data3=='n':
                                                        print("Vehicle insurance added in Main Price!")
                                                        data4 =input("Confirm this Purchase(Type 'y' for yes or  'n' for no)?: ")
                                                        if data4 =='y' or data4=='yes':
                                                                print("Congratulations! Your purchase was successful!")
                                                                print("Returning to HOME Menu")
                                                                break
                                                        elif data4=='n' or data4=='no':
                                                                pass                                                  
#dealership()
