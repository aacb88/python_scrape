import urllib2, csv
import mechanize
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')
    
br = mechanize.Browser()
br.open('http://enrarchives.sos.mo.gov/enrnet/')

br.select_form(nr=0)

control = br.form.find_control(id = "MainContent_cboRaces")

for item in control.items:
  if item.name == "460006719":
    item.selected = True
  
    response = br.submit(nr=1)

html = br.response().read()

soup = BeautifulSoup(html, "html.parser")

main_table = soup.find('table', {'id': 'MainContent_dgrdRaceResults'})


candidate_data = []
#for row in main_table.find_all('tr'):
  #data = [cell.text for cell in row.find_all('td')]
  #candidate_data.append(data)

county_table =soup.find('table', {'id': 'MainContent_dgrdCountyRaceResults'})

headers = county_table.find('tr', [0])

for row in headers:
  fields = [cell.text for cell in row.find_all('th')]
  candidate_data.append(fields)

#for tr[0] in county_table.find_all('th'):
    #field_name = [cell.text for cell in header.find_all('th')]
    #candidate_data.append(field_name)

#for header in county_table.find_all('tr'):
  #field_name = [cell.text for cell in header.find_all('th')]
  #candidate_data.append(field_name)

for row in county_table.find_all('tr'):
  data = [cell.text for cell in row.find_all('td')]
  candidate_data.append(data)

outfile = open("./candidate_table.csv", "w")
writer = csv.writer(outfile)
writer.writerows(candidate_data)