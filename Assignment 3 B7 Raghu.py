#!/usr/bin/env python
# coding: utf-8

# In[8]:


altitude = int(input('Enter the altitude: '))
if (altitude <= 1000):
    print('Safe to Land')
elif (altitude > 1000 and  altitude <5000):
    print('altitute is',altitude,    'Bring down to 1000')
elif (altitude > 5000):
    print('Turn Around and try later')


# In[42]:


for i in range(1, 201):
    if i>1:
        for j in range(2, i):
            if i%j == 0:
                pass
#                 print(i,'is not prime')
                break
        else:
            print(i, end=' ')
    else:
        print(i,'is neither prime nor componsite')


# In[ ]:




