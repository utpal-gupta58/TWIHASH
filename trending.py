from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://timesofindia.indiatimes.com/sports'
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close
page_soup= soup(page_html,"html.parser")

containers= page_soup.findAll("div",{"class":"gocricketwidget_con seowdtls"}) 
#print(len(containers))
  
#print(soup.prettify(containers[0]))
filename="trends.txt"
f=open(filename,"w")

container= containers[0]

for topic in container.findAll("div",{"class":"gocricket"}):
    top=topic.a.text
    print(top)
    f.write("%s\n"%top)
# topic = container.findAll("div",{"class":"gocricket"})
# print(topic[0].text) 



# headers="topics\n"
# f.write(headers)

# for container in containers:
#      topics=   topic[0].text
#      topic=container.findAll("div",{"class":"gocricket"})

#print("topics:"+ topics)



