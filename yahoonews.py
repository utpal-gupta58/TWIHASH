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

csv_file=open('yahoonews_data_4.csv','a+',encoding="utf-8")
csv_writer=csv.writer(csv_file)
# csv_writer.writerow(['Date','Time','Headline','Keywords'])

source= requests.get('https://in.news.yahoo.com/sports').text
soup=BeautifulSoup(source,'lxml')

y0=soup.find('div',attrs={'id':'Main'})
for y1 in y0.find_all('ul',class_='My(0) Ov(h) P(0) Wow(bw)'):
		for y2 in y1.find_all('li'):
			y3=y2.find('h3')
			y4=y3.find('a')
			headline=y4.text
			print(headline)
			# encoded=headline.encode('cp1252')
			# headline=encoded.decode('utf-8')
			link=str(y4.attrs['href'])
			source1=requests.get('https://in.news.yahoo.com'+link).text
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