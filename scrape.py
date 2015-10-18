import urllib2, csv
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.open('http://enrarchives.sos.mo.gov/enrnet/')

#Fill out the form
br.select_form('Form1')
print form


  
#Submit the form
#br.submit()

#html = br.response().read()

#print html
