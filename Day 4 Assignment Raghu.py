#!/usr/bin/env python
# coding: utf-8

# In[3]:


# ArmStrong Number in the range of 1042000 702648265 and exit the loop as soon as you encounter the first armstrong number?
# note please wait this code take 4 to 6 minute for execution 
# code is 100% correct and  Answer is 1741725 founded by this code
for i in range(1042000, 702648265):
    nq = str(i)
    n = len(nq)
    sn = int(nq[0])**n+int(nq[1])**n+int(nq[2])**n+int(nq[3])**n         +int(nq[4])**n+int(nq[5])**n+int(nq[6])**n
    while (i == sn):
        print(i)
        break
    if i == sn:
        break


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




