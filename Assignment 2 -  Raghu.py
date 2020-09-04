#!/usr/bin/env python
# coding: utf-8

# # List   and default function
# 
# 
# 

# In[28]:


fruits = ['Apple', 'Bannana', 'grapes']
print(fruits)

fruits.append('orange')
print('one more fruit added', fruits)


fruits.insert(2, 'watermelon')
print(fruits)

extra_fruits = ['papayas', 'kiwi']
fruits.extend(extra_fruits)
print(fruits)

print(fruits.pop())
print(fruits.pop(2))
print(fruits)

fruits.remove('Bannana')
print(fruits)


# # Dict and Defaults
# 

# In[53]:


score = dict([('kannada',97), ('math',56), ( 'Hindi',67),( 'science',76),('social science',87)])
print(score)

score['English'] = 78    # adding element to Dict
print(score)

print(score['math'])  #Accessing

del score['science']   # Deleting
print(score)

score.pop('English')
print(score)



# # set and Defaults

# In[59]:


courses = set(['Python', 'oops', 'java', 'javascript', 'java'])
print(courses)

courses.add('c')
print(courses)

courses.remove('oops')
print(courses)


# # Tuples and Defaults
# 

# In[76]:


name = tuple('raghu')
print(name)

num = (2, 4, 6, 78, 6, 'Raghu')  # tuple
print(num)

print(num[2:4])
print(num[-1])

num2 = (3, 5, 7, 9)
print(num + num2)

del num   #Deleting
# print(num)


# # String and Defaults

# In[89]:


name1 = str('raju')
print(name1)

print(type(name1))
print(name1[2])

print(name1.upper())
print(name1.lower())

print(len(name1))
print(name[-1])


# In[ ]:




