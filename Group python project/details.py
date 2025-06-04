import csv
def detail():
    while True:
        db = open("extracted.txt", 'r')
        l = db.readlines()
        for i in l:
            username, password = i.strip().split(',')
        with open(f'{username}.csv', 'a', newline='') as f:
            rec = csv.writer(f, delimiter=',')
            d1 = input("Postal CODE: ")
            d2 = input("Name On Card: ")
            d4 = input("Enter date of purchase(yyyy-mm-dd)")
            d3 = input("CVC- [three digit code number on back of your card]:")
            if len(d3) == 3:
                f.seek(0, 2)
                if f.tell() == 0:
                    rec.writerow(['POSTAL CODE', 'Name', 'CVC','Date_of_Purchase'])
                rec.writerow([d1, d2, d3, d4])
                print("Car booked for\nThank you for your purchase :)")
                print("Going back to car selection menu")
                break
            else:
                print("Input correct code!!!")
                continue
