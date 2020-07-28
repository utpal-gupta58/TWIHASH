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

csv_file=open('India_today_4.csv','a+')
csv_writer=csv.writer(csv_file)
# csv_writer.writerow(['Date','Time','Headline','Keywords'])

sports=["cricket","football","tennis","badminton","athletics","hockey","other-sports"]
for i in range(0,7):
	print(sports[i])
	source=requests.get("https://www.indiatoday.in/sports/"+sports[i]).text
	soup=BeautifulSoup(source,'lxml')

	for a1 in soup.find_all('div',class_='detail'):
		a=a1.find('a')
		link=str(a.attrs['href'])
		print(link)
		headline=a.text
		source1=requests.get("https://www.indiatoday.in"+link).text
		soup1=BeautifulSoup(source1,'lxml')
		try:
			keyword=soup1.find('meta',attrs={'name':'news_keywords'})
			data_keywords=str(keyword.attrs['content'])
		except:
			   data_keywords=""	
			
		print(data_keywords)
		print()

		csv_writer.writerow([today,current_time,headline,data_keywords])	

csv_file.close()				