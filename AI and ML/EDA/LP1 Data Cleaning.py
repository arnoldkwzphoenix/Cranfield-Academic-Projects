#!/usr/bin/env python
# coding: utf-8

# In[1]:


#to clean and revaluate certain components of data to display the averages of resultant forces and torques
import pandas as pd
import numpy as np
import math


# In[2]:


#to ignore certain warnings regarding copying/slicing pd
pd.options.mode.chained_assignment = None


# In[3]:


#read csv
lp1 = pd.read_csv('lp1_FT.csv')
lp1


# In[4]:


lp1.dtypes


# In[5]:


lp1.columns = ['Failure Type', 'Fx', 'Fy', 'Fz', 'Tx', 'Ty', 'Tz']


# In[6]:


lp1


# In[7]:


lp1_drop_Fail = lp1.drop(columns = ['Failure Type'])


# In[8]:


lp1_drop_Fail


# In[9]:


lp1_drop_nan = lp1_drop_Fail.dropna(axis = 0)


# In[10]:


lp1_drop_nan.reset_index(drop = True)


# In[11]:


#creating new columns for F resultant and T resultant
lp1_drop_nan["F_resultant"] = np.sqrt((lp1_drop_nan["Fx"]**2) + (lp1_drop_nan["Fy"]**2) + (lp1_drop_nan["Fz"]**2))
lp1_drop_nan["T_resultant"] = np.sqrt((lp1_drop_nan["Tx"]**2) + (lp1_drop_nan["Ty"]**2) + (lp1_drop_nan["Tz"]**2))


# In[12]:


#calling for F_resultant and T_resultant
lp1_drop_nan


# In[13]:


Avg_F_T = lp1_drop_nan[['F_resultant', 'T_resultant']].copy()


# In[14]:


Avg_F_T


# In[15]:


#using groupby to calculate for every 15 intervals (15 intervals == 1 subject)
Avg_FT= Avg_F_T.groupby(np.arange(len(Avg_F_T))//15).mean()


# In[16]:


Avg_FT


# In[17]:


#failure type column extract
Failure_type_col = lp1["Failure Type"]


# In[18]:


Failure_type_col


# In[19]:


Failure = Failure_type_col.dropna(axis = 0)


# In[20]:


Failure


# In[21]:


Failure = Failure.reset_index(drop = True)


# In[22]:


#combine the failure types and average F and T
Avg_FT['Failure Type'] = Failure 


# In[23]:


Avg_FT


# In[24]:


Avg_FT = Avg_FT[['Failure Type', 'F_resultant', 'T_resultant']]


# In[25]:


Avg_FT


# In[26]:


Final_lp1 = Avg_FT.to_csv('Final_lp1.csv', mode = 'w', index = False)


# In[27]:


#For individual Fx, Fy, Fz, Tx, Ty, Tz
F_T_individual = lp1_drop_nan[['Fx', 'Fy', 'Fz', 'Tx', 'Ty', 'Tz']]
F_T_individual


# In[28]:


#Getting Average of each failure for Fx, Fy, Fz, Tx, Ty, Tz
Avg_F_T_individual = F_T_individual.groupby(np.arange(len(Avg_F_T))//15).mean()


# In[29]:


Avg_F_T_individual


# In[35]:


Avg_F_T_individual['Failure Type'] = Failure 
Avg_F_T_individual = Avg_F_T_individual[['Failure Type', 'Fx', 'Fy', 'Fz', 'Tx', 'Ty', 'Tz']]


# In[36]:


Final_lp1_F_T_individual = Avg_F_T_individual.to_csv('Final_lp1_F_T_individual.csv', mode = 'w', index = False)


# In[37]:


F_T_individual.describe()


# In[32]:


Avg_FT.describe()


# In[38]:


Avg_F_T_individual


# In[ ]:




