import csv
def avpaint():
    with open("vPAINT.csv",'r') as f:
        rec = list(csv.reader(f))
    found = False
    m = input("Enter the sr.no.:")

    for i in rec:
        if i[0] == m:
            print("current:",i[7])
            i[7] = input("ENTER NEW:")
            new = i[7]
            found = True
            break
    with open("vPAINT.csv", 'w', newline='') as f:
        
        r = csv.writer(f,delimiter=',')
        r.writerows(rec)
    if found:
        print("UPDATED")
    else:
        print("record not found")
    for i in rec:
        print('x--------x--------x--------x--------x--------x--------x--------x--------x')
        print('|',i[0],'|',i[1],'|',i[2],'|',i[3],'|',i[4],'|',i[5],'|',i[6],'|',i[7],'|')
    print('x--------x--------x--------x--------x--------x--------x--------x--------x')

#print(new)
        

