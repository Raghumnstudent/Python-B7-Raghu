#!/usr/bin/env python
# coding: utf-8

# In[27]:


class account():
    def __init__(self, ownername, balance):
        self.ownername = ownername
        self.balance = balance
    def deposite(self, credited):
        self.credited = credited
        self.balance = self.balance + credited
        print('name is ', self.ownername, 'and balance is ', self.balance )
    def withdrawal(self, debited):
        self.debited = debited
        self.balance = self.balance - self.debited
        print('name is ', self.ownername, 'and balance is ', self.balance )
holder1 = account('Raghu', 50000)
holder2 = account('Ravi', 3450)
holder3 = account('sowmya', 30000)
holder4 = account('Naga', 2500)

print(holder1.ownername)
print(holder3.balance)

holder4.deposite(60000)
holder1.withdrawal(13459)
holder2.deposite(5000)
holder3.withdrawal(4583)
        


# In[26]:


# note I used formula as given only 

import math
class details():
    def __init__(self, name, Redius, Height):
        self.name = name
        self.Redius = Redius
        self.Height = Height
    def valumes(self):
        valume = (self.Height/3)
        print('name is ', self.name, 'valume is ', valume)
        
    def surfaceArea(self):
        base = (math.pi)*(pow(self.Redius, 2))
        side = (math.pi)*(self.Redius)*pow((pow(self.Redius, 2) + pow(self.Height,2)),0.5)
        print('name is ', self.name, 'base is ', base)
        print('name is ', self.name, 'side is ', side)
    
cylinder = details('cylinder', 5, 20)
sphere = details('sphere', 8, 28)

cylinder.valumes()
cylinder.surfaceArea()

sphere.valumes()
sphere.surfaceArea()


# In[ ]:





# In[ ]:




