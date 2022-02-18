import csv
dataset1=[]
dataset2=[]
with open('dataset_1.csv','r')as f:
    c=csv.reader(f)
    for row in c:
        dataset1.append(row)
with open('dataset_2sorted.csv','r')as f:
    c=csv.reader(f)
    for row in c:
        dataset2.append(row)

headers1=dataset1[0]
planet1=dataset1[1:]
headers2=dataset2[0]
planet2=dataset2[1:]

headers=headers1+headers2
planetdata=[]
for index,data in enumerate(planet1):
    planetdata.append(planet1[index]+planet2[index])
with open('final3.csv','a+')as f:
    c=csv.writer(f)
    c.writerow(headers)
    c.writerows(planetdata)