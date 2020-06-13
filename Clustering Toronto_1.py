#!/usr/bin/env python
# coding: utf-8

# Segmenting Neighbourhoods in Toronto

# Installing and Importing Libraries
# BeautifulSoup4 and lxml for rendering the html data into readable table
# pandas for manipulating Dataframe

# In[3]:


#!pip install lxml
#!pip install wikipedia
#!pip install pandas
#!pip install html5lib
#!pip install BeautifulSoup4
#!pip install bs4
#import lxml as lx
import pandas as pd
#import wikipedia as wp
import requests
from bs4 import BeautifulSoup
#import html5lib as hh


# Getting website_text from requests library's get function
# Then converting html to xml content
# After that, finding the table in the entire page (its a wikitable sortale)
# Finally, creating empty lists to get the data from the table and converting the lists to a dataframe

# In[66]:


website_text = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text
soup = BeautifulSoup(website_text,'xml')
table = soup.find('table',{'class':'wikitable sortable'})
A=[]
B=[]
C=[]
for row in table.findAll('tr'):
    cells=row.findAll('td')
    if len(cells)==3:
        A.append(cells[0].find(text=True).strip())
        B.append(cells[1].find(text=True).strip())
        C.append(cells[2].find(text=True).strip())
#soup.prettify
#soup.title.string
df=pd.DataFrame(A,columns=['Postal Code'])
df['Borough']=B
df['Neighborhood']=C
df = df[df['Borough'] != 'Not assigned']
df.head()


# In[67]:


df.shape


# In[68]:


#df[['Postal Code']]
df.reset_index(drop=True, inplace=True)
#df['Postal Code'][0]
df.head()


# In[69]:


df_geo = pd.read_csv('Geospatial_Coordinates.csv')
df_geo.head()


# In[70]:


df_geo.shape


# In[71]:


df1 = df.merge(df_geo, left_on='Postal Code', right_on='Postal Code')
#df1.to_csv("joined_file.csv")
df1.head()

