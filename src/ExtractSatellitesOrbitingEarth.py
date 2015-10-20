#!/usr/bin/python
''' The data of all of the satellites orbiting the Earth was 
acquired from the UCS Satellite Database located at:
www.ucsusa.org/satellite_database
The version used here is the most recent'''

import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import requests
import re

#Scrape the UCS Satellite Database webpage to get the 
#most up to date database excel file
http = httplib2.Http()
status, response = http.request('http://www.ucsusa.org/nuclear-weapons/space-weapons/satellite-database.html')

links = []
for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
	links.append(str(link))

for link in links:
	if "Excel" in link:
		myLink = re.search('"(.+?)"', link)
		if myLink:
			foundLink = myLink.group(1)
			#print(foundLink)


#Now that we have the link to the most up to date excel file
#We can download and save it
req = requests.get(foundLink)
with open("UCS_Satellite_Database_MostRecent.xls", "wb") as code:
	code.write(req.content)
#This file has all of the current satellites orbiting our planet
#(Updated approximately every 3 months by UCS)


