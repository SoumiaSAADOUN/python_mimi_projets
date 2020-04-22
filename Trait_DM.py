#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import xlrd
import xlsxwriter
import numpy as np
# Lire le fichier excel dans un dataframe pandas
df = pd.read_excel("F:\CS3_PFE\Gendarmerie\data\Classeur1.xlsx")


# In[2]:


print(df.head())


# In[3]:


print (df['NUM_ROUTE'])


# In[4]:


print(df['NUM_ROUTE'].isnull())


# In[5]:


#Liste des valeurs manquantes de mon fichier
missing_values=["/","//"]
df= pd.read_excel("F:\CS3_PFE\Gendarmerie\data\Classeur1.xlsx", na_values=missing_values)


# In[6]:


print(df['X'])


# In[7]:


print(df['Y'])


# In[8]:


# Nombre total de valeurs manquantes pour chaque attribut
print(df.isnull().sum())
# Nombre total de valeurs manquantes
print(df.isnull().sum().sum())


# In[9]:


print(df['ADVERSSER_ON'])
#del df['PK']
#print(df['ANNEE_PERMIS'].type)
#df.astype({'ANNEE_PERMIS': datetime.date, 'DATE_NAISS_CHAUFF': datetime.date})


# In[10]:


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('F:\\Classeur1.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet')
# Close the Pandas Excel writer and output the Excel file.
writer.save()


# In[ ]:




