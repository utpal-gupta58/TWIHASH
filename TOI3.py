from bs4 import BeautifulSoup
import requests
import csv
import time 

from datetime import datetime
from datetime import date

now = datetime.now()
today = date.today()
current_time = now.strftime("%H:%M:%S")

print("Current Time =", current_time)
print("Today's date:", today)

source=requests.get('https://timesofindia.indiatimes.com/sports').text

soup=BeautifulSoup(source,'lxml')


csv_file=open('toidata_4.csv','a+')
csv_writer=csv.writer(csv_file)
# csv_writer.writerow(['date','Time','Headline','Keywords'])

anchor1=soup.find_all('div',class_='news-section clearfix')
b=len(anchor1)

for i in range(1,b):
	for anchor3 in anchor1[i].find_all('span',class_='w_tle'):
		links=anchor3.find('a')
		link=str(links.attrs['href'])
		if link[0]!='h':
			source1=requests.get('https://timesofindia.indiatimes.com'+link).text
		else:
		    source1=requests.get(link).text	
		soup1=BeautifulSoup(source1,'lxml')
		a=soup1.find('section',class_='title_section clearfix')
		try:
			metas=a.find('h1')
			if 'data-keywords' in metas.attrs:
				headline=links.text
				print(headline)
				data_keywords=str(metas.attrs['data-keywords'])
				data_keywords=data_keywords.replace(',',' ')
				print(data_keywords)
				print()
				csv_writer.writerow([today,current_time,headline,data_keywords])
		except:
			pass	


for a1 in soup.find_all('div',class_='section_wdgt clearfix'):
	for a3 in a1.find_all('span',class_='w_tle'):
		links=a3.find('a')
		headline=links.text
		# print(headline)
		link=str(links.attrs['href'])
		source1=requests.get('https://timesofindia.indiatimes.com'+link).text
		soup1=BeautifulSoup(source1,'lxml')
		a=soup1.find('section',class_='title_section clearfix')
		try:
			metas=a.find('h1')
			if 'data-keywords' in metas.attrs:
				data_keywords=str(metas.attrs['data-keywords'])
				data_keywords=data_keywords.replace(',',' ')
				csv_writer.writerow([today,current_time,headline,data_keywords])
				# f1.write("%s\n"%data_keywords)
		except Exception as e:
			pass
		print(data_keywords)
		print()

# f1.close()
csv_file.close()