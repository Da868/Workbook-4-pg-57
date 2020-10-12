#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bs = [1,1,0,0,1]
ms = [2,1,0,0,0]
phd = [0,1,0,0,0]


# In[4]:


GradeList = zip(names,grades,bs,ms,phd)
df = pd.DataFrame(data=GradeList,
 columns=['Name','Grade','BS','MS','PhD'])
df


# In[9]:


df['Grade'].count() 
df['Grade'].mean() 
df['Grade'].std() 
df['Grade'].min() 
df['Grade'].max() 
df['Grade'].quantile(.25)
df['Grade'].quantile(.5)
df['Grade'].quantile(.75)


# In[10]:


df['BS'].mode()


# In[11]:


df['MS'].median()


# In[13]:


df['Grade'].std()


# In[14]:


df['Grade'].count()


# In[15]:


df['Grade'].mean()


# In[16]:


df['Grade'].min()


# In[17]:


df['Grade'].max()


# In[18]:


df['Grade'].quantile(.25)


# In[19]:


df['Grade'].quantile(.5)


# In[20]:


df['Grade'].quantile(.75)


# In[ ]:




