#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[9]:


data = pd.read_csv("data.csv")


# In[11]:


data.head()


# In[12]:


data.describe()


# In[13]:


data.apply(lambda x: sum(x.isnull()),axis=0)


# In[20]:


data['O3'].value_counts()


# In[21]:


data['O3'].fillna('16.31',inplace=True)


# In[19]:


print(data)


# In[14]:


data.drop(['O3'], axis=1)


# In[22]:


data['PM2.5'].value_counts()


# In[23]:


data['PM2.5'].fillna('14.92',inplace=True)


# In[24]:


print(data)


# In[25]:


data.drop(['PM2.5'], axis=1)


# In[26]:


data['Environmental_risk'].value_counts()


# In[27]:


data['Environmental_risk'].fillna('medio',inplace=True)


# In[28]:


print(data)


# In[29]:


data.drop(['Environmental_risk'], axis=1)


# In[ ]:




