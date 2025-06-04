import csv
def userprofile():
    db = open("extracted.txt", 'r')
    l = db.readlines()
    for i in l:
        username, password = i.strip().split(',')
    with open(f'{username}.csv', 'r') as f:
        r = csv.reader(f)
        h = next(r)
        print('x--------x------------x------------x------------x--------------x')
        print('|', h[0], '|', h[1], '|', h[2], '|', h[3], '|')
        print('x--------x------------x------------x------------x--------------x')

        for row in r:
            print('x--------x------------x------------x------------x--------------x')
            print('|',row[0],'|','\t',row[1],'|',row[2],'|',row[3],'|')
        
        print('x--------x------------x------------x------------x--------------x')