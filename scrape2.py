import urllib2, csv
import mechanize
from bs4 import BeautifulSoup
#reading unicode
import sys
reload(sys)
sys.setdefaultencoding('utf8')
    
br = mechanize.Browser()
br.open('http://enrarchives.sos.mo.gov/enrnet/')

#selecting the first form 
br.select_form(nr=0)

#Selecting Auditor Race for Main Page
control = br.form.find_control(id = "MainContent_cboRaces")

for item in control.items:
    if item.name == "460006719":
        item.selected = True

#Hit second submit button  
response = br.submit(nr=1)

html = br.response().read()

soup = BeautifulSoup(html, "html.parser")

main_table = soup.find('table', {'id': 'MainContent_dgrdRaceResults'})

#Creating Output
county_data = []

county_table =soup.find('table', {'id': 'MainContent_dgrdCountyRaceResults'})

for row in county_table.find_all('tr'):
    headers = [cell.text for cell in row.find_all('th')]
    if headers:
        county_data.append(headers)
    data = [cell.text for cell in row.find_all('td')]
    if data:
        county_data.append(data)

#for row in county_table.find_all('tr'):
    #headers = [cell.text for cell in row.find_all('th')]
    #county_data.append(headers)
    #data = [cell.text for cell in row.find_all('td')]
    #county_data.append(data)
    

outfile = open("./county_table.csv", "w")
writer = csv.writer(outfile)
writer.writerows(county_data)