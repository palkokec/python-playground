import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://www.vssr.sk/vyhladavanie/aktualne-vyzvy_')
 
# check status code for response received
# success code - 200
#print(r)
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

elms = soup.find_all('div', class_= 'lc-itm-txt')
for elm in elms:
    print(elm.prettify())
