import csv
def aphatchback():
    with open("PurHatchback.csv",'r') as f:
        rec = list(csv.reader(f))
    found = False
    m = input("Enter the sr.no.:")

    for i in rec:
        if i[0] == m:
            print("current:",i[5])
            i[5] = input("ENTER NEW:")
            new = i[5]
            found = True
            break
    with open("PurHatchback.csv", 'w', newline='') as f:
        
        r = csv.writer(f,delimiter=',')
        r.writerows(rec)
    if found:
        print("UPDATED")
    else:
        print("record not found")
    for i in rec:
        print('x--------x--------x--------x--------x--------x--------x--------x')
        print('|',i[0],'|',i[1],'|',i[2],'|',i[3],'|',i[4],'|',i[5],'|')
    print('x--------x--------x--------x--------x--------x--------x--------x')

#print(new)
        

