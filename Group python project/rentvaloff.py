import csv
with open("SUV.csv",'r') as f:
    rec = list(csv.reader(f))
found = False
m = input("Enter the sr.no.:")

for i in rec:
    if i[0] == m:
        new = i[4]
        found = True
        break
print(new)