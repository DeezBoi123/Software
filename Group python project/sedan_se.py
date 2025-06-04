import csv
def sedan():
    #fields = ['Sr.no','Model Name','Fuel Type','Luggage Space','Rental Price']
    with open("SEDAN.csv",'a',newline='') as f:
        rec = csv.writer(f,delimiter=',')
        #rec.writerow(fields)
        while True:
            s = int(input("Enter your Sr.no:"))
            m = input('Enter Model name of the car:')
            f = input("Enter fuel type fo car:")
            l = int(input("Enter Luggage space avaiable:"))
            r = input("Enter Rental Price:")
            R = [s,m,f,l,r]
            rec.writerow(R)
            ch = input("more data?")
            if ch == 'n' or ch == 'no':
                break
