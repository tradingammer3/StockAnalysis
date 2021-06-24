from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime 
import time


url = "https://www.sec.gov/cgi-bin/current?q1=0&q2=0&q3=13F"

#get all links
page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data, "lxml")
days_url = []


for link in soup.find_all('a'):
  if 'index' in link.get('href'):
    url_to_save = link.get('href')
    days_url.append(url_to_save)
    
time.sleep(10)    
    
# print(days_url)
days_url = days_url[0:3]
for item in days_url:  
  time.sleep(10)
  index ='https://www.sec.gov'+item
  index = pd.read_html(index)
  index = index[0]
  index = index[(index['Document'].str.contains('.html')) & (index['Type'].str.contains('INFORMATION TABLE'))]
  try:
  	index = index['Document'].iloc[0]
  except:
  	index = ''

  
  time.sleep(10)  
  # print(index)
  url = item.replace('-index.html','')
  url = url.replace('-','')
  url = 'https://www.sec.gov'+  url + '/xslForm13F_X01/' + index
  url = url.replace('html','xml')
  cik_company = item.split('data/')[1].split('/')[0]
  #add 1 second between loop iterations to comply with SEC site #policy
  time.sleep(10)
  # print(url)
  
  try:
  	DF_13F = pd.read_html(url)
  	DF_13F = DF_13F[-1]
  	DF_13F = DF_13F.iloc[2:]
  	new_header = DF_13F.iloc[0]
  	DF_13F.columns = new_header
  	DF_13F = DF_13F.iloc[1:]
  	DF_13F['date_reported'] = datetime.now().strftime("%Y%m")
  	DF_13F['cik_company'] = cik_company
  	value_to_store_as_index = DF_13F['CUSIP']+cik_company + datetime.now().strftime("%Y%m")
  	DF_13F['indice'] = value_to_store_as_index
  	DF_13F = DF_13F[['indice','NAME OF ISSUER','TITLE OF CLASS','CUSIP','(x$1000)','PRN AMT','PRN','date_reported','cik_company']]
  	print('new SEC13 report added to DataFrame')
  	print(DF_13F)

  except:
  	print('error')
  	pass


  
  
  
