import urllib2, csv
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.open('http://enrarchives.sos.mo.gov/enrnet/')

br.select_form(nr=0)

control = br.form.find_control(id = "MainContent_cboRaces")

for item in control.items:
  if item.name == "750003143":
    item.selected = True
  
    response = br.submit(nr=1)

    html = br.response().read()

    print html
  
