from wordcloud import WordCloud,STOPWORDS
import numpy as np
import os

from PIL import Image

currdir=os.path.dirname(__file__)

def create_wordcloud(text,i):
	mask=np.array(Image.open(os.path.join(currdir,"download.jpg")))


	stopwords=set(STOPWORDS)

	wc=WordCloud(background_color="white", mask=mask, max_words=3,stopwords=stopwords)

	wc.generate(text)

	wc.to_file(os.path.join(currdir,str(i)+".png"))

for i in range(0,70):
	f=open("D:/Work/BTP/Extracted Data/1/"+str(i)+".txt",'r')
	a=f.read();
	create_wordcloud(a,i)