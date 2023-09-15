#!/usr/bin/env python
# coding: utf-8

# In[11]:


### to clean and revaluate certain components of data to display the averages of resultant forces and torques
import pandas as pd
import numpy as np


# In[2]:


pd.options.mode.chained_assignment = None


# In[3]:


lp5 = pd.read_csv('lp5.csv')
lp5


# In[4]:


lp5.columns = ['Failure Type', 'Fx', 'Fy', 'Fz', 'Tx', 'Ty', 'Tz']
lp5.dtypes


# In[5]:


lp5_drop_fail = lp5.drop(columns = ['Failure Type'])
lp5_drop_nan = lp5_drop_fail.dropna(axis = 0)
lp5_working = lp5_drop_nan.reset_index(drop = True)
lp5_working


# In[15]:


lp5_drop_nan


# In[6]:


lp5_working["F_resultant"] = np.sqrt(lp5_working["Fx"]**2 + lp5_working["Fy"]**2 + lp5_working["Fz"]**2)
lp5_working["T_resultant"] = np.sqrt(lp5_working["Tx"]**2 + lp5_working["Ty"]**2 + lp5_working["Tz"]**2)
lp5_working


# In[7]:


Avg_F_T_lp5 = lp5_working[['F_resultant', 'T_resultant']].copy()
Avg_F_T_lp5 = Avg_F_T_lp5.groupby(np.arange(len(Avg_F_T_lp5))//15).mean()
Avg_F_T_lp5


# In[8]:


Failure_type_col = lp5['Failure Type']
Failure = Failure_type_col.dropna(axis = 0)
Failure = Failure.reset_index(drop = True)
Avg_F_T_lp5['Failure Type'] = Failure
Avg_F_T_lp5


# In[9]:


Avg_F_T_lp5 = Avg_F_T_lp5[['Failure Type', 'F_resultant', 'T_resultant']]
Avg_F_T_lp5
Final_lp5 = Avg_F_T_lp5.to_csv('Final_lp5.csv', mode = 'w', index = False)


# In[17]:


Avg_F_T_individual = lp5_drop_nan.groupby(np.arange(len(lp5_drop_nan))//15).mean()


# In[18]:


Avg_F_T_individual['Failure Type'] = Failure 
Avg_F_T_individual_lp5 = Avg_F_T_individual[['Failure Type', 'Fx', 'Fy', 'Fz', 'Tx', 'Ty', 'Tz']]


# In[19]:


Avg_F_T_individual_lp5


# In[20]:


Final_lp5_F_T_individual = Avg_F_T_individual_lp5.to_csv('Final_lp5_F_T_individual.csv', mode = 'w', index = False)
Final_lp5_F_T_individual


# In[21]:


df = pd.read_csv('Final_lp5_F_T_individual.csv')
df


# In[ ]:




