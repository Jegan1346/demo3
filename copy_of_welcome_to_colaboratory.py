# -*- coding: utf-8 -*-
"""Copy of Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15dP0BefV1s-j023o7kpVXCnqLaX7X2lP
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("NetFlix.csv")

data.isnull().sum()

data.info()

data['date_added']=pd.to_datetime(data['date_added'])
data.head(2)

data= data.dropna(how='any',axis=0)
data

data2=data
samp=data2['genres'].str.split(",", expand=True)
data2.drop(['genres'],axis=1)
data1= pd.concat([data2,samp], axis=1, join='inner')



plt.figure(figsize=(15,16))
sns.countplot(y="release_year",data=data,hue='type')

plt.figure(figsize=(7,5))
sns.countplot(y="type",data=data)

plt.figure(figsize=(7,5))
sns.countplot(y="rating",data=data,hue='type')

data1

data1.columns = data1.columns.str.replace('NAN', 'genere1')

demo=pd.read_csv("NetFlix.csv")
demo.isnull().sum()

data.info()

added=data.groupby(pd.Grouper(key='date_added', freq='Y')).sum()
added

demo=pd.read_csv("NetFlix.csv")

demo["country"].fillna('Unavailable',inplace=True)

demo=demo.dropna(how='any',axis=0)

plt.figure(figsize=(15,16))
sns.countplot(y="release_year",data=demo,hue='type')

plt.figure(figsize=(7,5))
sns.countplot(data=demo,x="type")

movies=demo[demo['type']=='Movie']
tvshows=demo[demo['type']=='TV Show']

plt.figure(figsize=(12,6))
sns.countplot(y='country',order=demo['country'].value_counts().index[0:15],data=movies)
plt.title("Top 15 Countries producing movies")

plt.figure(figsize=(12,6))
sns.countplot(y='country',order=demo['country'].value_counts().index[0:15],data=tvshows)
plt.title("To 15 countries producing TV Shows")

plt.figure(figsize=(7,5))
sns.countplot(y="rating",order=demo['rating'].value_counts().index[0:15],data=movies)
plt.title("Movies by Ratings")

plt.figure(figsize=(7,5))
sns.countplot(y="rating",order=demo['rating'].value_counts().index[0:15],data=tvshows)
plt.title("TV Shows by Ratings")

demo['date_added']=pd.to_datetime(demo['date_added'])

demo['date_added']= demo['date_added'].dt.year

plt.figure(figsize=(7,5))
sns.countplot(y="date_added",order=demo['date_added'].value_counts().index[0:15],data=demo,hue='type')
plt.title("Contents added by year")

demo

