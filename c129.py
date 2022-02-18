import csv
data=[]
with open('dataset_2.csv','r')as f:
    c =csv.reader(f)
    for row in c:
        data.append(row)

headers=data[0]
planetdata=data[1:]
for d in planetdata:
    d[2]=d[2].lower()
planetdata.sort(key=lambda planetdata: planetdata[2])
with open('dataset_2sorted.csv','a+')as f:
    c=csv.writer(f)
    c.writerow(headers)
    c.writerows
    c.writerow(planetdata)