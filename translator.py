#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xlrd
import json
import matplotlib.pyplot as plt
from googletrans import Translator
from xlwt import Workbook, Formula


trad=Translator()
document= xlrd.open_workbook("F:\CS3_PFE\Gendarmerie\data\Classeur1.xlsx")
print("nombre de feuilles dans le document : " +str(document.nsheets))
feuille=document.sheet_by_index(0)
print("nombre de lignes dans la feuille : " +str(feuille.nrows))
print("nombre de colonnes dans le feuille : " +str(feuille.ncols))
frows= feuille.nrows
fcols=feuille.ncols
cel=feuille.cell_value(rowx=1,colx=2)
print(cel)
cellule=trad.translate(text=cel,dest='fr')
print(cellule.text)
ftraduit=Workbook()
traduit=ftraduit.add_sheet('traduit')
i=0
j=0
for colnum in range(fcols):    
    traduit.write(0,colnum,feuille.cell_value(0,colnum))
for rownum in range(frows-1):
    r=rownum+1
    print(r)
    lignei = traduit.row(r)
    for colnum in range(fcols):
        #print ("col :=")
        cel=feuille.cell_value(r,colnum)
        if (type(cel) != float):
            cellule1=trad.translate(text=cel,dest='fr')
            lignei.write(colnum,cellule1.text)

        else: 
            cellule1=cel
            lignei.write(colnum,cellule1)
ftraduit.save('F:\\ftraduit.xls')
print("done")

    


# In[ ]:


print ('hi')


# In[ ]:





# In[ ]:





# In[ ]:




