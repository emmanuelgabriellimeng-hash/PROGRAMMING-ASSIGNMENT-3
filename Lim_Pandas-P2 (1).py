#!/usr/bin/env python
# coding: utf-8

# # Experiment 3 - PANDAS
# ### Name: Emmanuel Gabriel M. Lim
# ### Section: 2ECE-B
# ### Date: September 10, 2025
# ### Subject Code: ECE2112

# ## Problem 2
# 
# Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
# indexing operations.
# 
#     a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

# In[87]:


import pandas as pd

cars = pd.read_csv("cars.csv")  
cars.iloc[0:5, ::2]


#     b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

# In[67]:


mazda_rx4_row = cars[cars['Model'] == 'Mazda RX4']
mazda_rx4_row


#     c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# In[68]:


cars.loc[[23], ['Model', 'cyl']]


# 
#     d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# In[70]:


selected_models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(selected_models), ['Model', 'cyl', 'gear']]

