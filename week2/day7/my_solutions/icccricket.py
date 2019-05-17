from bs4 import BeautifulSoup
import requests

wiki="https://www.icc-cricket.com/rankings/mens/team-rankings/odi "
source = requests.get(wiki).text
soup = BeautifulSoup(source)
print (soup.prettify())



right_table=soup.find('table', class_="table-body__cell rankings-table__team u-text-left")
A=[]
B=[]
C=[]
D=[]

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    if len(cells) == 4:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())