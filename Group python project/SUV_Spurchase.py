import csv
def PSUV():
    #fields = ['Sr.no','Model Name','Engine Config.','Transmission','Damage History','Price']
    with open("PurSUV.csv",'a',newline='') as f:
        rec = csv.writer(f,delimiter=',')
        #rec.writerow(fields)
        while True:
            s = int(input("Enter your Sr.no:"))
            m = input('Enter Model name of the car:')
            e = input("Enter Engine Config of car:")
            t = input("Enter Transmission avaiable:")
            d = input("Enter Damage History:")
            r = input("Enter Price:")
            R = [s,m,e,t,d,r]
            rec.writerow(R)
            ch = input("more data?")
            if ch == 'n' or ch == 'no':
                break
