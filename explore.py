#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# input data
train = pd.read_csv("data/train.csv")


# In[3]:


total_passengers = len(train.Survived)
total_survived = sum(train.Survived)
total_percent = total_survived/total_passengers*100


# In[4]:


print("Passengers: ", total_passengers, 
      "\nSurvived: ", total_survived, 
      "\nPercent: ", total_percent, "%")


# # Explore Ticket

# In[5]:


query = 'SOTON'
sel = []
for i, row in train.iterrows():
    if query in str(row.Ticket):
        sel.append(i)
sel_df = train.iloc[sel]


# In[6]:


sel_passengers = len(sel_df.Survived)
sel_survived = sum(sel_df.Survived)
sel_percent = sel_survived/sel_passengers*100


# In[7]:


print("Passengers: ", sel_passengers, 
      "\nSurvived: ", sel_survived, 
      "\nPercent: ", sel_percent, "%")


# In[8]:


print("Ports:",
     "\nC: ", len(sel_df.loc[sel_df.Embarked == 'C']),
     "\nQ: ", len(sel_df.loc[sel_df.Embarked == 'Q']),
     "\nS: ", len(sel_df.loc[sel_df.Embarked == 'S']),
     )

