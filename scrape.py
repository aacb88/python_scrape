import urllib2, csv
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.open('http://enrarchives.sos.mo.gov/enrnet/')

#Fill out the form
if br.form["MainContent_cboRaces"]== ["------Missouri Statewide Offices-----"]:
  br.form["MainContent_cboRaces"].value = ["460006719"]
  
#Submit the form
br.submit()

html = br.response().read()

print html
