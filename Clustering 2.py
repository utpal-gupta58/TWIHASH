import pandas as pd
import numpy as np
import csv

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import cluster


stemmer=PorterStemmer()

sw=stopwords.words('english')
# print(sw)

def tokenizer(keyword):
	return [stemmer.stem(w) for w in keyword.split(' ')]

# keywords={'campaign building',
#           'ppc campaign generator',
#           'how to build ppc campaigns',
#           'how do you group keywords',
#           'how to group keywords',
#           'keyword grouper',
#           'keyword grouping software',
#           'ppc campaign builder',
#           'best software to group keywords','tokyo','Amritsar Punjab','punjab','Japan tokyo'}

keywords=[]


file=open("D:/Work/BTP/Extracted Data/1/toidata_1.csv")
reader=csv.reader(file)
lines=len(list(reader))
print(lines)

df1=pd.read_csv("D:/Work/BTP/Extracted Data/1/toidata_1.csv")
for i in range(1,lines,2):
     keywords.append(df1["Keywords"][i])

file1=open("D:/Work/BTP/Extracted Data/1/India_today_1.csv")
reader1=csv.reader(file1)
lines1=len(list(reader1))     
print(lines1)

df=pd.read_csv("D:/Work/BTP/Extracted Data/1/India_today_1.csv")
for i in range(1,lines1,2):
     keywords.append(df["Keywords"][i])


file2=open("D:/Work/BTP/Extracted Data/1/yahoonews_data_1.csv",encoding="utf-8")
reader2=csv.reader(file2)
lines2=len(list(reader2))
print(lines2)

df2=pd.read_csv("D:/Work/BTP/Extracted Data/1/yahoonews_data_1.csv")
for i in range(1,lines2,2):
     keywords.append(df2["Keywords"][i])
# print(keywords)     


tfidf=TfidfVectorizer(tokenizer=tokenizer, stop_words=sw)
X=pd.DataFrame(tfidf.fit_transform(keywords).toarray(), columns=tfidf.get_feature_names())
# # print(a)

c=cluster.KMeans(70)
a=c.fit_predict(X)
print(a)
b=len(a)
print(b)

X['pred']=c.fit_predict(X)
# print(X['pred'])

X['keywords']=keywords
# print(X.loc[0]['keywords'])
print(X)
d=0
for i in range(0,b):
     d=max(d,X['pred'][i])


for i in range(0,b):
     for j in range(0,d+1):
          if X['pred'][i]==j:
               f=open("D:/Work/BTP/Extracted Data/1/"+str(j) +".txt","a+")
               f.write(X['keywords'][i]+'\n')
               f.close()
X.to_csv('f5.csv')