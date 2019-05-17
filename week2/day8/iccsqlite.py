from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import sqlite3
from collections import OrderedDict

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
        
        
        


column=['team','weight matches','points','rating']
col_data = OrderedDict(zip(column,[A,B,C,D]))
df = pd.DataFrame(col_data) 

conn = sqlite3.connect ( 'icc.db' )
c = conn.cursor()
c.execute ("""CREATE TABLE icc(
          
           team TEXT,
          weight TEXT,
          point INTEGER,
          Rrating INTEGER
          )""")




for i in range(len(A)):
    c.execute("insert into icc values('{}','{}','{}','{}')".format(A[i],B[i],C[i],D[i]))
c.execute("select *from icc")
print(c.fetchall())



