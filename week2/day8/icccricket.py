from bs4 import BeautifulSoup

import requests

wiki="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(wiki).text
soup = BeautifulSoup(source,"lxml")
#print (soup.prettify())



right_table=soup.find('table', class_="table")
A=[]
B=[]
C=[]
D=[]

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    
    if len(cells) == 5:
        A.append(cells[1].text.strip())
        B.append(cells[2].text.strip())
        C.append(cells[3].text.strip())
        D.append(cells[4].text.strip())
        
        
        
import pandas as pd
from collections import OrderedDict

column=['team','weight matches','points','rating']
col_data = OrderedDict(zip(column,[A,B,C,D]))
df = pd.DataFrame(col_data) 
df.to_csv("data/former.csv")



