#!/usr/bin/env python
# coding: utf-8

# In[1]:


#to clean and revaluate certain components of data to display the averages of resultant forces and torques
import pandas as pd
import numpy as np


# In[2]:


pd.options.mode.chained_assignment = None


# In[3]:


lp3 = pd.read_csv('lp3.csv')


# In[4]:


lp3


# In[5]:


#had to add this due to some conflict with the csv heading and df table heading
lp3.columns = ['Part Position After Failure', 'Fx', 'Fy', 'Fz', 'Tx', 'Ty', 'Tz']
lp3.dtypes


# In[6]:


lp3_drop_fail = lp3.drop(columns = ['Part Position After Failure'])
lp3_drop_fail


# In[7]:


lp3_drop_nan = lp3_drop_fail.dropna(axis = 0)
lp3_working = lp3_drop_nan.reset_index(drop = True)
lp3_working


# In[8]:


lp3_working["F_resultant"] = np.sqrt(lp3_working["Fx"]**2 + lp3_working["Fy"]**2 + lp3_working["Fz"]**2)
lp3_working["T_resultant"] = np.sqrt(lp3_working["Tx"]**2 + lp3_working["Ty"]**2 + lp3_working["Tz"]**2)
lp3_working


# In[9]:


Avg_F_T_lp3 = lp3_working[['F_resultant', 'T_resultant']].copy()
Avg_F_T_lp3


# In[10]:


Avg_F_T_lp3 = Avg_F_T_lp3.groupby(np.arange(len(Avg_F_T_lp3))//15).mean()
Avg_F_T_lp3


# In[11]:


#failure type column extract
Failure_type_col = lp3["Part Position After Failure"]
Failure_type_col


# In[12]:


Failure = Failure_type_col.dropna(axis = 0)
Failure


# In[13]:


Failure = Failure.reset_index(drop = True)


# In[14]:


Avg_F_T_lp3['Part Position After Failure'] = Failure
Avg_F_T_lp3


# In[15]:


Avg_F_T_lp3 = Avg_F_T_lp3[['Part Position After Failure', 'F_resultant', 'T_resultant']]
Avg_F_T_lp3


# In[16]:


Final_lp3 = Avg_F_T_lp3.to_csv('Final_lp3.csv', mode = 'w', index = False)


# In[17]:


F_T_individual_lp3 = lp3_working[['Fx', 'Fy', 'Fz', 'Tx', 'Ty', 'Tz']]
F_T_individual_lp3


# In[18]:


Avg_F_T_individual = F_T_individual_lp3.groupby(np.arange(len(F_T_individual_lp3))//15).mean()
Avg_F_T_individual


# In[20]:


Avg_F_T_individual['Failure Type'] = Failure 
Avg_F_T_individual = Avg_F_T_individual[['Failure Type', 'Fx', 'Fy', 'Fz', 'Tx', 'Ty', 'Tz']]


# In[21]:


Final_lp3_F_T_individual = Avg_F_T_individual.to_csv('Final_lp3_F_T_individual.csv', mode = 'w', index = False)


# In[22]:


Avg_F_T_individual


# In[ ]:




