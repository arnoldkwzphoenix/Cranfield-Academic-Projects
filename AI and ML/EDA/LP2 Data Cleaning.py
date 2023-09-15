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
lp2 = pd.read_csv('lp2.csv')
lp2


# In[4]:


#had to add this due to some conflict with the csv heading and df table heading
lp2.columns = ['Failure Type', 'Fx', 'Fy', 'Fz', 'Tx', 'Ty', 'Tz']


# In[5]:


lp2.dtypes


# In[6]:


lp2_drop_fail = lp2.drop(columns = ['Failure Type'])
lp2_drop_fail


# In[7]:


lp2_drop_nan = lp2_drop_fail.dropna(axis = 0)
lp2_working = lp2_drop_nan.reset_index(drop = True)


# In[8]:


lp2_working


# In[9]:


lp2_working.dtypes


# In[10]:


lp2_working["F_resultant"] = np.sqrt(lp2_working["Fx"]**2 + lp2_working["Fy"]**2 + lp2_working["Fz"]**2)
lp2_working["T_resultant"] = np.sqrt(lp2_working["Tx"]**2 + lp2_working["Ty"]**2 + lp2_working["Tz"]**2)
lp2_working


# In[11]:


Avg_F_T_lp2 = lp2_working[['F_resultant', 'T_resultant']].copy()


# In[12]:


Avg_F_T_lp2


# In[13]:


Avg_F_T_lp2 = Avg_F_T_lp2.groupby(np.arange(len(Avg_F_T_lp2))//15).mean()
Avg_F_T_lp2


# In[14]:


#failure type column extract
Failure_type_col = lp2["Failure Type"]
Failure_type_col


# In[15]:


Failure = Failure_type_col.dropna(axis = 0)
Failure


# In[16]:


Failure = Failure.reset_index(drop = True)


# In[17]:


Avg_F_T_lp2['Failure Type'] = Failure
Avg_F_T_lp2


# In[18]:


Avg_F_T_lp2 = Avg_F_T_lp2[['Failure Type', 'F_resultant', 'T_resultant']]
Avg_F_T_lp2


# In[19]:


Final_lp2 = Avg_F_T_lp2.to_csv('Final_lp2.csv', mode = 'w', index = False)


# In[20]:


F_T_individual_lp2 = lp2_working[['Fx', 'Fy', 'Fz', 'Tx', 'Ty', 'Tz']]
F_T_individual_lp2


# In[21]:


Avg_F_T_individual = F_T_individual_lp2.groupby(np.arange(len(F_T_individual_lp2))//15).mean()
Avg_F_T_individual


# In[23]:


Avg_F_T_individual['Failure Type'] = Failure 
Avg_F_T_individual = Avg_F_T_individual[['Failure Type', 'Fx', 'Fy', 'Fz', 'Tx', 'Ty', 'Tz']]


# In[24]:


Final_lp2_F_T_individual = Avg_F_T_individual.to_csv('Final_lp2_F_T_individual.csv', mode = 'w', index = False)


# In[26]:


Avg_F_T_individual


# In[ ]:




