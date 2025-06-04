import csv
fields = ['Sr_no','Model_Name','Fuel_Type','Spark_Plugs','Battery','Windshield','Tires','Suspensions_FR','AC','Clutch','Sterring','Side_mirror','ECM_Repair']
with open("vSEDAN.csv",'a',newline='') as f:
    rec = csv.writer(f,delimiter=',')
    rec.writerow(fields)
    while True:
        s = int(input("Enter your Sr.no:"))
        m = input('Enter Model name of the car:')
        f = input("Enter fuel type fo car:")
        l = int(input("Enter price of Spark_Plugs:"))
        r = int(input("Enter price of battery :"))
        d = int(input("Enter price of Windshield:"))
        p = int(input("Enter price of Tires:"))
        q = int(input("Enter price of Suspensions_FR:"))
        x = int(input("Enter price of AC:"))
        y = int(input("Enter price of Clutch:"))
        a = int(input("Enter price of Sterring:"))
        e = int(input("Enter price of Side_mirror:"))
        z = int(input("Enter price of ECM_Repair:"))

        R = [s,m,f,l,r,d,p,q,x,y,a,e,z]
        rec.writerow(R)
        ch = input("more data?")
        if ch == 'n' or ch == 'no':
            break
