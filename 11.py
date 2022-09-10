a=[]
b=[]
c=[]
import xlrd 
loc = ("Edited_global_superstore_2016.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 

for i in range(1,51291): 
    a.append( sheet.cell_value(i, 10) )
for j in range(1,51291): 
    b.append( sheet.cell_value(j, 13) )
for k in range(1,51291): 
    c.append( sheet.cell_value(k, 14) )
    
import numpy as np
#t1=list(zip(a,b,c))
#d=np.array([  ((t1[l][0]-t1[m][0])**2 + (t1[l][1]-t1[m][1])**2 +(t1[l][2]-t1[m][2])**2 )**0.5 for l in range(len(t1)) for m in range(l,len(t1))])
         
t1=list(zip(a,b))
t2=list(zip(a,c))
#t3=list(zip(b,c))
t1=np.array(t1)
t2=np.array(t2)
#t3=np.array(t3)
d1=np.linalg.norm(t1-t2,axis=1)
#d2=np.linalg.norm(t1-t3,axis=1)
#d3=np.linalg.norm(t2-t3,axis=1)

from matplotlib import pyplot as plt
hist,bins=np.histogram(d1,100)
plt.hist(bins[:-1],bins,weights=hist)
plt.show()