#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


# In[2]:


import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)


# In[3]:


#tackling eda in general for datasets lp1 to lp5
#only exception case is lp3 that represents the part position after failure
lp1 = pd.read_csv('Final_lp1.csv')
lp2 = pd.read_csv('Final_lp2.csv')
lp3 = pd.read_csv('Final_lp3.csv')
lp4 = pd.read_csv('Final_lp4.csv')
lp5 = pd.read_csv('Final_lp5.csv')


# In[4]:


#checking data
lp1.head()


# In[5]:


lp2.head()


# In[6]:


lp3.head()


# In[7]:


lp4.head()


# In[8]:


lp5.head()


# ## Countplot for Failure Types in Lp1 to Lp5

# In[15]:


#countplot to show number of errors in each dataset
f, axes = plt.subplots(5,1, figsize = (16, 20))
cp1 = sb.countplot(lp1['Failure Type'], ax = axes[0])
cp1.bar_label(cp1.containers[0])
cp2 = sb.countplot(lp2['Failure Type'], ax = axes[1])
cp2.bar_label(cp2.containers[0])
cp3 = sb.countplot(lp3['Part Position After Failure'], ax = axes[2])
cp3.bar_label(cp3.containers[0])
cp4 = sb.countplot(lp4['Failure Type'], ax = axes[3])
cp4.bar_label(cp4.containers[0])
cp5 = sb.countplot(lp5['Failure Type'], ax = axes[4])
cp5.bar_label(cp5.containers[0])


# ## Boxplot for F Resultant, T Resultant and Failure Types

# In[10]:


f, axes = plt.subplots(4,1, figsize = (16,24))
sb.boxplot(x = 'F_resultant', y = 'Failure Type', data = lp1, ax = axes[0])
sb.boxplot(x = 'F_resultant', y = 'Failure Type', data = lp2, ax = axes[1])
sb.boxplot(x = 'F_resultant', y = 'Failure Type', data = lp4, ax = axes[2])
sb.boxplot(x = 'F_resultant', y = 'Failure Type', data = lp5, ax = axes[3])


# In[11]:


f, axes = plt.subplots(4,1, figsize = (16,24))
sb.boxplot(x = 'T_resultant', y = 'Failure Type', data = lp1, ax = axes[0])
sb.boxplot(x = 'T_resultant', y = 'Failure Type', data = lp2, ax = axes[1])
sb.boxplot(x = 'T_resultant', y = 'Failure Type', data = lp4, ax = axes[2])
sb.boxplot(x = 'T_resultant', y = 'Failure Type', data = lp5, ax = axes[3])


# ## Correlation and Jointpoint

# In[12]:


corr_lp1 = lp1[['F_resultant', 'T_resultant']]
corr_lp1.corr()


# In[13]:


sb.jointplot(x = 'F_resultant', y = 'T_resultant', data = lp1, height = 6)


# In[14]:


corr_lp2 = lp2[['F_resultant', 'T_resultant']]
corr_lp2.corr()


# In[15]:


sb.jointplot(x = 'F_resultant', y = 'T_resultant', data = lp2, height = 6)


# In[16]:


corr_lp3 = lp3[['F_resultant', 'T_resultant']]
corr_lp3.corr()


# In[17]:


sb.jointplot(x = 'F_resultant', y = 'T_resultant', data = lp3, height = 6)


# In[18]:


corr_lp4 = lp4[['F_resultant', 'T_resultant']]
corr_lp4.corr()


# In[19]:


sb.jointplot(x = 'F_resultant', y = 'T_resultant', data = lp4, height = 6)


# In[20]:


corr_lp5 = lp5[['F_resultant', 'T_resultant']]
corr_lp5.corr()


# In[21]:


sb.jointplot(x = 'F_resultant', y = 'T_resultant', data = lp5, height = 6)


# ## Kernel Density Distribution for F resultant and T resultant

# In[22]:


f, axes = plt.subplots(5,1, figsize = (16,24))
sb.kdeplot(data = lp1, x = 'F_resultant', ax = axes[0])
sb.kdeplot(data = lp2, x = 'F_resultant', ax = axes[1])
sb.kdeplot(data = lp3, x = 'F_resultant', ax = axes[2])
sb.kdeplot(data = lp4, x = 'F_resultant', ax = axes[3])
sb.kdeplot(data = lp5, x = 'F_resultant', ax = axes[4])


# In[23]:


f, axes = plt.subplots(5,1, figsize = (16,24))
sb.kdeplot(data = lp1, x = 'T_resultant', ax = axes[0])
sb.kdeplot(data = lp2, x = 'T_resultant', ax = axes[1])
sb.kdeplot(data = lp3, x = 'T_resultant', ax = axes[2])
sb.kdeplot(data = lp4, x = 'T_resultant', ax = axes[3])
sb.kdeplot(data = lp5, x = 'T_resultant', ax = axes[4])


# ## Individual Fx, Fy, Fz, Tx, Ty, Tz

# In[24]:


lp1_individual = pd.read_csv('Final_lp1_F_T_individual.csv')
lp2_individual = pd.read_csv('Final_lp2_F_T_individual.csv')
lp3_individual = pd.read_csv('Final_lp3_F_T_individual.csv')
lp4_individual = pd.read_csv('Final_lp4_F_T_individual.csv')
lp5_individual = pd.read_csv('Final_lp5_F_T_individual.csv')


# In[29]:


f, axes = plt.subplots(5,1, figsize = (16,8))
sb.boxplot(x = 'Fx', data = lp1_individual, ax = axes[0])
sb.boxplot(x = 'Fx', data = lp2_individual, ax = axes[1])
sb.boxplot(x = 'Fx', data = lp3_individual, ax = axes[2])
sb.boxplot(x = 'Fx', data = lp4_individual, ax = axes[3])
sb.boxplot(x = 'Fx', data = lp5_individual, ax = axes[4])


# In[30]:


f, axes = plt.subplots(5,1, figsize = (16,5))
sb.boxplot(x = 'Tx', data = lp1_individual, ax = axes[0])
sb.boxplot(x = 'Tx', data = lp2_individual, ax = axes[1])
sb.boxplot(x = 'Tx', data = lp3_individual, ax = axes[2])
sb.boxplot(x = 'Tx', data = lp4_individual, ax = axes[3])
sb.boxplot(x = 'Tx', data = lp5_individual, ax = axes[4])


# In[34]:


f, axes = plt.subplots(5, 1, figsize = (16,5))
sb.boxplot(x = 'Fx', data = lp1_individual, ax = axes[0])
sb.boxplot(x = 'Fx', data = lp2_individual, ax = axes[1])
sb.boxplot(x = 'Fx', data = lp3_individual, ax = axes[2])
sb.boxplot(x = 'Fx', data = lp4_individual, ax = axes[3])
sb.boxplot(x = 'Fx', data = lp5_individual, ax = axes[4])


# In[44]:


f, axes = plt.subplots(5, figsize = (8,12))
sb.heatmap(lp1_individual.corr(), vmin = -1, vmax = 1, annot = True, fmt = '.2f', ax = axes[0])
sb.heatmap(lp2_individual.corr(), vmin = -1, vmax = 1, annot = True, fmt = '.2f', ax = axes[1])
sb.heatmap(lp3_individual.corr(), vmin = -1, vmax = 1, annot = True, fmt = '.2f', ax = axes[2])
sb.heatmap(lp4_individual.corr(), vmin = -1, vmax = 1, annot = True, fmt = '.2f', ax = axes[3])
sb.heatmap(lp5_individual.corr(), vmin = -1, vmax = 1, annot = True, fmt = '.2f', ax = axes[4])


# In[ ]:




