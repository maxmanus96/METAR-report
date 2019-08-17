from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import shlex
import json
# eppo 4,epll  6,eplb 7,epzg 7 bak
#import urllib2
i=0
browser = webdriver.Chrome()
airport=['EPWA','EPKK','EPGD','EPKT','EPMO','EPWR','EPPO','EPRZ','EPSC','EPBY','EPLL','EPLB','EPZG','EPRA','EPSY']
#city=airport[0]
#url='https://www.aviationweather.gov/metar/data?ids='+city+'&format=raw&date=0&hours=0'
all_every =[]
all_every.append(['Airport','Temperature'])
#all_every.append(['Airport','Report_time','Winds','Weather','Visibility','Temperature'])
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
#	if any('/' in string for string in every):
 #       	print string
	for s in filter (lambda x: '/' in x, every): all_every.append([every[0],s.split('/')[0]])
#	if(every[0]=='EPPO'):
#		all_every.append([every[0],every[4].split('/')[0]])
#	elif(every[0]=='EPWA'):
#		all_every.append([every[0],every[4].split('/')[0]])
#	elif(every[0]=='EPMO'):
#		all_every.append([every[0],every[4].split('/')[0]])
#	elif(every[0]=='EPGD'):
#		all_every.append([every[0],every[4].split('/')[0]])
#	elif(every[0]=='EPRA'):
#		all_every.append([every[0],every[4].split('/')[0]])	
#	elif(every[0]=='EPLL'):
#		all_every.append([every[0],every[6].split('/')[0]])
#	elif(every[0]=='EPKK'):
#		all_every.append([every[0],every[5].split('/')[0]])	
#	elif(every[0]=='EPZG'):
#		all_every.append([every[0],every[7].split('/')[0]])
#	else:
#		all_every.append([every[0],every[5].split('/')[0]])	
	#all_every.append(every)
	for temp in every:
		print temp #we have all info,line by line
	print ("\n")
with open('data.json','w') as outfile:
	json.dump(all_every,outfile)
#x = soup.body.find('div', attrs={'class' : 'container'}).text

