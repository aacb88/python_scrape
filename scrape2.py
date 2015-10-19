
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
for row in main_table.find_all('tr'):
  data = [cell.text for cell in row.find_all('td')]
  candidate_data.append(data)

outfile = open("./candidate_table.csv", "w")
writer = csv.writer(outfile)
writer.writerows(candidate_data)

#county_table =soup.find('table', {'id': 'MainContent_dgrdCountyRaceResults'})

#for header in county_table.find_all('th'):
  #data = [cell.text for cell in row.find_all('th')]
  #print data

#for row in county_table.find_all('tr'):
  #data = [cell.text for cell in row.find_all('td')]


