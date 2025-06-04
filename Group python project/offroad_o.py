import csv
def offroad():
    #fields = ['Sr.no','Model Name','Fuel Type','Drive Type','Luggage Space','Rental Price']
    with open("Offroad.csv",'a',newline='') as f:
        rec = csv.writer(f,delimiter=',')
        #rec.writerow(fields)
        while True:
            s = int(input("Enter your Sr.no:"))
            m = input('Enter Model name of the car:')
            f = input("Enter fuel type fo car:")
            l = int(input("Enter Luggage space avaiable:"))
            d = input("Enter Drive Type:")
            r = input("Enter Rental Price:")
            R = [s,m,f,l,d,r]
            rec.writerow(R)
            ch = input("more data?")
            if ch == 'n' or ch == 'no':
                break
