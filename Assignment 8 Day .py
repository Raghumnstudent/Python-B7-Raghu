#!/usr/bin/env python
# coding: utf-8

# In[69]:


def decfunction(simple):
    def take_input():
        a = int(input('Enter number '))
        simple(a)
    return take_input


# In[42]:


@decfunction
def oddeven(num1):
    for i in range(1, num1):
        if i%2 == 0:
            print(i,' is Even')
        else:
            print(i,'is odd')


# In[70]:


oddeven()


# In[82]:


def decfunction(simple):
    def take_input():
        a = int(input('Enter Three digit Number only --> '))
        simple(a)
    return take_input


# In[83]:


@decfunction
def armstrong(number):
    digits = list(str(number))
    if int(digits[0])**3 + int(digits[1])**3 + int(digits[2])**3 == number:
        print(number, 'is ArmStrong Number ')
    else:
        print(number, 'is not  ArmStrong Number ')
        
        


# In[84]:


armstrong()


# In[ ]:





# In[14]:


try:
    myfile = open('Raghu.txt', 'r')
    myfile.write('Hey this is Raghu')
except Exception as e:
    print(e)


# In[15]:


try:
    myfile = open('Raghu.txt', 'q')
    myfile.write('Hey this is Raghu')
except Exception as e:
    print(e)


# In[ ]:




