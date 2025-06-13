#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sqlalchemy import create_engine


# In[3]:


engine = create_engine('postgresql://admin:admin123@localhost:5432/mydb')


# In[7]:


df=pd.read_csv('C:/Users/DELL/semigod_socials/extraction_scripts/recent_tracks.csv')


# In[10]:


pd.io.sql.get_schema(df, name='recent_tracks', con=engine)


# In[11]:


df.to_sql(name='recent_tracks', con=engine, if_exists='replace', index=False)
print("DataFrame written to SQL table 'recent_tracks' successfully.")


# In[ ]:




