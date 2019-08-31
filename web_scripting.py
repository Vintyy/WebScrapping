# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 20:53:51 2019

@author: vineeth.vijay.das
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 23:50:07 2019
    
@author: vineeth.vijay.das
"""

import requests 
import csv
csvfile = 'C:/Users/vineeth.vijay.das/Desktop/Python/Web_Scrapping/2017.csv'# location of the CSV file
import bs4

y = 2017 # to initialize year 
m = 1
d = 1
numbr = 42736 # constant number for the year 2010 - 40179, 2011 - 40544, 2012(leap year) -40909, 2013 - 41275, 2014 - 41640, 2015 - 42005, 2016(leap) - 42370, 2017 - 42736, 2018 - 43101, 2019 -43466 

def to_export(b):# function for traversing through the xml codes
    res = requests.get(b)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    #code to add the title - Respective dates before the details
    with open(csvfile,"a") as output:
        writer = csv.writer(output,lineterminator='\n')
        for i in soup:
            writer.writerow([soup.title.encode("utf-8")])
                
     # used this logic to get the appropriate hyperlink and news headings   
    b = soup.find_all("span",{"style":"font-family:arial ;font-size:12;color: #006699"})
    with open(csvfile,"a") as output:
        writer = csv.writer(output,lineterminator='\n')
        for i in b:
            for j in i:
                #print(j)
                writer.writerow([j.encode("utf-8")])    
    

for i in range(365):# loop to be activated for one year
# loop for jan till july mpnths having 31 days 
    if m%2==1 and m <=6:
    
        a = 'https://timesofindia.indiatimes.com/'+str(y)+'/'+str(m)+'/'+str(d)+'/archivelist/year-'+str(y)+',month-'+str(m)+',starttime-'+str(numbr)+'.cms'
        
            
        print(a)
        to_export(a) #calling function  to export the data
        d = d + 1
        if d>=32:# to re-initialize the values
            
            d=1
            m=m+1
            numbr = numbr + 1
            #print(m)
        
# for February as the month is different compared to other months       
    if m==2:
        a = 'https://timesofindia.indiatimes.com/'+str(y)+'/'+str(m)+'/'+str(d)+'/archivelist/year-'+str(y)+',month-'+str(m)+',starttime-'+str(numbr)+'.cms'
        print(a)
        to_export(a) #calling function to export the data
        d = d + 1
        if y%4==0 and d==29:# loop for the leap year
            numbr = numbr + 1
            a = 'https://timesofindia.indiatimes.com/'+str(y)+'/'+str(m)+'/'+str(d)+'/archivelist/year-'+str(y)+',month-'+str(m)+',starttime-'+str(numbr)+'.cms'
            print(a)
            to_export(a) #calling function to export the data
            
        if d==29:# loop to change the month from february
            d = 1
            m=m+1     
            
# loop for jan till june months having 30 days        
    if m%2==0 and (m<=7 and m!=2):# changed here
        a = 'https://timesofindia.indiatimes.com/'+str(y)+'/'+str(m)+'/'+str(d)+'/archivelist/year-'+str(y)+',month-'+str(m)+',starttime-'+str(numbr)+'.cms'
        print(a)
        to_export(a) #calling function to export the data
        d = d + 1    
        if d==31:
            d=1
            m=m+1
            if m==7:
                numbr = numbr + 1
       
# loop for July till Dec months having 30 days    
    if m%2==1 and (m>=7 and m<=12):
        a = 'https://timesofindia.indiatimes.com/'+str(y)+'/'+str(m)+'/'+str(d)+'/archivelist/year-'+str(y)+',month-'+str(m)+',starttime-'+str(numbr)+'.cms'
        print(a)
        to_export(a) #calling function to export the data
        d = d + 1
        if m == 7 and d==31:  # just for the 31st of july as it doesn't follow pattern
            numbr = numbr + 1
            a = 'https://timesofindia.indiatimes.com/'+str(y)+'/'+str(m)+'/'+str(d)+'/archivelist/year-'+str(y)+',month-'+str(m)+',starttime-'+str(numbr)+'.cms'
            print(a)
            to_export(a) #calling function to export the data
        if d >=31:
            d=1
            m=m+1
            numbr = numbr + 1
        
        
#loop for August till Dec months having 31 days 
    if m%2==0 and m>=7:
        a = 'https://timesofindia.indiatimes.com/'+str(y)+'/'+str(m)+'/'+str(d)+'/archivelist/year-'+str(y)+',month-'+str(m)+',starttime-'+str(numbr)+'.cms'
        print(a)
        to_export(a) #calling function to export the data
        d = d + 1
        if d==32:
            d = 1
            m = m + 1

            
    #print(d)
    numbr = numbr + 1    
    


