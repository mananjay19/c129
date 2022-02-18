from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv

starturl='https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
brower=webdriver.Chrome('chromedriver')
brower.get(starturl)
time.sleep(10)
headers=['name','lightyearsfromearth','planetmass','stellarmagnitude','discoverydate','hyperlink','planettype','planetradius','orbitalradius','orbitalperiod','eccentricity']
planetdata=[]
newplanetdata=[]
def scrape(): 
    for i in range(0,492):
        while True:
            time.sleep(2)
            soup=BeautifulSoup(brower.page_source,'html.parser')
            currentpagenum=int(soup.find_all('input',attrs={'class','page_num'})[0].get('value'))
            if currentpagenum<i:
                brower.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            elif currentpagenum>i:
                brower.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
            else:
                break
            for ultag in soup.find_all('ul',attrs={'class','exoplanet'}):
                litags=ultag.find_all('li') 
                templist=[]
                for index,litag in enumerate(litags):
                    if index==0:
                        templist.append(litag.find_all('a')[0].contents[0])
                    else:
                        try:
                            templist.append(litag.contents[0])
                        except:
                            templist.append('')
                hyperlinklitag=litags[0]
                templist.append('https://exoplanets.nasa.gov'+hyperlinklitag.find_all("a",href=True)[0]["href"])
                planetdata.append(templist)
            brower.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            print(f'{i}page done')

def scrapemoredata(hyperlink):
    try:
        page=requests.get(hyperlink)
        soup=BeautifulSoup(page.content,'html.parser')
        templist=[]
        for trtag in soup.find_all('tr',attrs={'class':'fact_row'}):
            tdtags=trtag.find_all('td')
            for tdtag in tdtags:
                try:
                    templist.append(tdtag.find_all('div',attrs={'class':'value'})[0].contents[0])
                except:
                    templist.append('')
        newplanetdata.append(templist)
    except:
        time.sleep(1)
        scrapemoredata(hyperlink)

scrape()
for index,data in enumerate(planetdata):
    scrapemoredata(data[5])
    print(f'{index+1} pagedone2')
finalplanetdata=[]

for index,data in enumerate(planetdata):
    newplanetdataelement=newplanetdata[index]
    newplanetdataelement=[elem.replace('\n','')for elem in newplanetdataelement]
    newplanetdataelement=newplanetdataelement[:7]
    finalplanetdata.append(data+newplanetdataelement)

with open('scrapper2.csv','w')as f:
    c=csv.writer(f)
    c.writerow(headers)
    c.writerows(newplanetdata)