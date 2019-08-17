from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import shlex
import json

#import urllib2
i=0
browser = webdriver.Chrome()
airport=['EPWA','EPKK','EPGD','EPKT','EPMO','EPWR','EPPO','EPRZ','EPSC','EPBY','EPLL','EPLB','EPZG','EPRA','EPSY']
#city=airport[0]
#url='https://www.aviationweather.gov/metar/data?ids='+city+'&format=raw&date=0&hours=0'
all_every =[]
all_every.append(['Airport','Temperature'])
for air in airport:	
	#browser.implicitly_wait(1)
	browser.implicitly_wait(1) #implicit wait for 10 sec.
	browser.get('https://www.aviationweather.gov/metar/data?ids='+air+'&format=raw&hours=0&taf=off&layout=off&date=0')
	first = browser.find_element_by_id('awc_main_content')
	#result=first.get_attribute("text")
	result=first.get_attribute("textContent")
	result=result.split("2018")[1]
	#print result
	every=shlex.split(result)
	all_every.append([every[0],every[5].split('/')[0]])
	for temp in every:
		print temp #we have all info,line by line
	print ("\n")
with open('data.json','w') as outfile:
	json.dump(all_every,outfile)
#x = soup.body.find('div', attrs={'class' : 'container'}).text

