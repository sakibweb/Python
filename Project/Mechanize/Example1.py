from mechanize import Browser

br = Browser()
br.open('http://www.city-data.com/')

br.find_link(text='CT')

req = br.click_link(text='CT')
br.open(req)

print br.geturl()

f = br.retrieve('http://pics3.city-data.com/images/data-stats-new.png')[0]
print f
fh = open(f)



#print br.response().read()
