#!/usr/bin/env python
# coding: utf-8

# # Experiment 3 - PANDAS
# ### Name: Emmanuel Gabriel M. Lim
# ### Section: 2ECE-B
# ### Date: September 10, 2025
# ### Subject Code: ECE2112

# ## Problem 1
# Using knowledge obtained from the experiment and demonstrations:
# 
#     a. Load the corresponding .csv file into a data frame named cars using pandas

# In[3]:


import pandas as pd

cars = pd.read_csv("cars.csv")  
cars


#     b. Display the first five and last five rows of the resulting cars.

# In[5]:


cars.head()


# In[6]:


cars.tail()

