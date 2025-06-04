def vcare():
        while True:
            print("=======================================================")
            print("Welcome to v-care {username}")
            print("what would u like to do?")
            print("=======================================================")
            c = input("Press 'M' for maintainence: ").lower()
            print("=======================================================")
            
            if c == 'm':
                while True:
                    print("1) Car wash \n2) Car Maintainance \n3) Paint restoration")
                    
                    ch = int(input("Enter valid choice number from the above: "))
                    
                    print('='*55)
                    l=input('Enter N for continue or Enter W go for another service:')
                    print('='*55)
                    if l.upper()=='W':
                         continue
                   
                    if ch == 1:
                        print('==================================================================[Welcome to Car Wash Section]=======================================================================')
                        x = input("Enter the date for checkup: ")
                        ch2 = input("Enter your address: ")
                        ch3 = input("Enter your phone number: ")
                        
                        len1 = len(ch3)
                        if len1 > 10 or len1 < 10:
                            print("Invalid phone number enter a 10 digit number")
                            break
                        else:
                            print('='*55)
                            g=input('Enter the name:')
                            print("Hello",g)
                            print('='*55)
                        
                        ch4 = input("Enter car's company name:")
                        ch5 = input("Enter vehicle model:")
                        print('='*55)
                        print("Select your vehicle type below")
                        print('='*55)
                        print("1) Regular Size Car \n2) Medium Size Car \n3) Compact SUV \n4) Minivan \n5) Pickup Truck \n6) Cargo Truck")
                        print('='*55)
                        ch6 = int(input("Enter the valid choice from above:"))
                        
                        while True:
                         print('='*55)
                         print('what would you like to do in car wash?')
                         print('='*55)
                         print("1) Basic Hand Wash: (25min) \n(Exterior Hand Wash(EHW) \n Towel Hand Dry(THD) \n Wheel Shine(WS))")
                         print('='*55)
                         print("2) Deluxe Wash: (45min) \n(Exterior Hand Wash(EHW) \n Towel Hand Dry(THD) \n Wheel Shine(WS) \n Tire Dressing(TD) \n Windows In & Out(WIO) \n Sealer Hand Wax(SHW))")
                         print('='*55)
                         print("3) Ultimate Shine: (60min) \n(Exterior Hand Wash(EHW) \n Towel Hand Dry(THD) \n Wheel Shine(WS) \n Tire Dressing(TD) \n Windows In & Out(WIO) \n Sealer Hand Wax(SHW) \n Interior Vacuum(IV) \n Door Shuts & Plastics(DSP) \n Dashboard Clean(DC) \n Air Freshener(AF))")
                         print('='*55)
                         print("4) Platinum Works: (100min) \n(Exterior Hand Wash(EHW) \n Towel Hand Dry(THD) \n Wheel Shine(WS) \n Tire Dressing(TD) \n Windows In & Out(WIO) \n Sealer Hand Wax(SHW) \n Interior Vacuum(IV) \n Door Shuts & Plastics(DSP) \n Dashboard Clean(DC) \n Air Freshener(AF) \n Triple Coat Hand Wax(TCHW) \n Exterior Vinyl Protectant(EVP) \n Rain-X Complete(RXC))")
                         print('='*55)
                         ch7 = int(input('Enter package you would like to BOOK:'))

                         print('='*55)
                         l=input('Enter N for continue or Enter W go for another package you want:')
                         print('='*55)
                         if l.upper()=='W':
                              continue
                         
                         if ch7 == 1:
                              EWH,THD,WS = 99,50,40
                              print('EWH =',EWH,'THD =',THD,'WS =',WS,'TOTAL AMOUNT=₹',EWH+THD+WS)
                              t=189
                         elif ch7 == 2:
                              EWH,THD,WS,TD,WIO,SHW = 99,50,40,110,160,130
                              print('EWH =',EWH,'THD =',THD,'WS =',WS,'TD =',TD,'WIO =',WIO,'SHW =',SHW,'TOTAL AMOUNT=₹',EWH+THD+WS+TD+WIO+SHW)
                              t=589
                         elif ch7 == 3:
                              EWH,THD,WS,TD,WIO,SHW,IV,DSP,DC,AF = 99,50,40,110,160,130,190,170,150,180
                              print('EWH =',EWH,'THD =',THD,'WS =',WS,'TD =',TD,'WIO =',WIO,'SHW =',SHW,'IV =',IV,'DSP =',DSP,'DC =',DC,'AF =',AF,'TOTAL AMOUNT=₹',EWH+THD+WS+TD+WIO+SHW+IV+DSP+DC+AF)
                              t=1279
                         elif ch7 == 4:
                              EWH,THD,WS,TD,WIO,SHW,IV,DSP,DC,AF,TCHW,EVP,RXC = 99,50,40,110,160,130,190,170,150,180,150,140,200
                              print('EWH =',EWH,'THD =',THD,'WS =',WS,'TD =',TD,'WIO =',WIO,'SHW =',SHW,'IV =',IV,'DSP =',DSP,'DC =',DC,'AF =',AF,'TCHW =',TCHW,'EVP =',EVP,'RXC =',RXC,'TOTAL AMOUNT=₹',EWH+THD+WS+TD+WIO+SHW+IV+DSP+DC+AF+TCHW+EVP+RXC)
                              t=1769
                         else:
                              print('Thank you for visiting')
                              break                            
                         print('='*55)         
                         print('choose a payment method')
                         print("1)CASH \n2)PAYPAL")
                         print('='*55)
                         ch8 = int(input('Enter payment method:'))
                         print('Loading Payment window...')
                         if ch8 == 1:
                              print('Confirm Booking??')
                              ch9 = input('YES OR NO:').lower()
                              if ch9 =='yes':
                                   print('Booking your slot and package...')
                                   print('Booking successful')
                              else:
                                   print('Booking Cancelled')
                                   break
                         elif ch8 == 2:
                              print('Enter card details...')
                              ch10 = int(input('Enter the last 4 digit number of your card:'))
                              ch11 = input('Enter DD/MM/YYYY of your card:')
                              print('Opening payment window...')
                              ch12 = int(input("enter the pin of your card:"))
                              ch14 = int(input('Enter the amount to be paid:'))
                              if ch14==t:
                                   print('Payment Successful')
                                   print('Booked your slot on...',x)
                                   print('Booking successful')
                                   print('HAVE A WONDERFUL DAY',g,'WITH YOUR DRIVE')
                                   print('='*55)
                              else:
                                   print('booking cancelled')
                                   break
                         else:
                              print('Unable to open payment window[SERVER DOWN]!!!!')
                              break
                         break
                         
                    elif ch == 2:
                          print("======================================================================[Welcome to Car Maintainance Section]===========================================================")
                          print('SELECT YOUR VEHCYCLE TYPE FROM BELOW')
                          print("Type 's' for SUV; type 'se' for SEDAN; type 'o' for OFF-ROADER")
                          print('Some Important Car parts listed below are available and can be replaced')
                          print('1) Spark Plugs \n2) The Battery \n3) Windshield \n4) Tires \n5) Suspensions(Front OR Rear) \n6) AC \n7) Clutch \n8) Sterring \n9) Side mirror \n10) ECM Repair')
                          print('='*55)
                          c = input("Enter a valid choice for vehcycle(s,se,o):")
                          print('='*55)

                          if c=='s':
                              while True:                              
                                   '''f=open("suv's.txt",'r')
                                   v=f.read()
                                   print(v)
                                   f.close()'''
                                   import vSUVread
                                   vSUVread.vsuv()
                                   
                                   a =int(input("Enter serial  nom. of preffered Company model: "))                              
                                   
                                   print('='*55)
                                   l=input('Enter N for continue or Enter W to go for another company model you have:')
                                   print('='*55)
                                   if l.upper()=='W':
                                        continue
                                   
                                   if a >= 10:
                                        print('INVALID CHOICE!!!!')
                                        break
                                   else:
                                        print('='*55)
                                        p=input('Enter your NAME:')
                                        print('='*55)
                                   
                                   if a==1:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=53543
                                        print('TOTAL AMOUNT TO BE PAID FOR [HYUNDAI CRETA],(FUEL TYPE:PETROL):',sum)
                                        
                                   elif a==2:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=62051
                                        print('TOTAL AMOUNT TO BE PAID FOR [HYUNDAI VENEU],(FUEL TYPE:PETROL):',sum)
                                   
                                   elif a==3:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=62426
                                        print('TOTAL AMOUNT TO BE PAID FOR [HYUNDAI EXTER],(FUEL TYPE:PETROL):',sum)

                                   elif a==4:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=59599
                                        print('TOTAL AMOUNT TO BE PAID FOR [KIA SELTOS],(FUEL TYPE:DIESEL):',sum)

                                   elif a==5:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=54920
                                        print('TOTAL AMOUNT TO BE PAID FOR [KIA SONET],(FUEL TYPE:PETROL):',sum)

                                   elif a==6:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=122372
                                        print('TOTAL AMOUNT TO BE PAID FOR [KIA CARNIVAL],(FUEL TYPE:DIESEL):',sum)

                                   elif a==7:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=64380
                                        print('TOTAL AMOUNT TO BE PAID FOR [MAHINDRA SCORPIO],(FUEL TYPE:DIESEL):',sum)

                                   elif a==8:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=61186
                                        print('TOTAL AMOUNT TO BE PAID FOR [MAHINDRA XUV300],(FUEL TYPE:PETROL):',sum)

                                   elif a==9:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=86467
                                        print('TOTAL AMOUNT TO BE PAID FOR [MAHINDRA XUV700],(FUEL TYPE:PETROL):',sum)
                                        
                                   print('='*55)
                                   print('choose a payment method')
                                   print("1)CASH \n2)PAYPAL")                                     
                                   print('='*55)
                                        
                                   ch8 = int(input('Enter payment method:'))
                                   print('Loading Payment window...')
                                   if ch8 == 1:
                                        print('Confirm Booking??')
                                        ch9 = input('YES OR NO:').lower()
                                        if ch9 =='yes'or'y':
                                             print('Booked your slot on...',x,'at',y)
                                             print('Booking successful')
                                             print('HAVE A WONDERFUL DAY',p,'WITH YOUR DRIVE')
                                        else:
                                             print('Booking Cancelled')
                                             break                                     
                                   elif ch8 == 2:
                                        print('Enter card details...')
                                        ch10 = int(input('Enter the last 4 digit number of your card:'))
                                        ch11 = input('Enter DD/MM/YYYY of your card:')
                                        print('Opening payment window...')
                                        ch12 = int(input("Enter the pin of your card:"))
                                        ch14 = int(input('Enter the amount to be paid:'))
                                        if ch14==sum:
                                             print('Payment Successful')
                                             print('Booked your slot on...',x,'at',y)
                                             print('Booking successful')
                                             print('HAVE A WONDERFUL DAY',p,'WITH YOUR DRIVE')
                                             print('='*55)
                                        else:
                                             print('booking cancelled')
                                             break
                                   else:
                                        print('Unable to open payment window[SERVER DOWN]!!!!')
                                        break
                                   break     
                                    
                          elif c=='se':
                              while True:
                                   '''f=open("sedan's.txt",'r')
                                   v=f.read()
                                   print(v)
                                   f.close()'''
                                   import vSEDANread
                                   vSEDANread.vsedan()

                                   a =int(input("Enter serial  nom. of preffered Company model: "))                              
                                   
                                   print('='*55)
                                   l=input('Enter N for continue or Enter W to go for another company model you have:')
                                   print('='*55)
                                   if l.upper()=='W':
                                        continue

                                   if a >= 10:
                                        print('INVALID CHOICE!!!!')
                                        break
                                   else:
                                        print('='*55)
                                        p=input('Enter your NAME:')
                                        print('='*55)

                                   if a==1:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=43456
                                        print('TOTAL AMOUNT TO BE PAID FOR [HYUNDAI AURA],(FUEL TYPE:DIESEL):',sum)
                                   
                                   elif a==2:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=45742
                                        print('TOTAL AMOUNT TO BE PAID FOR [HYUNDAI I20],(FUEL TYPE:PETROL):',sum)

                                   elif a==3:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=52739
                                        print('TOTAL AMOUNT TO BE PAID FOR [HYUNDAI VERNA],(FUEL TYPE:PETROL):',sum)

                                   elif a==4:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=117010
                                        print('TOTAL AMOUNT TO BE PAID FOR [HONDA ACCORD],(FUEL TYPE:PETROL):',sum)

                                   elif a==5:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=45846
                                        print('TOTAL AMOUNT TO BE PAID FOR [HONDA AMAZE],(FUEL TYPE:PETROL):',sum)

                                   elif a==6:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=81365
                                        print('TOTAL AMOUNT TO BE PAID FOR [HONDA CIVIC],(FUEL TYPE:DIESEL):',sum)

                                   elif a==7:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=38698
                                        print('TOTAL AMOUNT TO BE PAID FOR [MARUTI SWIFT D TOUR],(FUEL TYPE:PETROL):',sum)

                                   elif a==8:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=50276
                                        print('TOTAL AMOUNT TO BE PAID FOR [MARUTI CIAZ],(FUEL TYPE:PETROL):',sum)

                                   elif a==9:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=42697
                                        print('TOTAL AMOUNT TO BE PAID FOR [MARUTI DZIRE],(FUEL TYPE:PETROL):',sum)
                                        
                                   print('='*55)
                                   print('choose a payment method')
                                   print("1)CASH \n2)PAYPAL")                                     
                                   print('='*55)
                                        
                                   ch8 = int(input('Enter payment method:'))
                                   print('Loading Payment window...')
                                   if ch8 == 1:
                                        print('Confirm Booking??')
                                        ch9 = input('YES OR NO:').lower()
                                        if ch9 =='yes'or'y':
                                             print('Booked your slot on...',x,'at',y)
                                             print('Booking successful')
                                             print('HAVE A WONDERFUL DAY',p,'WITH YOUR DRIVE')
                                        else:
                                             print('Booking Cancelled')
                                             break                                     
                                   elif ch8 == 2:
                                        print('Enter card details...')
                                        ch10 = int(input('Enter the last 4 digit number of your card:'))
                                        ch11 = input('Enter DD/MM/YYYY of your card:')
                                        print('Opening payment window...')
                                        ch12 = int(input("Enter the pin of your card:"))
                                        ch14 = int(input('Enter the amount to be paid:'))
                                        if ch14==sum:
                                             print('Payment Successful')
                                             print('Booked your slot on...',x,'at',y)
                                             print('Booking successful')
                                             print('HAVE A WONDERFUL DAY',p,'WITH YOUR DRIVE')
                                             print('='*55)
                                        else:
                                             print('booking cancelled')
                                             break
                                   else:
                                        print('Unable to open payment window[SERVER DOWN]!!!!')
                                        break
                                   break

                          elif c=='o':
                              while True:
                                   '''f=open("off-roader's.txt",'r')
                                   v=f.read()
                                   print(v)
                                   f.close()'''
                                   import vOFFROADERread
                                   vOFFROADERread.voff()
                                   
                                   a =int(input("Enter serial  nom. of preffered Company model: "))                              
                                   
                                   print('='*55)
                                   l=input('Enter N for continue or Enter W to go for another company model you have:')
                                   print('='*55)
                                   if l.upper()=='W':
                                        continue

                                   if a >= 4:
                                        print('INVALID CHOICE!!!!')
                                        break
                                   else:
                                        print('='*55)
                                        p=input('Enter your NAME:')
                                        print('='*55)

                                   if a==1:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=63950
                                        print('TOTAL AMOUNT TO BE PAID FOR [MAHINDRA THAR],(FUEL TYPE:DIESEL):',sum)

                                   elif a==2:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=65305
                                        print('TOTAL AMOUNT TO BE PAID FOR [FORCE GURKHA],(FUEL TYPE:DIESEL):',sum)

                                   elif a==3:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=213907
                                        print('TOTAL AMOUNT TO BE PAID FOR [JEEP WRANGLER],(FUEL TYPE:PETROL):',sum)

                                   print('='*55)
                                   print('choose a payment method')
                                   print("1)CASH \n2)PAYPAL")                                     
                                   print('='*55)
                                        
                                   ch8 = int(input('Enter payment method:'))
                                   print('Loading Payment window...')
                                   if ch8 == 1:
                                        print('Confirm Booking??')
                                        ch9 = input('YES OR NO:').lower()
                                        if ch9 =='yes'or'y':
                                             print('Booked your slot on...',x,'at',y)
                                             print('Booking successful')
                                             print('HAVE A WONDERFUL DAY',p,'WITH YOUR DRIVE')
                                        else:
                                             print('Booking Cancelled')
                                             break                                     
                                   elif ch8 == 2:
                                        print('Enter card details...')
                                        ch10 = int(input('Enter the last 4 digit number of your card:'))
                                        ch11 = input('Enter DD/MM/YYYY of your card:')
                                        print('Opening payment window...')
                                        ch12 = int(input("Enter the pin of your card:"))
                                        ch14 = int(input('Enter the amount to be paid:'))
                                        if ch14==sum:
                                             print('Payment Successful')
                                             print('Booked your slot on...',x,'at',y)
                                             print('Booking successful')
                                             print('HAVE A WONDERFUL DAY',p,'WITH YOUR DRIVE')
                                             print('='*55)
                                        else:
                                             print('booking cancelled')
                                             break
                                   else:
                                        print('Unable to open payment window[SERVER DOWN]!!!!')
                                        break    
                                   break            
                    
                    elif ch == 3:
                          print("===================================================================[WELCOME TO PAINT RESTORATION SECTION]=============================================================")     
                          print("what would u like to do?")
                          print("1) Full Body paint \n2) Specific Body paint \n3) Custom paint \n4) Stock paint restoration")
                          print('='*55)
                          d = int(input('Enter the valid choice from above(1,2,3,4):'))
                          print('='*55)

                          if d == 1 or d==2:
                              while True:                              
                                   '''f=open("paint.txt",'r')
                                   v=f.read()
                                   print(v)
                                   f.close()'''
                                   import vPAINTread
                                   vPAINTread.vpaint()
                                   
                                   e =int(input("Enter serial  nom. of preffered Car Type: "))
                                   
                                   print('='*55)
                                   l=input('Enter N for continue or Enter W go for another car type you want:')
                                   print('='*55)
                                   if l.upper()=='W':
                                        continue
                                   
                                   if e >= 4:
                                        print('INVALID CHOICE!!!!')
                                        break
                                   else:
                                        print('='*55)
                                        p=input('Enter your NAME:')
                                        print('='*55)

                                   if e==1:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=43800
                                        print('TOTAL AMOUNT TO BE PAID FOR [SUV PAINT RESTORATION]:',sum)
                                   
                                   elif e==2:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=37800
                                        print('TOTAL AMOUNT TO BE PAID FOR [SEDAN PAINT RESTORATION]:',sum)
                                   
                                   elif e==3:
                                        ch3 = input("Enter your phone number: ")
                                        len1 = len(ch3)
                                        if len1 > 10 or len1 < 10:
                                             print("Invalid phone number enter a 10 digit number")
                                             break
                                        else:
                                             print("HELLO",p)
                                        
                                        x=input('Enter DATE(DD/MM/YYYY):')
                                        y=input('Enter Time(HH/MM)IST(AM/PM):')
                                        w=input('enter your STATE:')
                                        z=input('Enter your ADDRESS:')
                                        print('Your Information Has been SAVED...')
                                        
                                        sum=84360
                                        print('TOTAL AMOUNT TO BE PAID FOR [OFF-ROADERS PAINT RESTORATION]:',sum)
                                        

                                   print('='*55)
                                   print('choose a payment method')
                                   print("1)CASH \n2)PAYPAL")                                     
                                   print('='*55)
                                        
                                   ch8 = int(input('Enter payment method:'))
                                   print('Loading Payment window...')
                                   if ch8 == 1:
                                        print('Confirm Booking??')
                                        ch9 = input('YES OR NO:').lower()
                                        if ch9 =='yes'or'y':
                                             print('Booked your slot on...',x,'at',y)
                                             print('Booking successful')
                                             print('HAVE A WONDERFUL DAY',p,'WITH YOUR DRIVE')
                                        else:
                                             print('Booking Cancelled')
                                             break                                     
                                   elif ch8 == 2:
                                        print('Enter card details...')
                                        ch10 = int(input('Enter the last 4 digit number of your card:'))
                                        ch11 = input('Enter DD/MM/YYYY of your card:')
                                        print('Opening payment window...')
                                        ch12 = int(input("Enter the pin of your card:"))
                                        ch14 = int(input('Enter the amount to be paid:'))
                                        if ch14==sum:
                                             print('Payment Successful')
                                             print('Booked your slot on...',x,'at',y)
                                             print('Booking successful')
                                             print('HAVE A WONDERFUL DAY',p,'WITH YOUR DRIVE')
                                             print('='*55)
                                        else:
                                             print('booking cancelled')
                                             break
                                   else:
                                        print('Unable to open payment window[SERVER DOWN]!!!!')
                                        break
                                   break
                          
                          elif d == 3:
                               while True:
                                   print('Some best custom paints are available below')
                                   print("1) Candy colour \n2) Pearl colour \n3) Phalts colour \n4) Chameleon colour \n5) Chrome effect \n6) Neon colour \n7) Metallic colour")                                  
                                   
                                   f = int(input('Enter the valid choice from above(1,2,3,4,5,6,7):'))  
                                   
                                   print('='*55)
                                   l=input('Enter N for continue or Enter W go for another custom paint you want:')
                                   print('='*55)
                                   if l.upper()=='W':
                                        continue                                      
                                   
                                   if f == 1:
                                        p=5000 
                                        print("Price of Candy colour=",'₹',p,'/liter')
                                   elif f == 2:
                                        p=3000
                                        print("Price of Pearl colour=",'₹',p,'/liter')
                                   elif f == 3:
                                        p=4500
                                        print("Price of Phalts colour=",'₹',p,'/liter')
                                   elif f == 4:
                                        p=6000
                                        print("Price of Chameleon colour=",'₹',p,'/liter')
                                   elif f == 5:
                                        p=2500
                                        print("Price of Chrome effect=",'₹',p,'/liter')
                                   elif f == 6:
                                        p=5500
                                        print("Price of Neon colour=",'₹',p,'/liter')
                                   elif f == 7:
                                        p=6500
                                        print("Price of Metallic colour=",'₹',p,'/liter')
                                   else:
                                        print('NOT AVAILABLE!!!')
                                   
                                   print('='*55)
                                   g=input('Enter your name:')
                                   print('='*55)

                                   ch3 = input("Enter your phone number: ")
                                   len1 = len(ch3)
                                   if len1 > 10 or len1 < 10:
                                        print("Invalid phone number enter a 10 digit number")
                                        break
                                   else:
                                        print("HELLO",g)
                                        
                                   x=input('Enter DATE(DD/MM/YYYY):')
                                   y=input('Enter Time(HH/MM)IST(AM/PM):')
                                   w=input('enter your STATE:')
                                   z=input('Enter your ADDRESS:')
                                   print('Your Information Has been SAVED...')
                                   
                                   
                                   print('='*55)
                                   print('choose a payment method')
                                   print("1)CASH \n2)PAYPAL")                                     
                                   print('='*55)
                                        
                                   ch8 = int(input('Enter payment method:'))
                                   print('Loading Payment window...')
                                   if ch8 == 1:
                                        print('Confirm Booking??')
                                        ch9 = input('YES OR NO:').lower()
                                        if ch9 =='yes'or'y':
                                             print('Booked your slot on...',x,'at',y)
                                             print('Booking successful')
                                             print('HAVE A WONDERFUL DAY',g,'WITH YOUR DRIVE')
                                        else:
                                             print('Booking Cancelled')
                                             break                                     
                                   elif ch8 == 2:
                                        print('Enter card details...')
                                        ch10 = int(input('Enter the last 4 digit number of your card:'))
                                        ch11 = input('Enter DD/MM/YYYY of your card:')
                                        print('Opening payment window...')
                                        ch12 = int(input("Enter the pin of your card:"))
                                        ch14 = int(input('Enter the amount to be paid:'))
                                        if ch14==p:
                                             print('Payment Successful')
                                             print('Booked your slot on...',x,'at',y)
                                             print('Booking successful')
                                             print('HAVE A WONDERFUL DAY',g,'WITH YOUR DRIVE')
                                             print('='*55)
                                        else:
                                             print('booking cancelled')
                                             break
                                   else:
                                        print('Unable to open payment window[SERVER DOWN]!!!!')
                                        break
                                   break

                          elif d==4:
                               while True:
                                   print('Some best companies original paints are available below')
                                   print("1) Asian Paints \n2) Berger Paints India Limited \n3) Kansai Nerolac Paints Limited \n4) Nippon Paint (India) Company Limited \n5) PPG Asian Paints \n6) Akzo Nobel N.V. \n7) Indigo Paints")
                                   
                                   f = int(input('Enter the valid choice from above(1,2,3,4,5,6,7):'))
                                   
                                   print('='*55)
                                   l=input('Enter N for continue or Enter W go for another companies paint you want:')
                                   print('='*55)
                                   if l.upper()=='W':
                                        continue
                                   
                                   if f == 1:
                                        p=750 
                                        print("<AVG.Price> of Asian Paints=",'₹',p,'/liter')
                                   elif f == 2:
                                        p=375
                                        print("<AVG.Price> of Berger Paints India Limited=",'₹',p,'/liter')
                                   elif f == 3:
                                        p=293
                                        print("<AVG.Price> of Kansai Nerolac Paints Limited=",'₹',p,'/liter')
                                   elif f == 4:
                                        p=415
                                        print("<AVG.Price> of Nippon Paint (India) Company Limited=",'₹',p,'/liter')
                                   elif f == 5:
                                        p=586
                                        print("<AVG.Price> of PPG Asian Paints=",'₹',p,'/liter')
                                   elif f == 6:
                                        p=1500
                                        print("<AVG.Price> of Akzo Nobel N.V.=",'₹',p,'/liter')
                                   elif f == 7:
                                        p=450
                                        print("<AVG.Price> of Indigo Paints=",'₹',p,'/liter')
                                   else:
                                        print('NOT AVAILABLE!!!')
                                   
                                   print('='*55)
                                   g=input('Enter your name:')
                                   print('='*55)

                                   ch3 = input("Enter your phone number: ")
                                   len1 = len(ch3)
                                   if len1 > 10 or len1 < 10:
                                        print("Invalid phone number enter a 10 digit number")
                                        break
                                   else:
                                        print("HELLO",g)
                                        
                                   x=input('Enter DATE(DD/MM/YYYY):')
                                   y=input('Enter Time(HH/MM)IST(AM/PM):')
                                   w=input('enter your STATE:')
                                   z=input('Enter your ADDRESS:')
                                   print('Your Information Has been SAVED...')
                                   
                                   
                                   print('='*55)
                                   print('choose a payment method')
                                   print("1)CASH \n2)PAYPAL")                                     
                                   print('='*55)
                                        
                                   ch8 = int(input('Enter payment method:'))
                                   print('Loading Payment window...')
                                   if ch8 == 1:
                                        print('Confirm Booking??')
                                        ch9 = input('YES OR NO:').lower()
                                        if ch9 =='yes'or'y':
                                             print('Booked your slot on...',x,'at',y)
                                             print('Booking successful')
                                             print('HAVE A WONDERFUL DAY',g,'WITH YOUR DRIVE')
                                        else:
                                             print('Booking Cancelled')
                                             break                                     
                                   elif ch8 == 2:
                                        print('Enter card details...')
                                        ch10 = int(input('Enter the last 4 digit number of your card:'))
                                        ch11 = input('Enter DD/MM/YYYY of your card:')
                                        print('Opening payment window...')
                                        ch12 = int(input("Enter the pin of your card:"))
                                        ch14 = int(input('Enter the amount to be paid:'))
                                        if ch14==p:
                                             print('Payment Successful')
                                             print('Booked your slot on...',x,'at',y)
                                             print('Booking successful')
                                             print('HAVE A WONDERFUL DAY',g,'WITH YOUR DRIVE')
                                             print('='*55)
                                        else:
                                             print('booking cancelled')
                                             break
                                   else:
                                        print('Unable to open payment window[SERVER DOWN]!!!!')
                                        break                                   
                                   break
             