#!/usr/bin/env python
# coding: utf-8

# In[1]:


#to clean and revaluate certain components of data to display the averages of resultant forces and torques
import pandas as pd
import numpy as np


# In[2]:


pd.options.mode.chained_assignment = None


# In[3]:


lp4 = pd.read_csv('lp4.csv')


# In[4]:


lp4


# In[5]:


lp4.columns = ['Failure Type', 'Fx', 'Fy', 'Fz', 'Tx', 'Ty', 'Tz']
lp4.dtypes


# In[6]:


lp4_drop_fail = lp4.drop(columns = ['Failure Type'])
lp4_drop_nan = lp4_drop_fail.dropna(axis = 0)
lp4_working = lp4_drop_nan.reset_index(drop = True)
lp4_working


# In[7]:


lp4_working["F_resultant"] = np.sqrt(lp4_working["Fx"]**2 + lp4_working["Fy"]**2 + lp4_working["Fz"]**2)
lp4_working["T_resultant"] = np.sqrt(lp4_working["Tx"]**2 + lp4_working["Ty"]**2 + lp4_working["Tz"]**2)
lp4_working


# In[8]:


Avg_F_T_lp4 = lp4_working[['F_resultant', 'T_resultant']].copy()
Avg_F_T_lp4 = Avg_F_T_lp4.groupby(np.arange(len(Avg_F_T_lp4))//15).mean()
Avg_F_T_lp4


# In[9]:


Failure_type_col = lp4['Failure Type']
Failure = Failure_type_col.dropna(axis = 0)
Failure = Failure.reset_index(drop = True)
Avg_F_T_lp4['Failure Type'] = Failure
Avg_F_T_lp4


# In[10]:


Avg_F_T_lp4 = Avg_F_T_lp4[['Failure Type', 'F_resultant', 'T_resultant']]
Avg_F_T_lp4
Final_lp4 = Avg_F_T_lp4.to_csv('Final_lp4.csv', mode = 'w', index = False)


# In[18]:


Avg_F_T_lp4


# In[23]:


Avg_F_T_individual['Failure Type'] = Failure 
Avg_F_T_individual_lp4 = Avg_F_T_individual[['Failure Type', 'Fx', 'Fy', 'Fz', 'Tx', 'Ty', 'Tz']]


# In[24]:


Avg_F_T_individual_lp4


# In[25]:


Final_lp4_F_T_individual = Avg_F_T_individual_lp4.to_csv('Final_lp4_F_T_individual.csv', mode = 'w', index = False)
Final_lp4_F_T_individual


# In[27]:


df = pd.read_csv('Final_lp4_F_T_individual.csv')


# In[28]:


df


# In[ ]:




