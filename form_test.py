import mechanize
br = mechanize.Browser()

br.open('http://enrarchives.sos.mo.gov/enrnet/')

for form in br.forms():
    print "Form name",form.name
    print form

